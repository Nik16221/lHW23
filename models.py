from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_PARAMS = (
    "filter",
    "map",
    "unique",
    "sort",
    "limit"
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)  # обязательное поле для заполнения
    value = fields.Str(required=True)

    @validates_schema
    def validate_params(self, values, *args, **kwargs):
        if values["cmd"] not in VALID_CMD_PARAMS:
            raise ValidationError("неверно указано значение cmd")
        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
