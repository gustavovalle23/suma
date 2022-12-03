# -*- coding: utf-8 -*-
from datetime import date

from src.checker import checker


def test_check_for_a_string_value():
    samples = ["", " ", "a"]

    for value in samples:
        ret = checker.is_string(value)
        assert ret == True


def test_check_for_not_a_string_value():
    samples = [None, 1, [1], date(1990, 1, 1)]

    for value in samples:
        ret = checker.is_reg_exp(value)
        assert ret == False
