# -*- coding: utf-8 -*-
from app.checker import checker
from app.error_codes import err


def allow_null(value, options):
    if options == True:
        return

    result = checker.is_defined(value)
    if not result:
        return {err.cant_be_null.name: True}
