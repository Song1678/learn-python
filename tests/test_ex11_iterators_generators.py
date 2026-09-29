import types
from itertools import islice

from tests.utils import load

ex = load("stage2_advanced.ex11_iterators_generators")


def test_countdown():
    gen = ex.countdown(3)
    assert isinstance(gen, types.GeneratorType), "请使用 yield 实现"
    assert list(gen) == [3, 2, 1]
    assert list(ex.countdown(0)) == []


def test_fibonacci():
    gen = ex.fibonacci()
    assert isinstance(gen, types.GeneratorType)
    assert list(islice(gen, 10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_take():
    assert ex.take(range(10), 3) == [0, 1, 2]
    assert ex.take(iter([1, 2, 3]), 0) == []
    assert ex.take(iter([1, 2]), 5) == [1, 2]

    def naturals():
        n = 0
        while True:
            yield n
            n += 1

    assert ex.take(naturals(), 4) == [0, 1, 2, 3]


def test_chunked():
    assert isinstance(ex.chunked([], 2), types.GeneratorType)
    assert list(ex.chunked(range(5), 2)) == [[0, 1], [2, 3], [4]]
    assert list(ex.chunked("abcdef", 3)) == [["a", "b", "c"], ["d", "e", "f"]]
    assert list(ex.chunked([], 3)) == []


def test_running_total():
    assert list(ex.running_total([1, 2, 3, 4])) == [1, 3, 6, 10]


def test_flatten_deep():
    assert list(ex.flatten_deep([1, [2, [3, [4]]], 5])) == [1, 2, 3, 4, 5]
    assert list(ex.flatten_deep([[], [[]]])) == []


def test_grep_lines_is_lazy():
    consumed = []

    def lines():
        for line in ["ERROR a\n", "INFO b\n", "ERROR c\n", "INFO d\n"]:
            consumed.append(line)
            yield line

    gen = ex.grep_lines(lines(), "ERROR")
    assert next(gen) == "ERROR a"
    assert len(consumed) == 1, "应该是惰性的：只读取需要的行"
    assert list(gen) == ["ERROR c"]


def test_my_range():
    assert list(ex.MyRange(0, 10, 3)) == [0, 3, 6, 9]
    assert list(ex.MyRange(2, 5)) == [2, 3, 4]
    assert list(ex.MyRange(5, 5)) == []
    r = ex.MyRange(0, 2)
    assert iter(r) is r
    assert next(r) == 0
