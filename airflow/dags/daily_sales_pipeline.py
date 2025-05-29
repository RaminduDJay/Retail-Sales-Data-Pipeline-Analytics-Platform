from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG('daily_sales_pipeline',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False,
         description='Daily retail sales pipeline'
         ) as dag:

    ingest_task = BashOperator(
        task_id='ingest_sales_data',
        bash_command='D:/Projects/Retail Sales Data Pipeline & Analytics Platform/New folder/Retail-Sales-Data-Pipeline-Analytics-Platform/scripts/ingest.py'
    )

    dbt_run_task = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd D:/Projects/Retail Sales Data Pipeline & Analytics Platform/New folder/Retail-Sales-Data-Pipeline-Analytics-Platform/dbt_project/retail_transform && dbt run'
    )

    ingest_task >> dbt_run_task
