# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err


def url(value, options):
    if checker.is_empty(value):
        return None

    result = checker.is_valid_url(value, options)
    result = None if result else {[err.invalid_url]: True}
    return result
