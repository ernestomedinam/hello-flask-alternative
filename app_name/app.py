import os
from flask import Flask, jsonify
from flask_cors import CORS

from config import app_config

from app_name.db import db, migrate
from app_name.api import rest_api, docs, spec, jwt
from app_name.base.models.api_exception import APIException


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object("app_name.settings")
    config = app_config.config[config_name]
    app.config.from_object(config)
    config.init_app(app)
    app.config.update({"APISPEC_SPEC": spec})

    with app.app_context():
        import app_name.base.routes

        rest_api.init_app(app)

        CORS(app, supports_credentials=True)

        jwt.init_app(app)
        if not app.config["TESTING"]:
            db.init_app(app)
            migrate.init_app(app, db)

        docs.init_app(app)

        @app.errorhandler(APIException)
        def handle_invalid_usage(error):
            return jsonify(error.to_dict()), error.status_code

        return app
