import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from t08_flask_mysql.app.my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()



def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)  # Ініціалізація бази даних
    register_routes(app)

    return app

def _init_db(app: Flask) -> None:
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    with app.app_context():
        db.create_all()




def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config.get(MYSQL_ROOT_USER, "root"))
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config.get(MYSQL_ROOT_PASSWORD, "root"))
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)