# 🏦 Bank Transaction Fraud Detection Pipeline

This project builds an end-to-end ETL pipeline to process and detect fraudulent bank transactions.

## 🔍 Problem Statement
Financial institutions face the growing challenge of detecting fraudulent transactions in real-time. This project simulates such a scenario using rule-based anomaly detection and automates the pipeline with Python.

## 🧱 Tech Stack
- Python (Pandas, NumPy)
- ETL Scripted from Scratch
- CSV for input/output
- Visual Studio Code
- Git + GitHub for version control

## 📁 Project Structure
fraud_detection_pipeline/
│
├── data/                      # For raw sample data
├── dags/                      # For Airflow DAGs
├── etl/                       # For ETL scripts
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── dashboard/                 # For Streamlit visualization
│   └── app.py
├── utils/                     # For helper functions if needed
└── main.py                    # Main script to run components manually

## 🚀 How to Run the Pipeline?

```bash
python main.py
