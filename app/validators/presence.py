# -*- coding: utf-8 -*-
from app.checker import Checker as checker
from app.error_codes import codes as err


def presence(value, options):
    if not options:
        return

    result = checker.is_empty(value)
    if not result:
        err.get("cant_be_empty")
