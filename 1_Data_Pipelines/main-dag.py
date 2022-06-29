import os
import sys
sys.path.append(r'C:\Users\chenl\OneDrive\Desktop\Data-Engineer-Tech-Challenge-master')
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from main import main


# Setting arguments
args = {'owner': 'Lianghe Chen',
        'start_date': days_ago(0)}

# Defining the dag object
dag = DAG(dag_id='main-dag',
          default_args=args,
          #schedule_interval='@once'
          schedule_interval='00 01 * * *',
         ) # To make this workflow happen every day at 1am

# Assigning the task for our dag
with dag:
    data_pipelines = PythonOperator(task_id='main',
                                    python_callable=main)