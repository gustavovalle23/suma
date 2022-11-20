# -*- coding: utf-8 -*-
from app.checker import Checker as checker
from app.error_codes import err


def format(value, expression):
    if checker.is_empty(value):
        return

    result = checker.is_valid_format(value, expression)
    if not result:
        return {err.invalid_format: True}
