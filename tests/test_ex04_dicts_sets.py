from tests.utils import load

ex = load("stage1_basics.ex04_dicts_sets")


def test_word_count():
    assert ex.word_count("the cat and The dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
    assert ex.word_count("") == {}


def test_invert_dict():
    assert ex.invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_merge_counts():
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    assert ex.merge_counts(a, b) == {"x": 1, "y": 5, "z": 4}
    assert a == {"x": 1, "y": 2} and b == {"y": 3, "z": 4}, "不应修改原字典"


def test_group_by_first_letter():
    words = ["apple", "Banana", "avocado", "blueberry", "cherry"]
    assert ex.group_by_first_letter(words) == {
        "a": ["apple", "avocado"],
        "b": ["Banana", "blueberry"],
        "c": ["cherry"],
    }


def test_common_elements():
    assert ex.common_elements([1, 2, 2, 3, 5], [2, 3, 4, 3]) == [2, 3]
    assert ex.common_elements([1], [2]) == []


def test_get_nested():
    data = {"a": {"b": {"c": 42}}, "x": 1}
    assert ex.get_nested(data, "a.b.c") == 42
    assert ex.get_nested(data, "a.b") == {"c": 42}
    assert ex.get_nested(data, "x") == 1
    assert ex.get_nested(data, "a.x.y", "N/A") == "N/A"
    assert ex.get_nested(data, "x.y") is None


def test_unique_visitors():
    assert ex.unique_visitors(["a", "b"], ["b", "c"], ["b", "a"]) == (3, {"b"})
    assert ex.unique_visitors(["a"], ["b"]) == (2, set())


def test_sort_dict_by_value():
    d = {"a": 1, "b": 3, "c": 2}
    assert ex.sort_dict_by_value(d) == [("b", 3), ("c", 2), ("a", 1)]
    assert ex.sort_dict_by_value(d, reverse=False) == [("a", 1), ("c", 2), ("b", 3)]
