from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(app_config[config_name]) ## load from config.py
    app.config.from_pyfile('config.py')             ## load from instance/config.py

    Bootstrap(app)
    
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in."
    login_manager.login_view = "auth.login"

    ## DB migrations with Alembic
    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as blueprint_admin
    app.register_blueprint(blueprint_admin, url_prefix='/admin')
    from .auth import auth as blueprint_auth
    app.register_blueprint(blueprint_auth)
    from .home import home as blueprint_home
    app.register_blueprint(blueprint_home)

    return app

## Load views
# from app import views
