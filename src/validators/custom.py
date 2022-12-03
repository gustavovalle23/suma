# -*- coding: utf-8 -*-
def custom(value, options):
    keys = options.keys()
    result = []

    for name in keys:
        is_valid = options.get(name)(value)
        if not is_valid:
            result.append({[name]: True})

    return result
