# Rick and Morty API Project

## Installation
The project uses a Mongo database instance and some Python libraries such as `flask`, `requests` and `pymongo`. The Python version used is `3.9.5`.

### MongoDB
There are three alternatives to using MongoDB:

1. Downloading and installing on your machine: [Mongo's official website](https://www.mongodb.com/)
2. Creating a free instance in Atlas: [Mongo Atlas](https://www.mongodb.com/cloud/atlas)
3. Using a ready-made docker image: [link to Docker Hub](https://hub.docker.com/_/mongo)

### Python Libraries
All project dependencies are in the file [requirements.txt](requirements.txt). To install them, just run

     pip install -r requirements.txt

In Windows PowerShell or Unix Terminal (Linux/MacOS). Additionally, you may want to run this command from within a [virtual environment](https://docs.python.org/en-us/3/library/venv.html).

## Settings
The project has a simple configuration that consists of optionally setting two environment variables: `MONGO_DBNAME` and `MONGO_CONN_URL`, as seen in the [config.py](config.py) file.

The environment variable `MONGO_CONN_URL` is only needed if you use the Atlas instance. If installing locally or using a docker (with the appropriate ports exposed), it should not be necessary.

## Execution
     python app.py

The above command raises a Flask server on port 5000 which can be accessed by [http://localhost:5000](http://localhost:5000).
