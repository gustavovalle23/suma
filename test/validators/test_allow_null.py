# -*- coding: utf-8 -*-
from src.suma import validate
from src.error_codes import err


def test_does_allow_non_null_values():
    samples = [
        "text",
        0,
        1,
        False,
        True,
        [None],
        [1],
        {"obj": None},
        lambda: None,
        {},
        [],
        "",
        " ",
    ]

    for value in samples:
        validations = {"allow_null": True}
        ret = validate(value, validations)
        assert ret == {"value": value, "errors": []}


def test_does_not_allow_non_null_values():
    samples = [None]

    for value in samples:
        validations = {"allow_null": False}
        ret = validate(value, validations)
        assert ret == {"value": value, "errors": [{err.cant_be_null.name: True}]}


def test_does_allow_non_null_values():
    samples = [
        "text",
        0,
        1,
        False,
        True,
        [None],
        [1],
        {"obj": None},
        lambda: None,
        {},
        [],
        "",
        " ",
    ]

    for value in samples:
        validations = {"allow_null": True}
        ret = validate(value, validations)
        assert ret == {"value": value, "errors": []}


def test_does_allow_null_values():
    samples = [None]

    for value in samples:
        validations = {"allow_null": True}
        ret = validate(value, validations)
        assert ret == {"value": value, "errors": []}
