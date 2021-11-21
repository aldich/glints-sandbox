import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

# create_pet_table, populate_pet_table, get_all_pets, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

with DAG(
    dag_id="load_table_data",
    start_date=datetime.datetime(2021, 11, 20),
    schedule_interval="@once",
    catchup=False,
) as dag:
    insert_initial_data = PostgresOperator(
        task_id="load_initial_data",
        sql="INSERT INTO transaction (id, creation_date, sales_value) values (1,'2021-11-20', 1000);",
    )

    load_to_backup_table = PostgresOperator(
	task_id="backup_data",
	sql="select id, creation_date, sales_value into table transaction_monthly from transaction;",
    )


insert_initial_data >> load_to_backup_table
