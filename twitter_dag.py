from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter_etl import run_twitter_etl

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),  # Use a realistic recent start_date
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "twitter_etl_dag",
    default_args=default_args,
    description="Daily ETL from Twitter using Tweepy and Airflow",
    schedule_interval=timedelta(days=1),
    catchup=False,  # prevents backfilling for past dates
)

run_etl = PythonOperator(
    task_id="extract_twitter_data",
    python_callable=run_twitter_etl,
    dag=dag,
)

run_etl
