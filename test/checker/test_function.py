# -*- coding: utf-8 -*-
from src.checker import checker


def test_for_a_function_value():
    def sample_func():
        ...

    samples = [lambda: None, sample_func]

    for value in samples:
        ret = checker.is_function(value)
        assert ret == True


def test_for_not_a_function_value():
    samples = [None, 1, "def"]

    for value in samples:
        ret = checker.is_function(value)
        assert ret == False
