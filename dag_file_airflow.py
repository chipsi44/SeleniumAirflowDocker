
'''
I'm the MoveAndRenameMe file ! 
'''

#I apologize, but I will not be using Jupyter Notebook in this file anymore.
#It is a requirement for the file to work properly.

'''
So anyways, the first step is to get our function back !
'''
from ressource.func import *
'''
Let's now create our DAGS ! 

Import datetime, timedelta
From airflow import dag and PythonOperator
Import os
'''
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'Cyril_AI',#your name
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 12, 23), #make it start at 23:00
    'retries': 0
}

dag = DAG(
    'dag_scrapping', # DAG name
    default_args=default_args,
    description='Scrapp financial info on Yahoo finance',
    schedule_interval=timedelta(days=1) # run every day
)

# Define the Python Operators that will run the functions
scrap_financeYahoo_operator = PythonOperator(
    task_id='Yahoo_scrapping',
    python_callable=scrap_to_csv,
    dag=dag
)


scrap_financeYahoo_operator


#Let's now go into the docker file