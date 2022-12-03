# -*- coding: utf-8 -*-
from src.checker import checker


def test_check_for_an_array_value():
    samples = [[], [None], [1]]

    for value in samples:
        ret = checker.is_array(value)
        assert ret == True


def test__check_for_not_an_array_value():
    samples = [None, 1, "Array"]

    for value in samples:
        ret = checker.is_array(value)
        assert ret == False
