from flask import Blueprint, Response, current_app, json

userRouter = Blueprint("users", __name__)


@userRouter.route('/', methods=["GET"])
def getAllUser():
    return "Oke"
