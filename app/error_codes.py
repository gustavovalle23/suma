# -*- coding: utf-8 -*-
from enum import Enum


class Err(Enum):
    cant_be_null = "cant_be_null"
    cant_be_empty = "cant_be_empty"
    wrong_type = "wrong_type"
    is_too_short = "is_too_short"
    is_too_long = "is_too_long"
    wrong_length = "wrong_length"
    not_greater_than = "not_greater_than"
    not_greater_than_or_equal_to = "not_greater_than_or_equal_to"
    not_equal_to = "not_equal_to"
    not_less_than = "not_less_than"
    not_less_than_or_equal_to = "not_less_than_or_equal_to"
    not_an_integer = "not_an_integer"
    not_a_number = "not_a_number"
    too_early = "too_early"
    too_late = "too_late"
    not_at = "not_at"
    not_a_date = "not_a_date"
    invalid_format = "invalid_format"
    not_contains = "not_contains"
    contains = "contains"
    invalid_url = "invalid_url"
    invalid_email = "invalid_email"
    invalid_python_identifier = "invalid_python_identifier"


err = Err()
