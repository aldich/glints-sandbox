#Overview of the Process

Day 1

Setup VM based on linux to try install the PostgreSQL and Apache Airflow 
Progress:
1. PostgreSQL without Docker Installed
2. Docker Installed
3. Try to install PostgreSQL on Docker
4. Try to install Apache Airflow 

Progress so far:

sudo docker images
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
postgres     latest    577410342f45   2 days ago   374MB

sudo docker run -d --name postgres-server -p 5432:5432 -e "POSTGRESS_PASSWORD=tangSel" postgres
ad268d80f094135c2d2b11bc9f662ef73f4e9468f2ec6e2eec5c3ffa21ae1d29


ubuntu@ubuntu2110:~$ sudo docker volume create postgres-data-one
postgres-data-one
ubuntu@ubuntu2110:~$ sudo docker volume inspect postgres-data-one
[
    {
        "CreatedAt": "2021-11-20T19:15:37+07:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/postgres-data-one/_data",
        "Name": "postgres-data-one",
        "Options": {},
        "Scope": "local"
    }
]


root@ubuntu2110:~# docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e8afc16255c6   postgres   "docker-entrypoint.s…"   11 seconds ago   Up 10 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   postgres-server


Additional Setup to start PostgreSQL on Docker:
docker run -d --name postgres-server -p 5432:5432 -e "POSTGRESS_PASSWORD=tangSel" postgres
docker volume create postgres-data-one
docker volume inspect postgres-data-one

Try to setup another PostgreSQL on Docker:
docker run -d --name postgres-server-2 -p 5432:5432 -e "POSTGRES_PASSWORD=tangSel2" -d postgres2
docker stop postgres-server
docker rm postgres-server

Start the Airflow on Machine:
airflow webserver -p 5884
airflow scheduler

To Access the PostgreSQL DB: 
psql -h 127.0.0.1 -U postgres --password tangSel
CREATE DATABASE dailydlb;
CREATE DATABASE monthlydb;

\c dailydb;
CREATE TABLE transaction (id serial, creation_date date, sales_value int);
INSERT INTO transaction (id, creation_date, sales_value) values (1,'2021-11-20', 1000);
INSERT INTO transaction (id, creation_date, sales_value) values (2,'2021-11-20', 3000);


Day 2 

Loading data to Dockerize the PostgreSQL with Dockerize Apache Airflow 
Progress:
1. Installed PostgreSQL on Docker (for source and target)
2. Install Apache Airflow on Docker
3. Config the ETL Process (DAG from Apache Airflow)
4. Create documentation on the process

Progress so far:
1. Installed the prerequisite for Apache Airflow on Docker
2. Setup the config file (docker-compose.yaml)
3. Due to limitation of the hardware, Apache Airflow on Docker cannot be tested on Docker (screenshot attached) 
4. Switching to Apache Airflow on Machine
5. Setup the prerequisite (port 5884, setup the user and password for PostgreSQL access, setup the DAG for data processing) 
6. Initial test for loading the data from different table
7. Load Image to Hub (docker pull yonatanaldi/sandbox) 

Start Apache Airflow on Docker:
1. Get "curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.2/docker-compose.yaml'"
2. Create airflow-docker
3. Create folder dags, logs, plugins
4. Setup airflow user (echo -e "AIRFLOW_UID=$(id -u)" > .env)
5. Run initial setup (docker-compose up airflow-init)
6. Run Airflow on Docker (docker-compose up) --> failed 

Adding additional data on folder screenshot. 
Finishing documentation.
