# -*- coding: utf-8 -*-
from src.checker import checker


def test_check_for_a_regex_value():
    samples = ["([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"]

    for value in samples:
        ret = checker.is_reg_exp(value)
        assert ret == True


def test_check_for_not_a_regex_value():
    samples = [
        None,
        1,
    ]

    for value in samples:
        ret = checker.is_reg_exp(value)
        assert ret == False
