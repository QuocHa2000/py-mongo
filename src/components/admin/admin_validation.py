from marshmallow import Schema, ValidationError, fields, validate


class adminArgsSchema(Schema):
    name = fields.Str(validate=validate.Length(min=10), required=True)

    class Meta:
        strict = True


class adminViewArgsSchema(Schema):
    nam = fields.Str(validate=validate.Length(min=3), required=True)

    class Meta:
        strict = True
