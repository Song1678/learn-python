import pytest

from tests.utils import load

ex = load("stage1_basics.ex01_basics")


def test_celsius_to_fahrenheit():
    assert ex.celsius_to_fahrenheit(100) == 212
    assert ex.celsius_to_fahrenheit(0) == 32
    assert ex.celsius_to_fahrenheit(-40) == -40
    assert isinstance(ex.celsius_to_fahrenheit(10), float)


def test_divide_with_remainder():
    assert ex.divide_with_remainder(17, 5) == (3, 2)
    assert ex.divide_with_remainder(10, 2) == (5, 0)
    assert ex.divide_with_remainder(-7, 2) == (-4, 1)  # Python 向下取整，JS 的 % 结果不同


@pytest.mark.parametrize("value, expected", [
    (1, "int"), (1.5, "float"), ("s", "str"), (True, "bool"),
    (None, "NoneType"), ([1], "list"), ({"a": 1}, "dict"), ((1,), "tuple"), ({1}, "set"),
])
def test_describe_type(value, expected):
    assert ex.describe_type(value) == expected


@pytest.mark.parametrize("value, expected", [
    ([], False), ({}, False), ("", False), (0, False), (None, False), (0.0, False),
    ([0], True), ("0", True), (" ", True), (-1, True), ("False", True),
])
def test_is_truthy(value, expected):
    assert ex.is_truthy(value) is expected


def test_safe_int():
    assert ex.safe_int("42") == 42
    assert ex.safe_int("-7") == -7
    assert ex.safe_int("abc") == 0
    assert ex.safe_int("12abc", -1) == -1
    assert ex.safe_int("3.5", default=None) is None


def test_swap():
    assert ex.swap(1, 2) == (2, 1)
    assert ex.swap("a", [1]) == ([1], "a")


def test_bmi():
    assert ex.bmi(70, 1.75) == 22.9
    assert ex.bmi(50, 1.6) == 19.5


def test_is_valid_age():
    assert ex.is_valid_age(0) is True
    assert ex.is_valid_age(150) is True
    assert ex.is_valid_age(151) is False
    assert ex.is_valid_age(-1) is False
    assert ex.is_valid_age("18") is False
    assert ex.is_valid_age(18.0) is False
