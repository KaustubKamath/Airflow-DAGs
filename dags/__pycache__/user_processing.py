from airflow import DAG 
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json
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

    is_api_available = HttpSensor(
        task_id = 'is_api_available',
        http_conn_id= 'user_api',
        endpoint= 'api/'
    )

    extract_user = SimpleHttpOperator(
        task_id="extract_user",
        http_conn_id="user_api",
        endpoint='api/',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
        # response_check=lambda response: response.json()['json']['priority'] == 5,
        # response_filter=lambda response: json.loads(response.text),
        # extra_options: Optional[Dict[str, Any]] = None,
        # log_response: bool = False,
        # auth_type: Type[AuthBase] = HTTPBasicAuth,
    )