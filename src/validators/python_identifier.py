# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err


def python_identifier(value):
    if checker.is_empty(value):
        return {[err.cant_be_empty]: True}

    result = checker.is_valid_python_identifier(value)
    result = None if result else {[err.invalid_python_identifier]: True}

    return result
