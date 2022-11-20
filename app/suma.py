# -*- coding: utf-8 -*-
from app.checker import Checker as checker
from app.error_codes import error_codes
from app.validators.allow_null import allow_null
from app.validators.presence import presence
from app.validators.format import format

validators = {
    "presence": presence,
    "format": format,
    "allow_null": allow_null,
}


def validate(value, validations: dict):
    result = []

    for key, options in validations.items():
        validator = validators.get(key)
        if not validator:
            raise Exception(f'Unknown validator "{key}"')
        validation = validator(value, options)
        if validation:
            result = [*result, *validation]

    return {"value": value, "errors": result}
