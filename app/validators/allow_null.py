# -*- coding: utf-8 -*-
from app.checker import Checker as checker
from app.error_codes import codes as err


def allow_null(value, options):
    if options == True:
        return

    result = checker.is_defined(value)
    if not result:
        err.get("cant_be_null")
