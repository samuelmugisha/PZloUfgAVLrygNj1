
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV NLTK_DATA=/usr/local/share/nltk_data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords punkt

COPY app.py .
RUN mkdir -p backend_files
COPY final_ranking_model.joblib backend_files/
COPY job_title_embeddings.joblib backend_files/
COPY tfidf_vectorizer.joblib backend_files/
COPY tfidf_matrix.joblib backend_files/

EXPOSE 7860

CMD sh -c "streamlit run app.py --server.port=7860 --server.address=0.0.0.0 --server.headless=true"
