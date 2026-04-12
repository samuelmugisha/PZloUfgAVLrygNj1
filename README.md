# Talent Sourcing and Ranking Solution

## Project Overview

This project develops a sophisticated, machine learning-powered pipeline designed to automate and enhance the talent sourcing and ranking process for a talent management company. The core objective is to identify, rank, and dynamically re-rank potential candidates based on their fitness for specific roles, moving beyond traditional keyword-based searches to leverage advanced Natural Language Processing (NLP) and supervised learning techniques.

The solution addresses challenges such as improving ranking accuracy, incorporating human feedback, filtering candidates effectively, and mitigating bias. By combining lexical and semantic understanding of job titles with other candidate attributes and an adaptive 'fit' scoring mechanism, this system provides a robust and intelligent tool for efficient talent acquisition.

## Key Features

*   **Hybrid Ranking System:** Combines semantic similarity (from job titles) with a learned 'fit' score from a machine learning model.
*   **Adaptive Re-ranking:** Incorporates human supervisory signals (e.g., 'starring' a candidate) to dynamically update rankings.
*   **Advanced NLP:** Utilizes TF-IDF, Sentence Transformers (SBERT), and Large Language Model (LLM) embeddings for nuanced job title analysis.
*   **Comprehensive Feature Engineering:** Integrates `location` (one-hot encoded) and `connections` (numerical) for a holistic candidate profile.
*   **Flexible Filtering Strategies:** Implements score threshold, top-N, and percentile-based cut-offs for managing candidate lists.
*   **Bias Mitigation:** Proposes strategies for preventing human bias through diverse data, transparency, and model audits.

## Project Flow: Step-by-Step Implementation

### 1. Data Loading and Exploratory Data Analysis (EDA)

*   **Loading Data:** Candidate data is loaded from a CSV file into a Pandas DataFrame.
*   **Initial Inspection:** `df.head()` and `df.info()` are used to understand data structure, column types, and identify missing values.
*   **Distribution Analysis:** Histograms for `connection` and bar plots for `location` and `job_title` word frequencies are generated to reveal key patterns (e.g., dominance of '500+' connections, top locations, and prevalence of 'Human Resources' terms).

### 2. Text Preprocessing for Job Titles

*   **Cleaning Function (`process_words`):** A custom function is developed to clean, tokenize, remove stopwords, and stem job title strings. This ensures consistency and prepares text for vectorization.
*   **Tokenization and Stemming:** The `job_title` column is processed to create a `processed_job_title` column, containing lists of cleaned and stemmed tokens.

### 3. Feature Engineering and Vectorization

*   **TF-IDF Vectorization:** `TfidfVectorizer` is applied to cleaned job titles to convert them into numerical TF-IDF vectors. This captures the importance of words in each title relative to the entire dataset.
*   **Connection Handling:** The `connection` column is cleaned by converting '500+' entries to 500 and casting the column to an integer type, making it numerically usable.
*   **Location One-Hot Encoding:** The categorical `location` column is transformed using `OneHotEncoder` into a set of binary features, allowing the model to incorporate geographical information.
*   **Feature Combination:** All processed features (TF-IDF vectors, one-hot encoded locations, and numerical connections) are combined into a single feature matrix `X`.

### 4. Machine Learning Model Training

*   **Target Variable (`y`):** The `fit` column, initially with `NaN` values, is initialized to `0.0`. Supervisory signals (e.g., 'starring' a candidate) will update these values to `1.0`.
*   **Model Selection:** A `RandomForestRegressor` is chosen for its robustness and ability to handle complex relationships. 
*   **Model Training:** The model is trained on the combined feature matrix `X` and the target variable `y` to predict candidate 'fit' scores.
*   **Model Evaluation:** Performance is assessed using R-squared (R2) score and Root Mean Squared Error (RMSE), alongside a plot of actual vs. predicted `fit` scores.

### 5. Supervisory Signal Integration and Adaptive Re-ranking

*   **Initial 'Starring':** A specific job title (e.g., "Human Resources Professional") is 'starred' by manually setting its `fit` value to `1.0` in the DataFrame. This simulates initial human feedback.
*   **Ranking Function Modification:** The `search_job_titles_with_supervisory_signal` function is introduced. This function calculates a combined score: `cosine_similarity + (model.predict(X) * fit_weight)`.
*   **Demonstrating Re-ranking:** By comparing rankings before and after starring and retraining the model, the system's ability to adapt and boost the position of preferred candidates is clearly demonstrated.
*   **Iterative Feedback Loop:** The process of 'starring' new candidates (e.g., "Aspiring Human Resources Specialist") and retraining the model is shown to further refine rankings, showcasing the system's continuous learning capability.

### 6. Advanced NLP for Semantic Search

*   **Sentence Transformers (SBERT) Integration:** A pre-trained SBERT model (`all-MiniLM-L6-v2`) is loaded to generate context-aware embeddings for job titles. This improves semantic understanding beyond basic keyword matching.
*   **Large Language Model (LLM) Integration:** An LLM-based model (`paraphrase-MiniLM-L6-v2`) is also utilized to generate richer, semantically-focused embeddings, enhancing the ability to find related job titles even with varied phrasing.
*   **Comparison of Methods:** A detailed comparison (using bar plots and data tables) highlights the superior semantic understanding and higher relevance scores achieved by Transformer and LLM-based approaches compared to traditional TF-IDF.

