# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err


def contains(value, options):
    results = None

    if checker.is_empty(value):
        return None

    allowed = options.get("allowed")
    if allowed and not checker.contains(allowed, value):
        results = results or []
        results.append({err.not_contains.name: allowed})

    not_allowed = options.get("not_allowed")
    if not_allowed and checker.contains(not_allowed, value):
        results = results or []
        results.append({err.contains.name: not_allowed})

    return results
