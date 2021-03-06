# Running Locally with Python
- Clone this repository
- Open the directory where you cloned
- Open your terminal (ctrl + l / cmd / code .)
- run the following commands
```shell
python -m venv .venv
```
if using linux
```shell
source venv/bin/activate
```
if using windows
```shell
.venv/Scripts/Activate
```
- Install the requirements
```shell
pip install -r requirements.txt
```
- Run the file
```shell
python fake_api_workflow.py
```
This run will append 10000 rows to 'taxfix-challlenge.db' to change the number of rows to append or to replace the table. Please see the documentation in 'fake_api_workflow.py'
# Quick explanation
All operations are stored in the 'faker' directory
- ingestion
- transformation
- data request

The file 'fake_api_workflow.py' is our main application that connects
all these operations. To see more details about how it works and the parameters please see the file's documentation.

# Essential Parameters
You might want to change the number of rows that you want to request from the faker-api.
To do this, all you have to do is change the value of the variable 'desired_number_of_rows' inside the file 'fake_api_workflow.py'. The default value is 10000

# Compressed Documentation
You will find more detailed explanation about each function or class in: docs/build/html/index.html

# How to run this application using Docker
Make sure you have installed:
* docker

# Build the image using the dockerfile
Open your terminal in the directory of this project
```shell
docker build -t tax .
```

# Create a container
Now you need to create/run the container with the image
that we just built
```shell
docker run -it --name taxfix-challenge tax
```

# Get the ID of your container
```shell
docker container ls -a
```
Search for the image of your container and copy it's ID

# Getting Data from the container
After that, we need to retrieve data from the container volume
To do that
```shell
sudo docker cp <your-container-id>:/taxfix-challenge.db /taxfix-challenge.db
```
If you are using Windows, you must open your powershell in admin mode
```shell
docker cp <your-container-id>:/taxfix-challenge.db /taxfix-challenge.db
```
This command is going to copy the .db file into your current directory
