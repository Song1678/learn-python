from tests.utils import load

ex = load("stage1_basics.ex06_functions")


def test_make_greeting():
    assert ex.make_greeting("小红") == "你好，小红！"
    assert ex.make_greeting("Tom", greeting="Hi", punctuation="?") == "Hi，Tom?"
    assert ex.make_greeting("Tom", punctuation=".") == "你好，Tom."


def test_average():
    assert ex.average(1, 2, 3, 4) == 2.5
    assert ex.average(5) == 5
    assert ex.average() == 0.0
    assert ex.average(*[2, 4]) == 3


def test_build_profile():
    assert ex.build_profile("Tom", age=20, city="北京") == {"name": "Tom", "age": 20, "city": "北京"}
    assert ex.build_profile("Amy") == {"name": "Amy"}


def test_apply_n_times():
    assert ex.apply_n_times(lambda v: v * 2, 3, 1) == 8
    assert ex.apply_n_times(str.upper, 1, "a") == "A"
    assert ex.apply_n_times(lambda v: v + 1, 0, 10) == 10


def test_compose():
    inc = lambda x: x + 1  # noqa: E731
    dbl = lambda x: x * 2  # noqa: E731
    assert ex.compose(inc, dbl)(5) == 11
    assert ex.compose(dbl, inc)(5) == 12
    assert ex.compose()(7) == 7


def test_make_counter():
    c1 = ex.make_counter()
    c2 = ex.make_counter(10)
    assert [c1(), c1(), c1()] == [1, 2, 3]
    assert c2() == 11
    assert c1() == 4, "两个计数器应该互不影响"


def test_sort_by_length():
    assert ex.sort_by_length(["pear", "fig", "apple", "kiwi"]) == ["fig", "kiwi", "pear", "apple"]


def test_append_item():
    assert ex.append_item(1) == [1]
    assert ex.append_item(2) == [2], "默认参数被共享了！"
    existing = [0]
    assert ex.append_item(1, existing) == [0, 1]
    assert existing == [0, 1]


def test_format_record():
    assert ex.format_record("id") == "id: ?"
    assert ex.format_record("id", sep="=") == "id=?"
    assert ex.format_record("id", upper=True) == "ID: ?"
    import pytest
    with pytest.raises(TypeError):
        ex.format_record("id", "=")  # 仅限关键字参数不能按位置传
