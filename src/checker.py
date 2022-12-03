# -*- coding: utf-8 -*-
import re
from datetime import date
from numbers import Number
from keyword import kwlist
from collections.abc import Iterable

from src.error_codes import HerbsPYException


MUST_BE_A_DATE = "Invalid value. It must be a date."


class Checker:
    @staticmethod
    def is_function(value):
        return callable(value)

    @staticmethod
    def is_defined(value):
        return value is not None

    @staticmethod
    def is_array(value):
        return isinstance(value, list)

    @staticmethod
    def is_array_with_type(value):
        return isinstance(value, list) and len(value) == 1 and callable(value[0])

    @staticmethod
    def is_iterable(value):
        return isinstance(value, Iterable)

    @staticmethod
    def is_array_with_type_valid(value, type_checker, type):
        return all([type_checker(item, type) for item in value])

    @staticmethod
    def is_string(value):
        return isinstance(value, str)

    @staticmethod
    def is_boolean(value):
        return value == True or value == False

    @staticmethod
    def is_number(value):
        return isinstance(value, Number)

    @staticmethod
    def is_date(obj):
        return isinstance(obj, date)

    @staticmethod
    def is_instance_of(obj, type):
        return isinstance(obj, type)

    @staticmethod
    def is_object(value):
        return isinstance(value, object)

    @staticmethod
    def is_empty(value):
        if not Checker.is_defined(value):
            return True

        if Checker.is_function(value):
            return False

        if Checker.is_string(value):
            return bool(re.match(r"^(?![\s\S])", value))

        if Checker.is_array(value):
            return len(value) == 0

        if Checker.is_date(value):
            return False

        if Checker.is_object(value):
            return len(vars(value)) > 0

        return False

    @staticmethod
    def is_valid_format(value, expression):
        return bool(re.match(expression, value))

    @staticmethod
    def is_valid_email(value):
        if not Checker.is_string(value):
            return False

        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        return bool(re.search(regex, value))

    @staticmethod
    def is_valid_url(value, options: dict):
        if not Checker.is_string(value):
            return False

        regex = re.compile(
            r"^https?://"  # http:// or https://
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domain...
            r"localhost|"  # localhost...
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
            r"(?::\d+)?"  # optional port
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )
        return value is not None and regex.search(value)

    @staticmethod
    def is_valid_python_identifier(value):
        valid_name = r"/^[$A-Z_][0-9A-Z_$]*$/i"
        return bool(re.match(valid_name, value)) and value not in kwlist

    @staticmethod
    def is_too_short(value, minimum):
        if not Checker.is_number(minimum):
            raise HerbsPYException("Invalid minimum length. It must be a number.")
        return len(value) < minimum

    @staticmethod
    def is_too_long(value, maximum):
        if not Checker.is_number(maximum):
            raise HerbsPYException("Invalid maximum length. It must be a number.")
        return len(value) > maximum

    @staticmethod
    def is_wrong_length(value, expected_length):
        if not Checker.is_number(expected_length):
            raise HerbsPYException("Invalid length. It must be a number.")
        return len(value) != expected_length

    @staticmethod
    def is_equal_to(left, right):
        if not Checker.is_number(right):
            raise HerbsPYException('Invalid "Equal To". It must be a number.')
        return left == right

    @staticmethod
    def is_greater_than(left, right):
        if not Checker.is_number(right):
            raise HerbsPYException('Invalid "Greater Than". It must be a number.')
        return left > right

    @staticmethod
    def is_greater_than_or_equal_to(left, right):
        if not Checker.is_number(right):
            raise HerbsPYException(
                'Invalid "Greater Than Or Equal To". It must be a number.'
            )
        return left >= right

    @staticmethod
    def is_less_than(left, right):
        if not Checker.is_number(right):
            raise HerbsPYException('Invalid "Less Than". It must be a number.')
        return left < right

    @staticmethod
    def is_less_than_or_equal_to(left, right):
        if not Checker.is_number(right):
            raise HerbsPYException(
                'Invalid "Less Than Or Equal To". It must be a number.'
            )
        return left <= right

    @staticmethod
    def is_integer(value):
        return Checker.is_number(value) and value % 1 == 0

    @staticmethod
    def is_before_than(value, param):
        if not Checker.is_date(value):
            raise HerbsPYException(MUST_BE_A_DATE)
        return value < param

    @staticmethod
    def is_after_than(value, param):
        if not Checker.is_date(value):
            raise HerbsPYException(MUST_BE_A_DATE)
        return value > param

    @staticmethod
    def is_at(value: date, param: date):
        if not Checker.is_date(value):
            raise HerbsPYException(MUST_BE_A_DATE)
        return value == param

    @staticmethod
    def contains(object, value):
        if not Checker.is_defined(object):
            return False

        if Checker.is_array(object):
            return value in object

        if Checker.is_string(object):
            return str(value) in object

        if Checker.is_object(object):
            return value in vars(object).keys()

        return False


checker = Checker
