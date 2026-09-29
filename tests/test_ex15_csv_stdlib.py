import csv

import pytest

from tests.utils import DATA, load

ex = load("stage3_data.ex15_csv_stdlib")
SALES = DATA / "sales.csv"


@pytest.fixture(scope="module")
def raw_rows():
    with open(SALES, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


@pytest.fixture(scope="module")
def rows():
    return ex.read_sales(SALES)


def rev(r):
    return int(r["quantity"]) * float(r["unit_price"])


def test_read_sales(rows, raw_rows):
    assert len(rows) == len(raw_rows) == 48
    first = rows[0]
    assert first["order_id"] == 1003
    assert first["region"] == "华东"
    assert isinstance(first["quantity"], int)
    assert isinstance(first["unit_price"], float)
    assert set(first) == {"order_id", "date", "region", "product", "category", "quantity", "unit_price"}


def test_total_revenue(rows, raw_rows):
    assert ex.total_revenue(rows) == pytest.approx(sum(rev(r) for r in raw_rows))
    assert ex.total_revenue([]) == 0


def test_revenue_by_region(rows, raw_rows):
    result = ex.revenue_by_region(rows)
    assert set(result) == {"华东", "华北", "华南", "西南"}
    assert result["华东"] == pytest.approx(sum(rev(r) for r in raw_rows if r["region"] == "华东"))
    assert type(result) is dict


def test_top_products(rows):
    top = ex.top_products(rows, 3)
    assert len(top) == 3
    assert top[0][0] == "笔记本电脑"
    assert top[0][1] >= top[1][1] >= top[2][1]
    assert len(ex.top_products(rows, 100)) == 8


def test_monthly_revenue(rows, raw_rows):
    result = ex.monthly_revenue(rows)
    assert list(result) == ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06"]
    assert result["2024-03"] == pytest.approx(sum(rev(r) for r in raw_rows if r["date"].startswith("2024-03")))


def test_write_region_report(tmp_path, rows):
    out = tmp_path / "report.csv"
    ex.write_region_report(out, rows)
    with open(out, encoding="utf-8", newline="") as f:
        report = list(csv.DictReader(f))
    assert [r["region"] for r in report] == ["华东", "西南", "华南", "华北"]
    assert report[0] == {"region": "华东", "orders": "14", "revenue": "64789.00"}
    assert sum(int(r["orders"]) for r in report) == 48
