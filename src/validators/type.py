# -*- coding: utf-8 -*-
from datetime import date

from src.checker import checker
from src.error_codes import err

type_checkers = {
    str: checker.is_string,
    bool: checker.is_boolean,
    int: checker.is_number,
    float: checker.is_number,
    object: checker.is_object,
    date: checker.is_date,
    list: checker.is_array,
}


def type_validator(value, type):
    def find_type_checker(type):
        type_checker = type_checkers.get(type)
        if type_checker == None:
            type_checker = checker.is_instance_of
        return type_checker

    if not checker.is_defined(value):
        return None

    result, type_name = None, None

    if checker.is_array_with_type(type):
        type_checker = checker.is_array_with_type_valid
        inner_type = type[0]
        type_name = [inner_type.__name__]
        result = type_checker(value, find_type_checker(inner_type), inner_type)
    else:
        type_checker = find_type_checker(type)
        result = type_checker(value, type)

    if result:
        return {[err.wrong_type]: type_name}
