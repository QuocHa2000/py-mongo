from flask import Flask, app, current_app, abort, jsonify
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from routes import register_blueprints
from utils import error_handler


import logging
import time
import flask
import os
import yaml

config_file_path = os.path.dirname(
    os.path.abspath(__file__)) + "/config/config.yml"
config = (
    yaml.load(open(config_file_path), Loader=yaml.FullLoader)
    if os.path.isfile(config_file_path)
    else {}
)

default_config = {'MONGODB_SETTINGS': {
    'db': 'test_db',
    'host': 'localhost',
    'port': 27017,
    'username': '',
    'password': '',
    'authentication_source': 'admin'},
    # 'JWT_SECRET_KEY': 'changeThisKeyFirst'
}


def get_flask_app(config: dict = None) -> app.Flask:
    try:
        # Init Flask
        flask_app = Flask(__name__)

        # Config app
        config = config if config else default_config
        flask_app.config.update(config)

        # Add blueprint
        register_blueprints(flask_app=flask_app)

        # load config variable
        if "MONGODB_URI" in os.environ:
            flask_app.config['MONGODB_SETTINGS'] = {
                "host": os.environ["MONGODB_URI"], 'retryWrites': False}
        if "JWT_SECRET_KEY" in os.environ:
            flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

        # init api and routes
        api = Api(app=flask_app)

        # # Init jwt manager
        # jwt = JWTManager(app=flask_app)

        # Error handling
        error_handler.error_handling(flask_app)

        return flask_app
    except Exception as e:
        if e.messages:
            return jsonify({"error": e.messages})
        else:
            abort(500)


if __name__ == "__main__":
    while True:
        try:
            app = get_flask_app()
            app.run(host="0.0.0.0", port=3000, debug=True)
        except Exception as e:
            logging.error(e)
            time.sleep(10)
            pass
        else:
            break
