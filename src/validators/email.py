# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err


def email(value):
    if checker.is_empty(value):
        return None

    result = checker.is_valid_email(value)
    result = None if result else {[err.invalid_email]: True}

    return result
