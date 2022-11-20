# -*- coding: utf-8 -*-
from app.checker import Checker as checker
from app.error_codes import err


def presence(value, options):
    if not options:
        return

    result = checker.is_empty(value)
    if not result:
        return {err.cant_be_empty: options}
