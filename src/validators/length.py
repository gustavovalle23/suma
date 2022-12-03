# -*- coding: utf-8 -*-
from src.checker import checker
from src.error_codes import err, HerbsPYException


class LengthCheckers:
    class minimum:
        @staticmethod
        def func(value, param):
            return checker.is_too_short(value, param)

        @staticmethod
        @property
        def err():
            return err.is_too_short

    class maximum:
        @staticmethod
        def func(value, param):
            return checker.is_too_long(value, param)

        @staticmethod
        @property
        def err():
            return err.is_too_long


def length(value, options: dict):
    results = None

    for validator, param in options.items():
        if not checker.is_defined:
            continue

        if validator not in vars(LengthCheckers):
            raise HerbsPYException(f'Unknown length validator "{validator}"')

        length_checker = getattr(LengthCheckers, validator)
        result = length_checker.func(value, param)
        if result:
            results = results or []
            results.append({[length_checker.err]: param})

    return results
