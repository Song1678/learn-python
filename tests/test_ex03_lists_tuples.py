from tests.utils import load

ex = load("stage1_basics.ex03_lists_tuples")


def test_second_largest():
    assert ex.second_largest([3, 1, 4, 4, 2]) == 3
    assert ex.second_largest([5, 5]) is None
    assert ex.second_largest([1]) is None
    assert ex.second_largest([-1, -5, -3]) == -3


def test_chunk():
    assert ex.chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert ex.chunk([1, 2, 3], 3) == [[1, 2, 3]]
    assert ex.chunk([], 2) == []


def test_flatten():
    assert ex.flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert ex.flatten([]) == []


def test_rotate():
    assert ex.rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert ex.rotate([1, 2, 3], 0) == [1, 2, 3]
    assert ex.rotate([1, 2, 3], 4) == [3, 1, 2]
    assert ex.rotate([], 3) == []
    original = [1, 2, 3]
    ex.rotate(original, 1)
    assert original == [1, 2, 3], "不应修改原列表"


def test_dedupe():
    assert ex.dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert ex.dedupe(["a", "b", "a"]) == ["a", "b"]


def test_min_max():
    assert ex.min_max([3, 9, 1]) == (1, 9)
    assert ex.min_max([7]) == (7, 7)


def test_merge_sorted():
    assert ex.merge_sorted([1, 4, 7], [2, 3, 8]) == [1, 2, 3, 4, 7, 8]
    assert ex.merge_sorted([], [1, 2]) == [1, 2]
    assert ex.merge_sorted([1, 1], [1]) == [1, 1, 1]


def test_sort_people():
    people = [("Tom", 20), ("Amy", 25), ("Bob", 20)]
    assert ex.sort_people(people) == [("Bob", 20), ("Tom", 20), ("Amy", 25)]
    assert people == [("Tom", 20), ("Amy", 25), ("Bob", 20)], "不应修改原列表"


def test_head_and_tail():
    assert ex.head_and_tail([1, 2, 3]) == (1, [2, 3])
    assert ex.head_and_tail(["x"]) == ("x", [])
