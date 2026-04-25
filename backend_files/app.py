
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer # Import TfidfVectorizer
import time

st.set_page_config(
    page_title="Talent Sourcing App",
    layout="wide"
)

st.title("Talent Sourcing and Re-ranking Application")

# --- Helper Functions (from notebook) ---
def convert_connections_to_numeric(connection_str):
    if isinstance(connection_str, str) and connection_str.endswith('+'):
        return int(connection_str[:-1])
    try:
        return int(connection_str)
    except (ValueError, TypeError):
        return 0

def rerank_with_feedback(query, vectorizer_instance, vector_matrix_instance, dataframe, alpha=0.8):
    # Transform the query using the same vectorizer
    query_vector = vectorizer_instance.transform([query])

    # Calculate cosine similarity between the query and all job titles
    similarity_scores = cosine_similarity(query_vector, vector_matrix_instance).flatten()

    # Create a temporary DataFrame for ranking to avoid modifying the original df directly
    ranked_temp_df = dataframe.copy()
    ranked_temp_df['similarity_score'] = similarity_scores

    # Ensure 'numeric_connections' exists and is numeric for tie-breaking
    if 'numeric_connections' not in ranked_temp_df.columns:
        ranked_temp_df['numeric_connections'] = ranked_temp_df['connection'].apply(convert_connections_to_numeric)

    # Ensure 'fit' column exists and handle potential NaNs (e.g., fill with 0)
    if 'fit' not in ranked_temp_df.columns:
        ranked_temp_df['fit'] = 0.0
    else:
        ranked_temp_df['fit'] = ranked_temp_df['fit'].fillna(0.0)

    # Normalize fit score before combining with similarity
    max_fit = ranked_temp_df['fit'].max()
    if max_fit > 0:
        normalized_fit = ranked_temp_df['fit'] / max_fit
    else:
        normalized_fit = ranked_temp_df['fit'] # If all fit scores are 0, no normalization needed

    # Calculate the final combined score
    ranked_temp_df['final_score'] = alpha * ranked_temp_df['similarity_score'] + (1 - alpha) * normalized_fit

    # Sort by final_score (descending) and then by numeric_connections (descending)
    ranked_temp_df = ranked_temp_df.sort_values(
        by=['final_score', 'numeric_connections'],
        ascending=[False, False]
    )

    return ranked_temp_df


# --- Streamlit Application ---
st.markdown("Find and rank candidates based on job titles and user feedback.")
st.success("App loaded successfully") # New success message for app startup

# --- Model and Data Loading Logic ---
@st.cache_resource
def load_initial_resources():
    try:
        # Load the dataframe
        pipeline_data = joblib.load("backend_files/final_ranking_model.joblib")
        initial_df = pipeline_data['dataframe'].copy()
        initial_df['fit'] = 0.0 # Ensure 'fit' column is initialized

        # Load TF-IDF vectorizer and matrix
        tfidf_vectorizer = joblib.load("backend_files/tfidf_vectorizer.joblib")
        tfidf_matrix = joblib.load("backend_files/tfidf_matrix.joblib")

        return tfidf_vectorizer, tfidf_matrix, initial_df
    except FileNotFoundError:
        st.error("Error: Model or embedding file not found. Please ensure they are generated and saved.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading resources: {e}")
        st.stop()



# Initialize session state variables
if 'model_loaded_flag' not in st.session_state:
    st.session_state.model_loaded_flag = False
if 'vectorizer_instance' not in st.session_state: # Changed from sbert_model_instance
    st.session_state.vectorizer_instance = None
if 'vector_matrix_instance' not in st.session_state: # Changed from job_title_embeddings_instance
    st.session_state.vector_matrix_instance = None
if 'candidate_dataframe' not in st.session_state:
    st.session_state.candidate_dataframe = pd.DataFrame() # Placeholder until loaded

if not st.session_state.model_loaded_flag:
    if st.button("Load Ranking Model"):
        with st.spinner("Loading model and data... This may take a moment."):
            start_time = time.time()
            vectorizer_obj, vector_matrix_obj, initial_df = load_initial_resources()

            st.session_state.vectorizer_instance = vectorizer_obj
            st.session_state.vector_matrix_instance = vector_matrix_obj
            st.session_state.candidate_dataframe = initial_df

            st.session_state.model_loaded_flag = True
            end_time = time.time()
        st.success(f"Model and data loaded in {end_time - start_time:.2f} seconds!")
else:
    # Model is loaded, proceed with the app interface
    vectorizer_instance = st.session_state.vectorizer_instance
    vector_matrix_instance = st.session_state.vector_matrix_instance
    current_df = st.session_state.candidate_dataframe.copy() # Work with a copy to allow local modifications before updating session_state

    # --- Sidebar for Query and Parameters ---
    st.sidebar.header("Search Parameters")
    search_query = st.sidebar.text_input(
        "Enter a search query (e.g., 'aspiring human resources', 'full-stack software engineer')",
        value="aspiring human resources"
    )
    alpha_weight = st.sidebar.slider(
        "Weight for Similarity Score (alpha)",
        min_value=0.0,
        max_value=1.0,
        value=0.8,
        step=0.05,
        help="Higher alpha means more weight on job title similarity, lower means more weight on user feedback."
    )

    # --- Main Content Area ---
    if search_query:
        st.subheader(f"Results for: '{search_query}'")

        # Rerank using the session state dataframe
        ranked_df = rerank_with_feedback(search_query, vectorizer_instance, vector_matrix_instance, current_df, alpha=alpha_weight)

        st.markdown("### Top Candidates")

        # Display the top candidates
        display_df = ranked_df[['id', 'job_title', 'location', 'connection', 'similarity_score', 'fit', 'final_score']]
        st.dataframe(display_df.head(10))

    # --- Feedback Section (Moved to Sidebar) ---
    st.sidebar.markdown("--- ")
    st.sidebar.subheader("Provide Feedback")
    candidate_id_to_star = st.sidebar.number_input(
        "Enter Candidate ID to Star",
        min_value=int(current_df['id'].min()),
        max_value=int(current_df['id'].max()),
        step=1,
        value=72 # Default for demonstration
    )

    if st.sidebar.button("Star Candidate and Re-rank"):
        if candidate_id_to_star in st.session_state.candidate_dataframe['id'].values:
            # Update the 'fit' score directly in the session_state DataFrame
            st.session_state.candidate_dataframe.loc[st.session_state.candidate_dataframe['id'] == candidate_id_to_star, 'fit'] = 1.0
            st.sidebar.success(f"Candidate ID {candidate_id_to_star} starred! Re-ranking...")
            # Rerun the app to reflect changes
            st.experimental_rerun()
        else:
            st.sidebar.error(f"Candidate ID {candidate_id_to_star} not found.")

    st.sidebar.markdown("--- ")
    if st.sidebar.button("Reset Feedback"):
        st.session_state.candidate_dataframe['fit'] = 0.0
        st.sidebar.warning("All feedback reset. Rankings reverted to initial state.")
        st.experimental_rerun()
