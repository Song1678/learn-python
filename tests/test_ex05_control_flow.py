import pytest

from tests.utils import load

ex = load("stage1_basics.ex05_control_flow")


def test_fizzbuzz():
    result = ex.fizzbuzz(15)
    assert result[:5] == ["1", "2", "Fizz", "4", "Buzz"]
    assert result[14] == "FizzBuzz"
    assert len(result) == 15


@pytest.mark.parametrize("score, expected", [
    (100, "A"), (90, "A"), (89, "B"), (80, "B"), (75, "C"), (60, "D"), (59, "F"), (0, "F"),
])
def test_grade(score, expected):
    assert ex.grade(score) == expected


def test_grade_invalid():
    with pytest.raises(ValueError):
        ex.grade(101)
    with pytest.raises(ValueError):
        ex.grade(-1)


def test_first_negative_index():
    assert ex.first_negative_index([3, 5, -1, -4]) == 2
    assert ex.first_negative_index([1, 2]) == -1
    assert ex.first_negative_index([]) == -1


def test_is_prime():
    primes = [n for n in range(30) if ex.is_prime(n)]
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert ex.is_prime(7919)


def test_collatz_steps():
    assert ex.collatz_steps(1) == 0
    assert ex.collatz_steps(6) == 8
    assert ex.collatz_steps(27) == 111


def test_multiplication_table():
    assert ex.multiplication_table(3) == ["1x1=1", "1x2=2 2x2=4", "1x3=3 2x3=6 3x3=9"]
    assert ex.multiplication_table(9)[-1].endswith("9x9=81")


def test_dot_product():
    assert ex.dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert ex.dot_product([], []) == 0


@pytest.mark.parametrize("code, expected", [
    (200, "OK"), (301, "Redirect"), (302, "Redirect"), (404, "Not Found"),
    (500, "Server Error"), (503, "Server Error"), (418, "Unknown"), (600, "Unknown"),
])
def test_http_status_text(code, expected):
    assert ex.http_status_text(code) == expected


@pytest.mark.parametrize("command, expected", [
    (["go", "北"], "向北移动"),
    (["pick", "钥匙"], "捡起钥匙"),
    (["drop", "剑", "盾"], "丢下2件物品"),
    (["drop"], "丢下0件物品"),
    (["quit"], "再见"),
    (["dance", "now"], "未知命令"),
    ([], "未知命令"),
])
def test_handle_command(command, expected):
    assert ex.handle_command(command) == expected
