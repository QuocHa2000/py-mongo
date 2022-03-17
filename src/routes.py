from flask import Blueprint, current_app, abort, jsonify
from components.admin.admin_controller import adminRouter
from components.users.user_controller import userRouter


def register_blueprints(flask_app):
    try:
        with flask_app.app_context():
            current_app.register_blueprint(
                adminRouter, url_prefix='/admin')
            current_app.register_blueprint(userRouter, url_prefix="/user")
    except Exception as e:
        pass
