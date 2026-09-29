import pandas as pd
import pytest

from tests.utils import DATA, load

ex = load("stage3_data.ex17_pandas_basics")


@pytest.fixture
def df():
    data = pd.read_csv(DATA / "sales.csv", parse_dates=["date"])
    data["revenue"] = data["quantity"] * data["unit_price"]
    return data


def test_load_sales(df):
    loaded = ex.load_sales(DATA / "sales.csv")
    assert isinstance(loaded, pd.DataFrame)
    assert pd.api.types.is_datetime64_any_dtype(loaded["date"]), "date 列需要解析成日期"
    assert "revenue" in loaded.columns
    pd.testing.assert_series_equal(loaded["revenue"], df["revenue"], check_dtype=False)


def test_basic_info(df):
    info = ex.basic_info(df)
    assert info["rows"] == 48
    assert info["columns"] == list(df.columns)
    assert info["regions"] == sorted(["华东", "华北", "华南", "西南"])


def test_filter_by_region(df):
    result = ex.filter_by_region(df, "华北")
    assert len(result) == 7
    assert (result["region"] == "华北").all()


def test_big_orders(df):
    result = ex.big_orders(df, 10000)
    assert len(result) > 0
    assert (result["revenue"] >= 10000).all()
    assert result["revenue"].is_monotonic_decreasing
    assert list(result.index) == list(range(len(result)))


def test_electronics_in_region(df):
    result = ex.electronics_in_region(df, "华南", 5)
    expected = df[(df.region == "华南") & (df.category == "电子产品") & (df.quantity >= 5)]
    assert result["order_id"].tolist() == expected["order_id"].tolist()
    assert len(result) > 0


def test_add_month_column(df):
    result = ex.add_month_column(df)
    assert "month" not in df.columns, "不应修改原 DataFrame"
    assert result["month"].iloc[0] == "2024-01"
    assert set(result["month"]) == {f"2024-0{m}" for m in range(1, 7)}


def test_select_and_rename(df):
    result = ex.select_and_rename(df)
    assert list(result.columns) == ["日期", "商品", "销售额"]
    assert len(result) == 48


def test_revenue_stats(df):
    stats = ex.revenue_stats(df)
    assert stats == {
        "sum": round(float(df.revenue.sum()), 2),
        "mean": round(float(df.revenue.mean()), 2),
        "max": round(float(df.revenue.max()), 2),
        "min": round(float(df.revenue.min()), 2),
    }
    assert all(type(v) is float for v in stats.values())


def test_orders_between(df):
    result = ex.orders_between(df, "2024-03-01", "2024-03-31")
    assert len(result) == 8
    assert result["date"].min() >= pd.Timestamp("2024-03-01")
    assert result["date"].max() <= pd.Timestamp("2024-03-31")


def test_category_counts(df):
    counts = ex.category_counts(df)
    assert sum(counts.values()) == 48
    assert set(counts) == {"电子产品", "生活用品", "图书"}
    assert counts == {k: int(v) for k, v in df["category"].value_counts().items()}
