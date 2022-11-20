# -*- coding: utf-8 -*-
import re
from datetime import date
from numbers import Number
from keyword import kwlist
from collections.abc import Iterable


class Checker:
    @staticmethod
    def is_function(value):
        return callable(value)

    @staticmethod
    def is_defined(value):
        return value != None

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
            return len(vars(value) > 0)

        return False

    @staticmethod
    def is_valid_format(value, expression):
        return bool(re.match(expression, value))

    def is_valid_email(value):
        if not Checker.is_string(value):
            return False

        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        return bool(re.search(regex, value))

    # @staticmethod
    # def is_valid_url(value, options: dict):
    #     if not Checker.is_string(value):
    #         return False

    #     schemes = options.get('schemes', ['http', 'https'])
    #     allow_data_url = options.get('allow_data_url', False)
    #     allow_local = options.get('allow_local', False)

    #     url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

    @staticmethod
    def is_valid_python_identifier(value):
        valid_name = r"/^[$A-Z_][0-9A-Z_$]*$/i"
        return bool(re.match(valid_name, value)) and value not in kwlist

    @staticmethod
    def is_too_short(value, minimum):
        if not Checker.is_number(minimum):
            raise Exception("Invalid minimum length. It must be a number.")
        return len(value) < minimum

    @staticmethod
    def is_too_long(value, maximum):
        if not Checker.is_number(maximum):
            raise Exception("Invalid maximum length. It must be a number.")
        return len(value) > maximum

    @staticmethod
    def is_wrong_length(value, expected_length):
        if not Checker.is_number(expected_length):
            raise Exception("Invalid length. It must be a number.")
        return len(value) != expected_length

    @staticmethod
    def is_equal_to(left, right):
        if not Checker.is_number(right):
            raise Exception('Invalid "Equal To". It must be a number.')
        return left == right

    @staticmethod
    def is_greater_than(left, right):
        if not Checker.is_number(right):
            raise Exception('Invalid "Greater Than". It must be a number.')
        return left > right

    @staticmethod
    def is_greater_than_or_equal_to(left, right):
        if not Checker.is_number(right):
            raise Exception('Invalid "Greater Than Or Equal To". It must be a number.')
        return left >= right

    @staticmethod
    def is_less_than(left, right):
        if not Checker.is_number(right):
            raise Exception('Invalid "Less Than". It must be a number.')
        return left < right

    @staticmethod
    def is_less_than_or_equal_to(left, right):
        if not Checker.is_number(right):
            raise Exception('Invalid "Less Than Or Equal To". It must be a number.')
        return left <= right

    @staticmethod
    def is_integer(value):
        return Checker.is_number(value) and value % 1 == 0

    @staticmethod
    def is_before_than(value, param):
        if not Checker.is_date(value):
            raise Exception("Invalid value. It must be a date.")
        return value < param

    @staticmethod
    def isAfterThan(value, param):
        if not Checker.is_date(value):
            raise Exception("Invalid value. It must be a date.")
        return value > param

    @staticmethod
    def isAt(value: date, param: date):
        if not Checker.is_date(value):
            raise Exception("Invalid value. It must be a date.")
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