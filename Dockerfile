# Dockerfile for Flowly Codex Init Anywhere
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_ui/app.py", "--server.enableCORS=false", "--server.port=8501"]
