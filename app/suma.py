# -*- coding: utf-8 -*-
from app.checker import Checker
from app.error_codes import err, HerbsPYException
from app.validators.allow_null import allow_null
from app.validators.presence import presence
from app.validators.format import format
from app.validators.type import type_validator
from app.validators.type import type_validator
from app.validators.length import length
from app.validators.numericality import numericality
from app.validators.datetime_validator import datetime_validator
from app.validators.url import url
from app.validators.python_identifier import python_identifier
from app.validators.email import email
from app.validators.contains import contains
from app.validators.custom import custom

validators = {
    "presence": presence,
    "format": format,
    "allow_null": allow_null,
    "type": type_validator,
    "length": length,
    "numericality": numericality,
    "datetime_validator": datetime_validator,
    "url": url,
    "python_identifier": python_identifier,
    "email": email,
    "contains": contains,
    "custom": custom,
}


def validate(value, validations: dict):
    result = []

    for key, options in validations.items():
        validator = validators.get(key)
        if not validator:
            raise HerbsPYException(f'Unknown validator "{key}"')
        validation = validator(value, options)
        if validation:
            result = [*result, *validation]

    return {"value": value, "errors": result}


error_codes = err
checker = Checker
