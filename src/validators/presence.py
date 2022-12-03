# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err


def presence(value, options):
    if not options:
        return

    result = checker.is_empty(value)
    if not result:
        return {err.cant_be_empty.name: options}
