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

- Machine Learning (ML)
- Natural Language Processing (NLP)
- Transformer-based models and LLMs
- Human-in-the-loop feedback

The solution tackles a real-world hiring challenge:

> *How can we automatically identify the best candidates for a role and continuously improve rankings using human feedback?*

---

## 🎯 Objectives

- Predict candidate-job fit (`fit score`)
- Rank candidates based on relevance and suitability
- Dynamically re-rank candidates using recruiter feedback
- Reduce manual screening effort
- Build a system that improves over time
- Dynamic re-ranking based on new signals

---

## 🧠 Key Features

- ✅ Candidate filtering and preprocessing
- ✅ Transformer-based semantic understanding of job titles
- ✅ LLM-powered embeddings for deeper contextual matching
- ✅ Machine Learning model for fit prediction
- ✅ Ranking engine combining similarity + ML predictions
- ✅ Human feedback loop via “starring” candidates
- ✅ Dynamic re-ranking based on new signals 

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

---
## 📌 Future Improvements
- Fine-tune transformer models on hiring data
- Use advanced ranking models (LambdaMART, XGBoost Ranker)
- Real-time feedback integration
- Add explainability (feature importance, SHAP)
- Deploy as an API for ATS integration

---
## 🙌 Conclusion

This project demonstrates my ability to:

- Design end-to-end AI systems for real-world problems

- Combine: Machine Learning | Transformers | LLMs | Human feedback loops
- Build systems that are adaptive, scalable, and intelligent
---

From a hiring perspective, this project highlights:

✔ Strong ML + NLP + LLM integration skills
✔ Real-world system design thinking
✔ Ability to build production-oriented AI pipelines
✔ Understanding of ranking systems and feedback learning

---
👤 Author

Samuel Mugisha
Machine Learning | AI Systems 
