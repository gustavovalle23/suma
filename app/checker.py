# -*- coding: utf-8 -*-
from collections.abc import Iterable
from numbers import Number
from datetime import date
import re


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

    def is_valid_format(value, expression):
        return bool(re.match(expression, value))
