# -*- coding: utf-8 -*-
from src.checker import checker


def test_check_for_a_iterable_value():
    samples = [
        [{"name": "jhon", "age": 35}, {"name": "marie", "age": 29}],
        ["a", "b", "c"],
    ]

    for value in samples:
        ret = checker.is_iterable(value)
        assert ret == True


def test_check_for_not_a_iterable_value():
    class A:
        ...

    def b():
        ...

    samples = [None, 1, A, b]

    for value in samples:
        ret = checker.is_iterable(value)
        assert ret == False
