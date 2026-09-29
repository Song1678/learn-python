import pandas as pd
import pytest

from tests.utils import DATA, load

ex = load("stage3_data.ex18_pandas_cleaning")


@pytest.fixture
def raw():
    return pd.read_csv(DATA / "users_dirty.csv")


def test_strip_strings(raw):
    result = ex.strip_strings(raw)
    assert result.loc[0, "name"] == "张三"
    assert result.loc[1, "city"] == "上海"
    assert raw.loc[0, "name"] == "  张三 ", "不应修改原 DataFrame"


def test_normalize_emails(raw):
    result = ex.normalize_emails(raw)
    assert result.loc[1, "email"] == "lisi@example.com"
    assert result.loc[4, "email"] == "zhangsan@example.com"
    assert pd.isna(result.loc[8, "email"])


def test_drop_invalid_emails(raw):
    result = ex.drop_invalid_emails(ex.normalize_emails(raw))
    assert 3 not in result["id"].tolist()   # wangwu@example 没有域名后缀
    assert 9 not in result["id"].tolist()   # 缺失
    assert len(result) == 8


def test_drop_duplicate_users(raw):
    result = ex.drop_duplicate_users(ex.normalize_emails(raw))
    assert 5 not in result["id"].tolist()
    assert 1 in result["id"].tolist()


def test_clean_age():
    df = pd.DataFrame({"age": ["20", None, "abc", "40", "150", "-3"]})
    result = ex.clean_age(df)
    assert result["age"].tolist() == [20, 30, 30, 40, 30, 30]
    assert pd.api.types.is_integer_dtype(result["age"])


def test_normalize_city():
    df = pd.DataFrame({"city": [" beijing", "上海市", "shanghai ", "广州"]})
    assert ex.normalize_city(df)["city"].tolist() == ["北京", "上海", "上海", "广州"]


def test_parse_signup_dates(raw):
    result = ex.parse_signup_dates(raw)
    assert pd.api.types.is_datetime64_any_dtype(result["signup_date"])
    assert result.loc[2, "signup_date"] == pd.Timestamp("2024-03-10")
    assert pd.isna(result.loc[5, "signup_date"])


def test_clean_users(raw):
    result = ex.clean_users(raw)
    assert result["id"].tolist() == [1, 2, 4, 6, 7, 8, 10]
    assert list(result.index) == list(range(7))
    assert result["age"].tolist() == [28, 31, 42, 31, 31, 31, 31]
    assert result["city"].tolist() == ["北京", "上海", "北京", "深圳", "上海", "上海", "深圳"]
    assert result["name"].tolist()[0] == "张三"
    assert result["email"].str.islower().all()


def test_missing_report(raw):
    assert ex.missing_report(raw) == {"age": 2, "email": 1}
