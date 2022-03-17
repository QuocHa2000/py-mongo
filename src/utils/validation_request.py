

def validation(jsonSchema, argsSchema, viewArgsSchema, request):
    errors = []
    validatedData = []
    if (jsonSchema):
        try:
            jsonValidation = jsonSchema().load(request.get_json())
            validatedData.append(jsonValidation)
        except Exception as e:
            print("jsonSchemaErr", e)
            catchValidationError(errors=errors, e=e)
            pass

    if (argsSchema):
        try:
            argsValidation = argsSchema().load(request.args)
            validatedData.append(argsValidation)
        except Exception as e:
            print("argsSchemaErr", e)
            catchValidationError(errors=errors, e=e)
            pass

    if (viewArgsSchema):
        try:
            viewArgsValidation = viewArgsSchema().load(request.view_args)
            validatedData.append(viewArgsValidation)
        except Exception as e:
            print("viewArgsSchemaErr", e)
            catchValidationError(errors=errors, e=e)
            pass

    return [errors, validatedData]


def getValidationErrorValue(error_messages):
    error_list = []
    for key in error_messages:
        error_list.append(error_messages[key][0])
    return error_list


def catchValidationError(errors, e):
    errorList = getValidationErrorValue(e.messages)
    errors.extend(errorList)
