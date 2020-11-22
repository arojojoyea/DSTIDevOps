# WEB APPLICATION PROJECT
A web application on Python storing (CRUD) data in a database (MySQL, hosted online).

# FOLDER STRUCTURE
.

├───.circleci
├───source_code #Code directory
│   ├─── app.py #Application Python file
│   ├── mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
│   └── test.py #Test Pyton file
├─── Procfile
├─── Readme.md
├─── requirements.txt
└─── runtime.txt


# File Description
APP.PY: The Python application file
DOCKER-COMPOSE.YML: The docker compose yaml config file
DOCKERFILE:  The docker file
mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
requirements.txt:   The file listing all the environmental requirements to be installed in the container
test.py: The Python file for testing 
Procfile: For declaring what commands are run on the Heroku platform
  
# CI
The project is sent to a CI server (CircleCI)
![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/ci_img.png?raw=true)

