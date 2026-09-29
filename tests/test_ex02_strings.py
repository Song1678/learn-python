import pytest

from tests.utils import load

ex = load("stage1_basics.ex02_strings")


def test_greet():
    assert ex.greet("小明", 18) == "你好，小明！明年你就 19 岁了。"


def test_reverse_string():
    assert ex.reverse_string("abc") == "cba"
    assert ex.reverse_string("") == ""
    assert ex.reverse_string("上海自来水") == "水来自海上"


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("No 'x' in Nixon", True),
])
def test_is_palindrome(s, expected):
    assert ex.is_palindrome(s) is expected


def test_count_vowels():
    assert ex.count_vowels("Hello World") == 3
    assert ex.count_vowels("AEIOU aeiou") == 10
    assert ex.count_vowels("rhythm") == 0


def test_mask_phone():
    assert ex.mask_phone("13812345678") == "138****5678"


def test_format_price():
    assert ex.format_price(1234.5) == "¥1,234.50"
    assert ex.format_price(0) == "¥0.00"
    assert ex.format_price(1000000) == "¥1,000,000.00"


def test_split_and_strip():
    assert ex.split_and_strip(" apple, banana ,, cherry ") == ["apple", "banana", "cherry"]
    assert ex.split_and_strip("") == []


def test_to_snake_case():
    assert ex.to_snake_case("getUserName") == "get_user_name"
    assert ex.to_snake_case("UserName") == "user_name"
    assert ex.to_snake_case("id") == "id"


def test_center_title():
    assert ex.center_title("Menu", 10) == "===Menu==="
    assert ex.center_title("Hi", 6, "*") == "**Hi**"
    assert len(ex.center_title("Title")) == 20
