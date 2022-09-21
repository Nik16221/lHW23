from typing import Iterable, Dict, Any

from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_PARAMS: Iterable[str] = (
    "filter",
    "map",
    "unique",
    "sort",
    "limit",
    "regex"
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)  # обязательное поле для заполнения
    value = fields.Str(required=True)

    @validates_schema
    def validate_params(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values["cmd"] not in VALID_CMD_PARAMS:
            raise ValidationError("неверно указано значение cmd")
        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
