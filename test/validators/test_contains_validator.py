# -*- coding: utf-8 -*-
from src.suma import validate, error_codes

err = error_codes


def test_does_allow_empty_values():
    samples = [{}, None, ""]

    for value in samples:
        validations = {"contains": {}}
        ret = validate(value, validations)

        assert ret == {"value": value, "errors": []}


def test_allow_if_the_value_is_included_is_an_string_and_the_conditional_is_allowed():
    samples = [["lorem", "lorem ipsum"], ["bar", "bar"], ["baz", "baz"]]

    for value in samples:
        options = {"allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_allow_if_the_value_is_not_included_is_an_string_and_the_conditional_is_not_allowed():
    samples = [["foo", "text"], ["bar", "lorem"], ["baz", "ipsum"]]

    for value in samples:
        options = {"not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_not_allows_if_the_value_is_not_included_is_an_string_and_the_conditional_is_allowed():
    samples = [
        ["foo", "text", err.not_contains.name],
        ["bar", "lorem", err.not_contains.name],
        ["baz", "ipsum", err.not_contains.name],
    ]

    for value in samples:
        options = {"allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[2]: value[1]}]]}
