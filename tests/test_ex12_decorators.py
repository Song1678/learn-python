import pytest

from tests.utils import load

ex = load("stage2_advanced.ex12_decorators")


def test_make_multiplier():
    double, triple = ex.make_multiplier(2), ex.make_multiplier(3)
    assert double(5) == 10
    assert triple(5) == 15


def test_count_calls():
    @ex.count_calls
    def greet(name):
        """打招呼"""
        return f"hi {name}"

    assert greet.calls == 0
    assert greet("a") == "hi a"
    greet("b")
    assert greet.calls == 2
    assert greet.__name__ == "greet", "请使用 functools.wraps"
    assert greet.__doc__ == "打招呼"


def test_memoize():
    calls = []

    @ex.memoize
    def slow_square(n):
        calls.append(n)
        return n * n

    assert slow_square(4) == 16
    assert slow_square(4) == 16
    assert slow_square(5) == 25
    assert calls == [4, 5]
    assert slow_square.cache == {(4,): 16, (5,): 25}


def test_memoize_fib_is_fast():
    @ex.memoize
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    assert fib(80) == 23416728348467685


def test_repeat():
    counter = []

    @ex.repeat(3)
    def tick(x):
        counter.append(x)
        return len(counter)

    assert tick("a") == [1, 2, 3]
    assert tick.__name__ == "tick"


def test_validate_positive():
    @ex.validate_positive
    def area(w, h=1):
        return w * h

    assert area(2, 3) == 6
    assert area(2, h=0) == 0
    with pytest.raises(ValueError):
        area(-1, 2)
    with pytest.raises(ValueError):
        area(1, h=-0.5)


def test_log_calls():
    logs = []

    @ex.log_calls(logs)
    def add(a, b=0):
        return a + b

    @ex.log_calls(logs)
    def shout(s):
        return s.upper()

    assert add(1, b=2) == 3
    add(5)
    shout("hi")
    assert logs == ["add(1, b=2) -> 3", "add(5) -> 5", "shout('hi') -> 'HI'"]
    assert shout.__name__ == "shout"
