# -*- coding: utf-8 -*-
from src.error_codes import err, HerbsPYException
from src.checker import checker


class DateTimeCheckers:
    class before:
        @staticmethod
        def func(value, param):
            return not checker.is_before_than(value, param)

        @staticmethod
        def err():
            return err.too_late

    class after:
        @staticmethod
        def func(value, param):
            return not checker.is_after_than(value, param)

        @staticmethod
        def err():
            return err.too_early

    class after:
        @staticmethod
        def func(value, param):
            return not checker.is_at(value, param)

        @staticmethod
        def err():
            return err.not_at


def datetime_validator(value, options: dict):
    results = None

    for validator, param in options.items():
        if not checker.is_defined:
            continue

        if validator not in vars(DateTimeCheckers):
            raise HerbsPYException(f'Unknown length validator "{validator}"')

        dt_checker = getattr(DateTimeCheckers, validator)

        if not checker.is_date(value):
            results = results or []
            results.append({[err.not_a_date]: param})
            continue

        result = dt_checker.func(value, param)
        if result:
            results = results or []
            results.append({[dt_checker.err]: param})

    return results
