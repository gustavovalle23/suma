# -*- coding: utf-8 -*-
from src.checker import checker


def test_check_for_a_object_value():
    samples = [
        {},
        dict(),
    ]

    for value in samples:
        ret = checker.is_object(value)
        assert ret == True


def test_check_for_not_a_object_value():
    samples = [
        None,
        1,
        "dict",
    ]

    for value in samples:
        ret = checker.is_object(value)
        assert ret == False
