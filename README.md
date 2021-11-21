# glints-sandbox

Hi, 

First of all, thank you for the opportunity and giving me a change to showcase this use case to you.
Proceeding to the technical part, I've only got the chance to setup 1 DB instance on Docker due to the limitation on my current hardware. 
Below is the user and passwor for the DB:
user: postgres 
pass: tangSel

For the Airflow setup, I've initially tried to setup it locally and move to the docker setup. 
Initial installation was successful and I've successfully setup the Apache Airflow UI and Scheduler. 
For the Docker part, unfortunately I haven't been able to start the service after the pre requisite setup for the Docker config due to my VM and hardware limitation. 

For access of the Airflow:
user: admin
pass: tangSel

For the docker-compose.yaml file that I setup was available on:
airflow-docker/docker-compose.yaml

For the ETL (Extract, Transform, and Load) process on the Airflow, I've setup the code to move a data from one table to another due the limitation on the DB setup. 
The file was available on:
airflow/dags/etl_job.py

For now, this's was the best that I can do due to my limited time and experience.

Thanks in advance.

Regards,
Aldi
