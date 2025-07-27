from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

default_args = {
    'owner': 'soumyadeep',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'fraud_detection_pipeline',
    default_args=default_args,
    description='ETL pipeline for bank fraud detection',
    schedule_interval='@daily',
    catchup=False,
)

# Define tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

# Task dependencies
extract_task >> transform_task >> load_task
