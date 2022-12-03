# -*- coding: utf-8 -*-
from datetime import date

from src.checker import checker


def test_check_for_a_date_value():
    example = date(1999, 10, 10)
    ret = checker.is_date(example)
    assert ret == True


def test_check_for_not_a_date_value():
    samples = [None, 1, [1], "Date", "1999/01/01"]

    for value in samples:
        ret = checker.is_date(value)
        assert ret == False
