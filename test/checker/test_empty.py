# -*- coding: utf-8 -*-
from src.checker import checker


def test_for_an_empty_value():
    samples = ["", " ", [], {}]

    for value in samples:
        ret = checker.is_empty(value)
        assert ret == True


def test_for_not_an_empty_value():
    samples = ["text", 0, 1, False, True, [None], [1], {"obj": None}, lambda: None]

    for value in samples:
        ret = checker.is_empty(value)
        assert ret == False
