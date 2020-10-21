# python-flask-basic-crud

## Postgres DB
```
docker run --rm -d \
-p 5432:5432 \
-e POSTGRES_DB=adb \
-e POSTGRES_USER=auser \
-e POSTGRES_PASSWORD=apassword \
postgres

docker run --rm -d \
-p 8080:3306 \
-e MYSQL_DATABASE=adb \
-e MYSQL_USER=auser \
-e MYSQL_PASSWORD=apassword \
-e MYSQL_ROOT_PASSWORD=rootpassword \
mysql:latest
```

To start the app
```
export FLASK_CONFIG='development'
export FLASK_APP=run.py
flask run
```

To migrate DB
```
flask db init     ## creates migrations directory
flask db migrate
flask db upgrade
```
# python-flask-basic-crud