### 7. Filtering and Cut-off Strategies

*   **Score Threshold Filtering:** A function `filter_by_score_threshold` is implemented to retain only candidates whose combined score meets a predefined minimum.
*   **Top-N Cut-off:** The `get_top_n_candidates` function allows users to retrieve only the top `N` ranked individuals.
*   **Percentile-Based Cut-off:** The `get_candidates_above_percentile` function dynamically filters candidates whose scores fall above a specified percentile, adapting to the score distribution.

### 8. Bias Mitigation Strategies

*   **Discussion:** The project outlines strategies to prevent human bias, focusing on: diverse training data, transparency in ranking factors, regular model audits, and considering biases in features like `location` and `connections`.
*   **Robustness through Feedback:** The iterative feedback loop is presented as a mechanism for continuous improvement and mitigating initial biases over time.


## Performance Benchmarks

### Machine Learning Model (RandomForestRegressor)

*   **R-squared (R2) Score:** 0.8384
*   **Root Mean Squared Error (RMSE):** 0.0392

These metrics indicate a strong predictive performance, with the model explaining approximately 83.84% of the variance in the 'fit' score and exhibiting a low average prediction error.

### Comparison of Ranking Methods (TF-IDF vs. Transformer vs. LLM)

Upon comparing the combined scores (cosine similarity + weighted ML fit) for the query "Human Resources":

*   **TF-IDF + ML Fit:** Consistently yielded the lowest combined scores (e.g., "Aspiring Human Resources Specialist" at 0.8496). This method, based on lexical matching, struggles with semantic nuances and often misses relevant candidates that do not contain exact keywords.
*   **Transformer (MiniLM) + ML Fit:** Showed significantly higher scores (e.g., "Aspiring Human Resources Specialist" at 1.2744). This model excels at capturing contextual and semantic meaning, leading to more accurate and comprehensive identification of relevant job titles.
*   **LLM (paraphrase) + ML Fit:** Also produced high scores (e.g., "Aspiring Human Resources Specialist" at 1.1467), demonstrating strong semantic understanding, particularly for paraphrased or related terms. For this specific query, the general-purpose `all-MiniLM-L6-v2` performed slightly better than `paraphrase-MiniLM-L6-v2` for the top results.

**Key Insight:** Transformer and LLM-based approaches provide superior semantic understanding compared to TF-IDF, leading to higher relevance scores and the ability to identify a broader, more nuanced set of potential candidates, even when job titles use varied phrasing. This enhanced semantic understanding is crucial for effective talent sourcing.

## Tools and Technologies Used

*   **Programming Language:** Python
*   **Data Manipulation:** Pandas, NumPy
*   **Machine Learning:** Scikit-learn (TfidfVectorizer, OneHotEncoder, RandomForestRegressor, cosine_similarity)
*   **Natural Language Processing:** NLTK (stopwords, punkt, PorterStemmer), Sentence Transformers (all-MiniLM-L6-v2, paraphrase-MiniLM-L6-v2)
*   **Visualization:** Matplotlib, Seaborn

## Concluding Remarks for Hiring Managers and Recruiters

This project demonstrates a robust and intelligent approach to talent sourcing, leveraging cutting-edge machine learning and natural language processing techniques. As a significant contributor to this initiative, I have actively shaped a solution that not only automates a traditionally manual and labor-intensive process but also introduces a critical layer of adaptability and continuous improvement.

My contributions include:

*   **Designing and implementing a hybrid ranking algorithm** that intelligently combines lexical and semantic text similarity with a learned 'fit' score, moving beyond simple keyword matching to genuinely understand the nuances of job roles and candidate profiles.
*   **Developing an iterative feedback mechanism** that allows human insights to directly influence and refine the ranking model. This ensures the system constantly learns from expert feedback, adapts to evolving preferences, and delivers increasingly precise results, reducing the time and effort required to identify ideal candidates.
*   **Integrating advanced NLP models (Sentence Transformers and LLMs)** to unlock deeper semantic understanding, enabling the discovery of highly relevant candidates whose titles might not contain exact keywords but are conceptually aligned. This expands the talent pool and uncovers 'hidden gems' often missed by traditional methods.
*   **Implementing flexible filtering and cut-off strategies** that provide granular control over candidate lists, empowering recruiters to efficiently manage pipeline volume without sacrificing quality.
*   **Actively considering and proposing strategies for bias mitigation**, demonstrating a commitment to ethical AI development and fostering fair, inclusive hiring practices.

This project showcases my ability to translate complex business problems into actionable, data-driven solutions, employing a diverse toolkit of ML and NLP techniques. It highlights my dedication to building systems that are not only efficient but also intelligent, adaptable, and ethically conscious—qualities essential for modern talent acquisition challenges.

