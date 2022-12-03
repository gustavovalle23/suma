# -*- coding: utf-8 -*-
from src.checker import checker


def test_check_for_a_value_that_contains_in_array_or_string_or_object():
    samples = [
        [["small", "medium", "large"], "large"],
        ["hello world 1", "hello"],
        [[25, 5, 4], 4],
        [{"foo": True}, "foo"],
    ]

    for value in samples:
        ret = checker.contains(value[0], value[1])
        assert ret == True


def test_check_for_a_value_that_not_contains_in_array_or_string_or_object():
    samples = [
        [["small", "medium", "large"], "xlarge"],
        ["hello world 2", "goodbye"],
        ["hello world 3", None],
        [None, "hello world 4"],
        [None, None],
        [[25, 5, 4], 14],
        [{"foo": True}, "bar"],
        [256, 6],
    ]

    for value in samples:
        ret = checker.contains(value[0], value[1])
        assert ret == False
