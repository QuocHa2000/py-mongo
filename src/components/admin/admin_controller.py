from flask import Blueprint, Response, current_app, json, request, jsonify
adminRouter = Blueprint("admins", __name__)


@adminRouter.route("/<nam>", methods=["GET"])
def getAdmin(nam):
    try:
        # validate = validation_request.validation(
        #     jsonSchema=None, argsSchema=admin_validation.adminArgsSchema, viewArgsSchema=admin_validation.adminViewArgsSchema, request=request)
        # print(validate)
        # print(request.args)
        # print(request.view_args, nam)
        # try:
        #     validation = adminArgsSchema().load(request.args)
        #     print(validation)
        # except ValidationError as err:
        #     print("eeee", err)
        #     pass
        # print(request.view_args)
        # print(nam)
        return "asd"
    except Exception as e:
        print("eeeeeeeeee", e)
        pass


@adminRouter.route('/', methods=["GET"])
def getAllAdminsAccount():
    try:
        data = Admins.objects().values_list('email', 'name', 'phone').as_pymongo()
        return jsonify({'result': data})
    except Exception as e:
        print("eeeeeeeeee", e)
        pass
