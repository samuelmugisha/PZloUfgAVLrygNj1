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

**1. 📥 Data Ingestion**
Input candidate data:
-  id
-  job_title
-  location
-  connections

**2. 🧹 Data Preprocessing & Feature Engineering**
**Text Processing**
- Normalize and clean job titles
- Tokenization and text standardization
  
**Connection Handling:**
- The `connection` column is cleaned by converting '500+' entries to 500 and casting the column to an integer type, making it numerically usable.
  
**Location One-Hot Encoding:**
- The categorical `location` column is transformed using `OneHotEncoder` into a set of binary features, allowing the model to incorporate geographical information.
  
**3. 🧠 Vectorization (Core Innovation)**

The system uses hybrid text representations:

  A. TF-IDF (Lexical Matching)
    - Captures keyword-level similarity
    - Useful for exact matches like “HR Intern”

  B. Transformer-based Embeddings
    - Generated using models like:
    - Sentence Transformers
    - BERT-like architectures
    - Captures semantic meaning
    
Example:
“Talent Acquisition Intern” ≈ “HR Intern”

  C. LLM-powered Representations (Advanced Layer)
    - Large Language Models enhance:
    - Context understanding
    - Role similarity
    - Ambiguous title interpretation
    - Helps bridge gaps where keywords fail

👉 This hybrid approach significantly improves candidate matching accuracy.

**4. 🧾 Feature Store**

  All features are combined into a unified feature matrix:
    - TF-IDF vectors
    - Transformer embeddings
    - Location features
    - Connections (numeric)
 
**5. 🤖 Machine Learning Model**

    Model: Random Forest Regressor
    Target: fit score (0–1)
    The model learns:
    Which features indicate strong candidate-role alignment
    Patterns from historical selections and feedback

**6. 🔍 Query Processing & Semantic Matching**

Example query:
        "Aspiring Human Resources"
        Processing Steps:
        Query is encoded using:
        TF-IDF
        Transformer embeddings
        (Optional) LLM-based encoding
        Compared against candidate representations
        Semantic similarity is computed

**7. 📊 Ranking Engine**

Final ranking score combines:
> *Final Score = Similarity Score + (ML Fit Score × Weight)*

Where:
Similarity comes from Transformer + TF-IDF matching
Fit score comes from ML predictions

**8. ⭐ Human Feedback Loop (Key Innovation)**

Recruiter reviews candidates
“Stars” an ideal candidate
This acts as:
A supervisory signal defining what a “good candidate” looks like

**9. 🔁 Dynamic Re-Ranking (Learning from Feedback)**

After a candidate is starred:
The system:
- Learns from the selected profile
- Identifies similar candidates using embeddings
- The model is retrained or adjusted
- Ranking updates dynamically

👉 This transforms the system from static ranking → adaptive intelligence

**10. 🎯 Filtering & Output**

- Score Threshold Filtering: A function filter_by_score_threshold is implemented to retain only candidates whose combined score meets a predefined minimum.
- Top-N Cut-off: The get_top_n_candidates function allows users to retrieve only the top N ranked individuals.
- Percentile-Based Cut-off: The get_candidates_above_percentile function dynamically filters candidates whose scores fall above a specified percentile, adapting to the score distribution.



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
**✅ Machine Learning Model (RandomForestRegressor)**
- R-squared (R2) Score: 0.8384
- Root Mean Squared Error (RMSE): 0.0392
These metrics indicate a strong predictive performance, with the model explaining approximately 83.84% of the variance in the 'fit' score and exhibiting a low average prediction error.

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
