from airflow import DAG 
from airflow.providers.postgres.operators.postgres import PostgresOperator
import datetime
import pendulum

with DAG(
    dag_id = 'user_processing',
    start_date = pendulum.datetime(2023,9,19, tz = 'UTC'),
    schedule_interval = '@daily', 
    catchup = False
) as dag:
    
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id = 'postgres',
        sql = '''
        create table if not exists users(
            firstname text not null,
            lastname text not null,
            country text not null,
            username text not null,
            password text not null,
            email text not null
        );
        '''
    )