import math

import pytest

from tests.utils import load

ex = load("stage2_advanced.ex08_classes")


class TestBankAccount:
    def test_init(self):
        assert ex.BankAccount("Tom").balance == 0
        assert ex.BankAccount("Tom", 100).balance == 100
        assert ex.BankAccount("Tom").owner == "Tom"

    def test_deposit_withdraw(self):
        acc = ex.BankAccount("Tom")
        acc.deposit(100)
        acc.withdraw(20)
        assert acc.balance == 80
        assert acc.history == [("deposit", 100), ("withdraw", 20)]

    def test_invalid_operations(self):
        acc = ex.BankAccount("Tom", 50)
        with pytest.raises(ValueError):
            acc.deposit(0)
        with pytest.raises(ValueError):
            acc.withdraw(-5)
        with pytest.raises(ValueError):
            acc.withdraw(51)
        assert acc.balance == 50
        assert acc.history == []

    def test_balance_read_only(self):
        acc = ex.BankAccount("Tom")
        with pytest.raises(AttributeError):
            acc.balance = 1000

    def test_str(self):
        acc = ex.BankAccount("Tom", 80)
        assert str(acc) == "Tom 的账户，余额 80.00 元"


class TestVector:
    def test_repr_eq(self):
        assert repr(ex.Vector(1, 2)) == "Vector(1, 2)"
        assert ex.Vector(1, 2) == ex.Vector(1, 2)
        assert ex.Vector(1, 2) != ex.Vector(2, 1)
        assert ex.Vector(1, 2) != (1, 2)

    def test_operators(self):
        assert ex.Vector(1, 2) + ex.Vector(3, 4) == ex.Vector(4, 6)
        assert ex.Vector(5, 5) - ex.Vector(1, 2) == ex.Vector(4, 3)
        assert ex.Vector(1, 2) * 3 == ex.Vector(3, 6)
        assert abs(ex.Vector(3, 4)) == 5.0

    def test_unpack(self):
        x, y = ex.Vector(7, 8)
        assert (x, y) == (7, 8)


class TestShapes:
    def test_areas(self):
        assert ex.Rectangle(2, 3).area() == 6
        assert ex.Circle(1).area() == pytest.approx(math.pi)
        assert ex.Square(4).area() == 16

    def test_inheritance(self):
        sq = ex.Square(2)
        assert isinstance(sq, ex.Rectangle) and isinstance(sq, ex.Shape)
        assert sq.width == sq.height == 2

    def test_name_and_describe(self):
        assert ex.Rectangle(2, 3).name == "Rectangle"
        assert ex.Square(1).name == "Square"
        assert ex.Rectangle(2, 3).describe() == "Rectangle，面积 6.00"
        assert ex.Circle(1).describe() == "Circle，面积 3.14"

    def test_total_area(self):
        shapes = [ex.Rectangle(2, 3), ex.Square(2), ex.Circle(1)]
        assert ex.total_area(shapes) == pytest.approx(10 + math.pi)


class TestStack:
    def test_push_pop(self):
        s = ex.Stack()
        s.push(1)
        s.push(2)
        assert s.peek() == 2
        assert len(s) == 2
        assert s.pop() == 2
        assert s.pop() == 1
        assert len(s) == 0

    def test_empty(self):
        s = ex.Stack()
        assert not s
        with pytest.raises(IndexError, match="stack is empty"):
            s.pop()
        with pytest.raises(IndexError):
            s.peek()
        s.push("x")
        assert s

    def test_from_list(self):
        s = ex.Stack.from_list([1, 2, 3])
        assert isinstance(s, ex.Stack)
        assert s.pop() == 3
        assert len(s) == 2
