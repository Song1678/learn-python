import pytest

from tests.utils import load

ex = load("stage2_advanced.ex14_dataclasses_typing")


def test_product():
    p = ex.Product("笔", 2.5, 10)
    assert p.total_value == 25
    assert ex.Product("纸", 1.0).quantity == 0
    assert repr(p) == "Product(name='笔', price=2.5, quantity=10)"
    assert p == ex.Product("笔", 2.5, 10)


def test_product_negative_price():
    with pytest.raises(ValueError):
        ex.Product("坏", -1)


def test_inventory_default_not_shared():
    a, b = ex.Inventory(), ex.Inventory()
    a.add(ex.Product("x", 1, 1))
    assert b.products == []


def test_inventory():
    inv = ex.Inventory()
    inv.add(ex.Product("苹果", 5.0, 10))
    inv.add(ex.Product("香蕉", 3.0, 2))
    inv.add(ex.Product("苹果", 5.0, 5))
    assert len(inv.products) == 2
    assert inv.find("苹果").quantity == 15
    assert inv.find("西瓜") is None
    assert inv.total_value() == 5.0 * 15 + 3.0 * 2
    assert inv.low_stock() == ["香蕉"]
    assert inv.low_stock(threshold=100) == sorted(["苹果", "香蕉"])


def test_top_students():
    students = [ex.Student(80, "A"), ex.Student(95, "B"), ex.Student(70, "C"), ex.Student(88, "D")]
    assert ex.top_students(students, 2) == ["B", "D"]


def test_summarize():
    products = [ex.Product("a", 1.0, 3), ex.Product("b", 2.0, 4), ex.Product("c", 2.5)]
    assert ex.summarize(products) == {"count": 3, "total_quantity": 7, "avg_price": 1.83}
    assert ex.summarize([]) == {"count": 0, "total_quantity": 0, "avg_price": 0.0}
