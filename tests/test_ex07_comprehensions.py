from tests.utils import load

ex = load("stage1_basics.ex07_comprehensions")


def test_squares_of_evens():
    assert ex.squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert ex.squares_of_evens([]) == []


def test_word_lengths():
    assert ex.word_lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}


def test_transpose():
    assert ex.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert ex.transpose([[1]]) == [[1]]


def test_flatten_matrix():
    assert ex.flatten_matrix([[1, 2], [3, 4], []]) == [1, 2, 3, 4]


def test_label_numbers():
    assert ex.label_numbers([1, 2, 3]) == ["奇", "偶", "奇"]


def test_filter_by_value():
    assert ex.filter_by_value({"a": 1, "b": 5, "c": 3}, 3) == {"b": 5, "c": 3}


def test_unique_lengths():
    assert ex.unique_lengths(["a", "bb", "cc", "ddd"]) == {1, 2, 3}
    assert ex.unique_lengths([]) == set()


def test_pythagorean_triples():
    assert ex.pythagorean_triples(13) == [(3, 4, 5), (5, 12, 13), (6, 8, 10)]
    assert ex.pythagorean_triples(4) == []


def test_sum_of_squares():
    assert ex.sum_of_squares(3) == 14
    assert ex.sum_of_squares(100) == 338350


def test_has_negative():
    assert ex.has_negative([1, -2, 3]) is True
    assert ex.has_negative([1, 2]) is False
    assert ex.has_negative([]) is False


def test_index_users():
    users = [{"id": 1, "name": "A"}, {"name": "B"}, {"id": 3, "name": "C"}]
    assert ex.index_users(users) == {1: "A", 3: "C"}
