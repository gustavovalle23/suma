# -*- coding: utf-8 -*-
from app.checker import checker
from app.error_codes import err


def url(value, options):
    if checker.is_empty(value):
        return None

    result = checker.is_valid_url(value, options)
    result = None if result else {[err.invalid_url]: True}
    return result
