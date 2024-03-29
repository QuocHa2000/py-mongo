from flask import Flask, request, Response, jsonify
from werkzeug.exceptions import HTTPException
import json


def error_handling(app):
    @app.errorhandler(404)
    def not_found(error=None):
        message = jsonify({
            "message": "Resource Not Found :" + request.url,
            "status": 404
        })
        return message

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response
