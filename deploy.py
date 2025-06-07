name: Deploy Codex UI

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install streamlit

      - name: Run Codex UI (headless preview)
        run: streamlit run streamlit_ui/app.py --server.headless true --server.port 8501
