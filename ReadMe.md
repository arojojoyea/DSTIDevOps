# WEB APPLICATION PROJECT
A web application programming interface on Python storing (CRUD) data in a database (MySQL, hosted online).

# FOLDER STRUCTURE


![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/folder_structure.png?raw=true)

- source_code : Code directory
- app.py :  Application Python file
- mysqlclient-1.4.6-cp39-cp39-win_amd64.whl : mysql wheel
- test.py : Test Pyton file
- Procfile :  List of Heroku process types in the app
- Readme.md
- requirements.txt  : List of all dependencies required to be installed in the container
runtime.txt

# File Description
- APP.PY: The Python application file
- DOCKER-COMPOSE.YML: The docker compose yaml config file
- DOCKERFILE:  The docker file
- mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
- requirements.txt:   The file listing all the environmental requirements to be installed in the container
- test.py: The Python file for testing 
- Procfile: For declaring what commands are run on the Heroku platform
  
# CI
The project is sent to a CI server (CircleCI)
![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/ci_img.png?raw=true)

# CD
The project is sent through a pipeline to an Heroku CD server
![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/heroku_page.png?raw=true)
![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/cd_show.png?raw=true)

# KUBERNETES
Kubernetes is set up for high availability.
![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/kuber/kuber_pic.png?raw=true)

![alt text](https://github.com/arojojoyea/DSTIDevOps/blob/main/kuber/kuber_pic2.png?raw=true)
