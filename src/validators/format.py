# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err


def format(value, expression):
    if checker.is_empty(value):
        return

    result = checker.is_valid_format(value, expression)
    if not result:
        return {err.invalid_format.name: True}
