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


def test_does_not_allows_if_the_value_is_included_in_a_string_and_the_conditional_is_not_allowed():
    samples = [
        ["foo", "foo", err.contains.name],
        ["bar", "bar", err.contains.name],
        ["baz", "baz", err.contains.name],
    ]

    for value in samples:
        options = {"not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[2]: value[1]}]]}


def test_allow_if_the_value_is_included_in_an_array_and_the_conditional_is_allowed():

    samples = [
        ["foo", ["foo", "bar", "baz"]],
        ["bar", ["foo", "bar", "baz"]],
        ["baz", ["baz", "bar", "baz"]],
    ]

    for value in samples:
        options = {"allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_allow_if_the_value_is_not_included_in_an_array_and_the_conditional_is_not_allowed():
    samples = [
        ["lorem", ["foo", "bar", "baz"]],
        ["ipsum", ["foo", "bar", "baz"]],
        ["dolor", ["baz", "bar", "baz"]],
    ]

    for value in samples:
        options = {"not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_does_not_allow_if_the_value_is_not_included_in_an_array_and_the_conditional_is_allowed():
    samples = [
        ["foo", ["x", "y", "z"], err.not_contains.name],
        ["bar", ["a", "b", "c"], err.not_contains.name],
    ]

    for value in samples:
        options = {"allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[2]: value[1]}]]}


def test_does_not_allow_if_the_value_is_included_in_an_array_and_the_conditional_is_not_allowed():
    samples = [
        ["x", ["x", "y", "z"], err.contains.name],
        ["a", ["a", "b", "c"], err.contains.name],
    ]

    for value in samples:
        options = {"not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[2]: value[1]}]]}


def test_allow_if_the_value_is_included_with_option_as_array_and_the_conditional_is_allowed():
    sizes = ["small", "medium", "large"]
    value = "large"

    options = {"allowed": sizes}

    validations = {"contains": options}

    ret = validate(value, validations)

    assert ret == {"value": value, "errors": []}


def test_allow_if_the_value_is_not_included_with_option_as_array_and_the_conditional_is_not_allowed():
    sizes = ["small", "medium", "large"]
    value = "xlarge"

    options = {"not_allowed": sizes}

    validations = {"contains": options}

    ret = validate(value, validations)

    assert ret == {"value": value, "errors": []}


def test_does_not_allow_if_the_value_is_not_included_with_option_as_array_and_the_conditional_is_allowed():
    sizes = ["small", "medium", "large"]
    value = "xlarge"

    options = {"allowed": sizes}

    validations = {"contains": options}

    ret = validate(value, validations)

    assert ret == {"value": value, "errors": [[{err.not_contains.name: sizes}]]}


def test_does_not_allow_if_the_value_is_included_with_option_as_array_and_the_conditional_is_not_allowed():
    sizes = ["small", "medium", "large"]
    value = "large"

    options = {"not_allowed": sizes}

    validations = {"contains": options}

    ret = validate(value, validations)

    assert ret == {"value": value, "errors": [[{err.contains.name: sizes}]]}


def test_does_not_allow_if_the_value_is_included_with_option_as_array_and_the_conditional_is_not_allowed_and_if_the_value_is_not_included_with_option_as_array_and_the_conditional_is_allowed():
    allowed_list = ["small", "medium", "large"]
    not_allowed_list = ["xlarge", "xxlarge", "tiny"]
    value = "xlarge"

    options = {"allowed": allowed_list, "not_allowed": not_allowed_list}

    validations = {"contains": options}

    ret = validate(value, validations)

    assert ret == {
        "value": value,
        "errors": [
            [
                {err.not_contains.name: allowed_list},
                {err.contains.name: not_allowed_list},
            ]
        ],
    }


def test_allow_value_is_included_in_an_object_and_the_conditional_is_allowed():
    samples = [
        ["type", {"type": "Fiat", "model": "500", "color": "white"}],
        [
            "price",
            {"type": "Ford", "model": "Mustang", "color": "black", "price": 8000},
        ],
    ]

    for value in samples:
        options = {"allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_allow_value_if_is_not_included_in_an_object_and_the_conditional_is_not_allowed():
    samples = [
        ["price", {"type": "Fiat", "model": "500", "color": "white"}],
        ["year", {"type": "Ford", "model": "Mustang", "color": "black", "price": 8000}],
    ]

    for value in samples:
        options = {"not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_does_not_allow_value_is_not_included_in_an_object_and_the_conditional_is_allowed():
    samples = [
        ["foo", {"bar": True}, err.not_contains.name],
        ["bar", {"foo": True}, err.not_contains.name],
    ]

    for value in samples:
        options = {"allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[2]: value[1]}]]}


def test_does_not_allow_if_the_value_is_included_in_an_object():
    samples = [
        ["foo", {"foo": True}, err.contains.name],
        ["bar", {"bar": True}, err.contains.name],
    ]

    for value in samples:
        options = {"not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[2]: value[1]}]]}


def test_allow_multiple_validations_with_substring_is_valid_in_a_string_and_the_conditional_is_allowed_and_not_allowed_together():
    samples = [
        ["lorem", "hello", "lorem ipsum"],
        ["bar", "foo", "bar"],
        ["baz", "world", "baz"],
    ]

    for value in samples:
        options = {"allowed": value[2], "not_allowed": value[1]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": []}


def test_does_not_allow_multiple_validations_with_substring_is_invalid_in_a_string_and_the_conditional_is_allowed_and_not_allowed_together():
    samples = [["hello", "hello", "hello world", err.contains.name]]

    for value in samples:
        options = {"allowed": value[1], "not_allowed": value[2]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[3]: value[2]}]]}


def test_does_not_allow_multiple_validations_with_substring_is_valid_in_a_string_and_the_conditional_is_allowed_and_not_allowed_together():
    samples = [["lorem", "hello world", "world", err.not_contains.name]]

    for value in samples:
        options = {"allowed": value[1], "not_allowed": value[2]}
        validations = {"contains": options}
        ret = validate(value[0], validations)

        assert ret == {"value": value[0], "errors": [[{value[3]: value[1]}]]}
