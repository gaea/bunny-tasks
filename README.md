# bunny-tasks-api

## Project download
```
git clone https://github.com/gaea/bunny-tasks.git
```

## Project setup
```
cd bunny-tasks

python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt

export APP_SETTINGS_MODULE="config.local"
export FLASK_APP="app.py"

```
Database (postgres) connection have to be configured in the config/local.py

Database schema is specified in the database/schema.sql

### Run server for development
```
flask run
```
Development server will be running in http://127.0.0.1:5000/

### Test api
Import the postman collection located in the 'postman_collection folder'