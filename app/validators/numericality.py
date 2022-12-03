# -*- coding: utf-8 -*-
from app.checker import checker
from app.error_codes import err, HerbsPYException


class NumericalityCheckers:
    class greater_than:
        @staticmethod
        def func(value, param):
            return not checker.is_greater_than(value, param)

        @staticmethod
        def err():
            return err.not_greater_than

    class greater_than_or_equal_to:
        @staticmethod
        def func(value, param):
            return not checker.is_greater_than_or_equal_to(value, param)

        @staticmethod
        def err():
            return err.not_greater_than_or_equal_to

    class equal_to:
        @staticmethod
        def func(value, param):
            return not checker.is_equal_to(value, param)

        @staticmethod
        def err():
            return err.not_equal_to

    class less_than:
        @staticmethod
        def func(value, param):
            return not checker.is_less_than(value, param)

        @staticmethod
        def err():
            return err.not_less_than

    class less_than_or_equal_to:
        @staticmethod
        def func(value, param):
            return not checker.is_less_than_or_equal_to(value, param)

        @staticmethod
        def err():
            return err.not_less_than_or_equal_to

    class only_integer:
        @staticmethod
        def func(value, param):
            return param == True and not checker.is_integer(value)

        @staticmethod
        def err():
            return err.not_an_integer


def numericality(value, options: dict):
    results = None

    for validator, param in options.items():
        if not checker.is_defined():
            continue

        if validator not in vars(NumericalityCheckers):
            raise HerbsPYException(f'Unknown numericality validator "{validator}"')

        num_checker = getattr(NumericalityCheckers, validator)

        if not checker.is_number(value):
            results = results or []
            results.append({[err.not_a_number]: param})
            continue

        result = num_checker.func(value, param)
        if result:
            results = results or []
            results.append({[num_checker.err]: param})

    return results
