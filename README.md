# Airflow-DAGs

This repository contains the DAG built for learning and practice purposes.

# Airflow Setup

- The docker-compose file contains the required Docker containers required to run Airflow.
- .env file contains the Docker image name.

* Please refer to this [video](https://www.youtube.com/watch?v=6k1CyA5zYgg&t=249s) on how to install Docker Desktop.
* Once the Docker Desktop is installed, run the following command on the terminal, from within the directory where the docker-compose file is present `docker-compose up -d`.
* To access Airflow UI, open a web browser and go to `localhost:8080`.
* If you don't see the page, make sure nothing is running on the port 8080.
* To check about the status of the containers use `docker-compose ps`.
* To check logs about a container use `docker logs nameOfTheFolder-nameOfTheContainer`.
* To stop the containers use `docker-compose down`.
* To restart Airflow first use `docker-compose down` and then use `docker-compose up -d`.
* To remove the containers or if any error related to upgarding database use `docker volume prune` and then `docker-compose up -d`.
