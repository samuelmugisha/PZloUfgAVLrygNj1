# 🚀 AI-Powered Talent Sourcing & Candidate Ranking System

![GitHub Repo stars](https://img.shields.io/github/stars/samuelmugisha/PZloUfgAVLrygNj1?style=social)
![GitHub forks](https://img.shields.io/github/forks/samuelmugisha/PZloUfgAVLrygNj1?style=social)
![License](https://img.shields.io/github/license/samuelmugisha/PZloUfgAVLrygNj1)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Transformers](https://img.shields.io/badge/Transformers-NLP-green)
![LLMs](https://img.shields.io/badge/LLMs-AI-purple)

---

## 📌 Project Overview

This project objective was to design an intelligent system to **identify, rank, and continuously improve candidate selection** for specific job roles.

The solution tackles a real-world hiring challenge:

**How can we automatically identify the best candidates for a role and continuously improve rankings using human feedback?**

To solve this, the system leverages a combination of:

- Natural Language Processing (NLP)
- Transformer-based models and LLMs
- Human-in-the-loop feedback

The solution tackles a real-world hiring challenge:

> *How can we automatically identify the best candidates for a role and continuously improve rankings using human feedback?*

---

## 🎯 Objectives

The goal of this project is to automate and improve the talent sourcing process. It tackles challenges such as identifying suitable candidates, ranking them effectively, and incorporating human feedback to continuously enhance the ranking system. The application leverages natural language processing (NLP) to understand job titles and determine candidate fit.

---

## 🧠 Key Features

- ✅ **Exploratory Data Analysis (EDA):** Initial analysis of candidate data, including connection distribution and top locations.
- ✅ **Text Preprocessing:** Cleaning and standardizing job titles using techniques like tokenization, stopword removal, stemming, and regex for noise reduction.
- ✅ **Text Vectorization:** Implementation and comparison of various methods to convert job titles into numerical representations:
    -   Bag of Words (BoW)
    -   TF-IDF (Term Frequency-Inverse Document Frequency)
    -   Word2Vec
    -   GloVe
    -   FastText
    -   BERT (Bidirectional Encoder Representations from Transformers)
    -   SBERT (Sentence-BERT)
- ✅ **User Feedback Re-ranking:** A mechanism to re-rank candidates by incorporating user feedback (e.g., 'starring' a candidate) to adjust their 'fit' score.
- ✅ **Streamlit Application:** A web application for interactive searching, ranking, and feedback collection.


---

## 🏗️ System Design Diagram

<center> <img src="data/System design.jpg" alt="System Design Diagram" width="900"></center>


---
## 🔄  End-to-End Workflow

The solution follows a comprehensive workflow to achieve its goals:

1.  **Data Loading & Initial Inspection:** Candidate data is loaded, and initial exploratory data analysis (EDA) is performed to understand its structure, identify missing values, and gain preliminary insights into `connection` and `location` distributions.
2.  **Text Preprocessing:** The `job_title` column undergoes a rigorous preprocessing pipeline including lowercasing, tokenization, regex-based cleaning, stopword removal, punctuation stripping, and Porter stemming. This ensures consistent and clean text for vectorization.
3.  **Text Vectorization & Comparison:** Cleaned job titles are transformed into numerical vectors using multiple techniques:
    *   **Lexical Models:** Bag of Words (BoW) and TF-IDF (Term Frequency-Inverse Document Frequency).
    *   **Word Embedding Models:** Word2Vec, GloVe, and FastText.
    *   **Contextual Embedding Models:** BERT and SBERT.
    Each method is used to rank candidates based on cosine similarity to a search query, and their performance is comparatively analyzed.
4.  **Re-ranking with User Feedback:** A crucial component, this module allows human feedback (e.g., 'starring' a candidate) to influence subsequent rankings. When a candidate is starred, their 'fit' score is updated, and a combined score (weighted average of similarity and normalized fit) is calculated for re-ranking.
5.  **Application Deployment:** The entire system is packaged into a Streamlit web application. Essential models (like `tfidf_vectorizer`) and processed dataframes are saved and loaded by the app. The application is deployed to Hugging Face Spaces using a `Dockerfile` and `requirements.txt` for environment setup.



---
## Bias Mitigation Strategies
- The project outlines strategies to prevent human bias, focusing on: diverse training data, transparency in ranking factors, regular model audits, and considering biases in features like location and connections.
- Robustness through Feedback: The iterative feedback loop is presented as a mechanism for continuous improvement and mitigating initial biases over time.

---
## Final output:

- High-quality ranked candidate list
- Evaluation Approach
- Ranking accuracy (top candidates relevance)
- Improvement after feedback loops
- Reduction in manual review time
- Semantic matching quality (LLM vs keyword baseline)

---

## 📈 Performance Benchmarks

**✅ Comparison of Ranking Methods (TF-IDF vs. Transformer vs. LLM)**

Upon comparing the combined scores (cosine similarity + weighted ML fit) for the query "Human Resources":
- TF-IDF + ML Fit: Consistently yielded the lowest combined scores (e.g., "Aspiring Human Resources Specialist" at 0.8496). This method, based on lexical matching, struggles with semantic nuances and often misses relevant candidates that do not contain exact keywords.
  
- Transformer (MiniLM) + ML Fit: Showed significantly higher scores (e.g., "Aspiring Human Resources Specialist" at 1.2744). This model excels at capturing contextual and semantic meaning, leading to more accurate and comprehensive identification of relevant job titles.

- LLM (paraphrase) + ML Fit: Also produced high scores (e.g., "Aspiring Human Resources Specialist" at 1.1467), demonstrating strong semantic understanding, particularly for paraphrased or related terms. For this specific query, the general-purpose all-MiniLM-L6-v2 performed slightly better than paraphrase-MiniLM-L6-v2 for the top results.

**✅ 💡 Key Insight**
- Transformer embeddings dramatically improve matching quality
- LLMs help capture nuanced job title meaning beyond keywords
- Hybrid systems (TF-IDF + Transformers + ML) outperform single approaches
- Human feedback is critical for continuous improvement
- Ranking systems benefit more from iteration than complexity alone

## ⚠️ Challenges & Considerations
- Noisy and inconsistent job titles
- Ambiguity in role definitions
- Bias introduced via human feedback
- Balancing semantic vs keyword matching
- Generalization across job domains

---
## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas / NumPy
- Sentence Transformers / BERT models
- LLM-based embedding techniques
- NLP (TF-IDF, semantic similarity)

## GitHub README

# Talent Sourcing and Ranking Application

This project develops a talent sourcing and ranking application designed to help identify and prioritize potential candidates for various roles based on their job titles and user feedback. It explores different text vectorization techniques and implements a re-ranking algorithm to refine candidate lists.

## Project Overview

The goal of this project is to automate and improve the talent sourcing process. It tackles challenges such as identifying suitable candidates, ranking them effectively, and incorporating human feedback to continuously enhance the ranking system. The application leverages natural language processing (NLP) to understand job titles and determine candidate fit.

## End-to-End Workflow

The solution follows a comprehensive workflow to achieve its goals:

1.  **Data Loading & Initial Inspection:** Candidate data is loaded, and initial exploratory data analysis (EDA) is performed to understand its structure, identify missing values, and gain preliminary insights into `connection` and `location` distributions.
2.  **Text Preprocessing:** The `job_title` column undergoes a rigorous preprocessing pipeline including lowercasing, tokenization, regex-based cleaning, stopword removal, punctuation stripping, and Porter stemming. This ensures consistent and clean text for vectorization.
3.  **Text Vectorization & Comparison:** Cleaned job titles are transformed into numerical vectors using multiple techniques:
    *   **Lexical Models:** Bag of Words (BoW) and TF-IDF (Term Frequency-Inverse Document Frequency).
    *   **Word Embedding Models:** Word2Vec, GloVe, and FastText.
    *   **Contextual Embedding Models:** BERT and SBERT.
    Each method is used to rank candidates based on cosine similarity to a search query, and their performance is comparatively analyzed.
4.  **Re-ranking with User Feedback:** A crucial component, this module allows human feedback (e.g., 'starring' a candidate) to influence subsequent rankings. When a candidate is starred, their 'fit' score is updated, and a combined score (weighted average of similarity and normalized fit) is calculated for re-ranking.
5.  **Application Deployment:** The entire system is packaged into a Streamlit web application. Essential models (like `tfidf_vectorizer`) and processed dataframes are saved and loaded by the app. The application is deployed to Hugging Face Spaces using a `Dockerfile` and `requirements.txt` for environment setup.

## Key Features

-   **Exploratory Data Analysis (EDA):** Initial analysis of candidate data, including connection distribution and top locations.
-   **Text Preprocessing:** Cleaning and standardizing job titles using techniques like tokenization, stopword removal, stemming, and regex for noise reduction.
-   **Text Vectorization:** Implementation and comparison of various methods to convert job titles into numerical representations:
    -   Bag of Words (BoW)
    -   TF-IDF (Term Frequency-Inverse Document Frequency)
    -   Word2Vec
    -   GloVe
    -   FastText
    -   BERT (Bidirectional Encoder Representations from Transformers)
    -   SBERT (Sentence-BERT)
-   **Cosine Similarity Ranking:** Ranking candidates based on the cosine similarity between a search query and their job title vectors.
-   **User Feedback Re-ranking:** A mechanism to re-rank candidates by incorporating user feedback (e.g., 'starring' a candidate) to adjust their 'fit' score.
-   **Streamlit Application:** A web application for interactive searching, ranking, and feedback collection.

## Tools Used

-   **Python:** The primary programming language.
-   **Jupyter/Google Colab:** For notebook development and experimentation.
-   **Pandas:** For data manipulation and analysis.
-   **NumPy:** For numerical operations.
-   **Scikit-learn:** For various machine learning utilities, including `TfidfVectorizer` and `cosine_similarity`.
-   **NLTK:** For natural language processing tasks like tokenization and stemming.
-   **Gensim:** For Word2Vec and FastText model handling.
-   **Hugging Face Transformers & Sentence-Transformers:** For BERT and SBERT embeddings.
-   **Matplotlib & Seaborn:** For data visualization.
-   **Streamlit:** For building the interactive web application.
-   **Hugging Face Spaces:** For deploying the web application.
---
## Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    The `requirements.txt` file lists all necessary Python packages.
    ```bash
    pip install -r backend_files/requirements.txt
    ```

4.  **Download NLTK data:**
    NLTK is used for text preprocessing. The `Dockerfile` handles this for deployment, but for local execution, you might need to download `stopwords` and `punkt` corpora.
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

5.  **Prepare `backend_files`:**
    Ensure that the `backend_files` directory contains the necessary model and data artifacts:
    -   `final_ranking_model.joblib` (DataFrame)
    -   `tfidf_vectorizer.joblib`
    -   `tfidf_matrix.joblib`
    -   `app.py` (Streamlit application script)
    -   `requirements.txt`
    -   `Dockerfile`

    *Note: These files are typically generated by running the full Jupyter/Colab notebook provided.* If you are using the Colab notebook, ensure you run all cells to generate these artifacts.

## Usage

Once installed, you can run the Streamlit application locally:

```bash
streamlit run backend_files/app.py
```

This will open the application in your web browser, usually at `http://localhost:8501`.
---
### Application Features:

-   **Search Query:** Enter a job title or role (e.g., "aspiring human resources", "full-stack software engineer") to get ranked candidates.
-   **Similarity Weight (Alpha):** Adjust the slider to control the influence of semantic similarity versus user feedback in the final ranking score.
-   **Star Candidate:** Select a candidate ID and click "Star Candidate and Re-rank" to mark them as a good fit. The system will then re-rank the candidates, giving more weight to previously starred individuals.
-   **Reset Feedback:** Clear all user feedback to revert to the initial similarity-based ranking.

### Deployment to Hugging Face Spaces:

- The project includes a `Dockerfile` and `requirements.txt` to facilitate deployment on platforms like Hugging Face Spaces. The notebook automates the process of saving necessary files into the `backend_files` directory and uploading them to a specified Hugging Face Space.
---
###  🙌 Conclusion

- This project demonstrates a robust approach to talent sourcing using various NLP techniques. The comparative analysis of vectorization methods highlights the trade-offs between lexical (BoW, TF-IDF) and semantic (Word2Vec, GloVe, FastText, BERT, SBERT) models. The implemented re-ranking mechanism further enhances the system's adaptability and accuracy by incorporating valuable human feedback.

- From a hiring perspective, this project highlights:
✔ Strong ML + NLP + LLM integration skills
✔ Real-world system design thinking
✔ Ability to build production-oriented AI pipelines
✔ Understanding of ranking systems and feedback learning
---
## 📌 Future Improvements
- Fine-tune transformer models on hiring data
- Use advanced ranking models (LambdaMART, XGBoost Ranker)
- Real-time feedback integration
- Add explainability (feature importance, SHAP)
- Deploy as an API for ATS integration

---

---
👤 Author

Samuel Mugisha
Machine Learning | AI Systems 
