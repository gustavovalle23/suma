# -*- coding: utf-8 -*-
from src.checker import checker


def test_check_for_a_defined_value():
    samples = [
        "",
        " ",
        "text",
        0,
        1,
        False,
        True,
        [],
        [None],
        [1],
        {},
        {"obj": None},
        lambda: {},
    ]

    for value in samples:
        ret = checker.is_defined(value)
        assert ret == True


def test_check_for_not_a_defined_value():
    ret = checker.is_defined(None)
    assert ret == False
