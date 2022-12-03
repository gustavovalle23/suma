# -*- coding: utf-8 -*-
from app.checker import checker
from app.error_codes import err


def contains(value, options):
    results = None

    if checker.is_empty(value):
        return None

    allowed = options.get("allowed")
    if allowed and not checker.contains(allowed, value):
        results = results or []
        results.append({[err.not_contains]: allowed})

    not_allowed = options.get("not_allowed")
    if not_allowed and checker.contains(not_allowed, value):
        results = results or []
        results.append({[err.contains]: not_allowed})

    return results
