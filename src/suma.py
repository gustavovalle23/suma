# -*- coding: utf-8 -*-
from src.checker import Checker
from src.error_codes import err, HerbsPYException
from src.validators.allow_null import allow_null
from src.validators.presence import presence
from src.validators.format import format
from src.validators.type import type_validator
from src.validators.type import type_validator
from src.validators.length import length
from src.validators.numericality import numericality
from src.validators.datetime_validator import datetime_validator
from src.validators.url import url
from src.validators.python_identifier import python_identifier
from src.validators.email import email
from src.validators.contains import contains
from src.validators.custom import custom

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
            result.append(validation)

    return {"value": value, "errors": result}


error_codes = err
checker = Checker
