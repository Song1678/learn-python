import pandas as pd
import pytest

from tests.utils import DATA, load

ex = load("stage3_data.ex19_pandas_analysis")


@pytest.fixture
def df():
    data = pd.read_csv(DATA / "sales.csv", parse_dates=["date"])
    data["revenue"] = data["quantity"] * data["unit_price"]
    return data


def test_revenue_by_region(df):
    s = ex.revenue_by_region(df)
    assert isinstance(s, pd.Series)
    assert s.index.tolist() == ["华东", "西南", "华南", "华北"]
    assert s["华东"] == 64789
    assert s.sum() == df["revenue"].sum()


def test_region_summary(df):
    summary = ex.region_summary(df)
    assert summary.index.tolist() == ["华东", "西南", "华南", "华北"]
    assert summary.loc["华东", "orders"] == 14
    assert summary.loc["华东", "quantity"] == 101
    assert summary.loc["华东", "revenue"] == 64789
    assert summary.loc["华东", "avg_order"] == pytest.approx(4627.79)
    assert set(summary.columns) >= {"orders", "quantity", "revenue", "avg_order"}


def test_category_share(df):
    s = ex.category_share(df)
    assert s.index.tolist()[0] == "电子产品"
    assert s["电子产品"] == 91.8
    assert s.sum() == pytest.approx(100, abs=0.2)


def test_monthly_revenue(df):
    s = ex.monthly_revenue(df)
    assert s.index.tolist() == [f"2024-0{m}" for m in range(1, 7)]
    assert s.sum() == df["revenue"].sum()


def test_month_over_month(df):
    s = ex.month_over_month(df)
    assert pd.isna(s.iloc[0])
    assert s["2024-02"] == pytest.approx(0.4044)
    assert s["2024-04"] == pytest.approx(-0.8927)


def test_pivot_region_category(df):
    p = ex.pivot_region_category(df)
    assert set(p.index) == {"华东", "华北", "华南", "西南"}
    assert set(p.columns) == {"电子产品", "生活用品", "图书"}
    assert p.values.sum() == df["revenue"].sum()
    assert not p.isna().any().any()


def test_top_product_by_region(df):
    assert ex.top_product_by_region(df) == {
        "华东": "笔记本电脑", "华北": "无线耳机", "华南": "无线耳机", "西南": "笔记本电脑",
    }


def test_compare_with_targets(df):
    targets = pd.read_csv(DATA / "sales_targets.csv")
    result = ex.compare_with_targets(df, targets)
    assert list(result.columns) == ["region", "revenue", "target", "achievement"]
    assert result["achievement"].is_monotonic_decreasing
    row = result.set_index("region").loc["西南"]
    assert row["achievement"] == round(51587 / 45000, 2)
    assert list(result.index) == list(range(4))
