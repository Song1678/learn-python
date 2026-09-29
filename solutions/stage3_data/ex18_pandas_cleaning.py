"""
练习 18：pandas 数据清洗
=======================

真实数据总是脏的。数据文件 data/users_dirty.csv 中包含：
多余空格、大小写不一致的邮箱、缺失值、非法年龄、重复用户、城市写法不统一、日期格式混乱……

知识点
------
- 缺失值：  df.isna()  df.isna().sum()  df.dropna(subset=[...])  s.fillna(value)
- 字符串方法（.str 访问器，向量化）：
      s.str.strip()  s.str.lower()  s.str.contains(regex)  s.str.replace(a, b)
- 类型转换：  pd.to_numeric(s, errors="coerce")     无法转换的变成 NaN
              pd.to_datetime(s, errors="coerce", format="mixed")
- 映射替换：  s.replace({"旧": "新"})   s.map(dict)
- 去重：      df.drop_duplicates(subset=["email"], keep="first")
- 条件赋值：  df.loc[条件, "列"] = 值    或   s.where(cond)（不满足 cond 的变 NaN）
- 每个函数都应返回新的 DataFrame，不修改传入的 df（先 df = df.copy()）

运行测试：  pytest tests/test_ex18_pandas_cleaning.py
"""
import pandas as pd

CITY_MAP = {"beijing": "北京", "shanghai": "上海", "上海市": "上海"}
EMAIL_PATTERN = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"


def strip_strings(df):
    """去掉所有文本列两端的空白。
    提示：df.select_dtypes(include=["object", "string"]).columns 找出文本列
    """
    df = df.copy()
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip()
    return df


def normalize_emails(df):
    """email 列去空白并转小写（缺失值保持缺失）。"""
    df = df.copy()
    df["email"] = df["email"].str.strip().str.lower()
    return df


def drop_invalid_emails(df):
    """删除 email 缺失或不符合 EMAIL_PATTERN 的行。
    提示：s.str.match(pattern, na=False)
    """
    return df[df["email"].str.match(EMAIL_PATTERN, na=False)]


def drop_duplicate_users(df):
    """按 email 去重，保留第一次出现的行。"""
    return df.drop_duplicates(subset=["email"], keep="first")


def clean_age(df):
    """age 列：转成数字（无法转换的变 NaN），不在 0~120 之间的也视为 NaN，
    然后用剩余有效年龄的中位数填充缺失值，最终转为 int 类型。
    """
    df = df.copy()
    age = pd.to_numeric(df["age"], errors="coerce")
    age = age.where(age.between(0, 120))
    df["age"] = age.fillna(age.median()).astype(int)
    return df


def normalize_city(df):
    """city 列去空白，然后用 CITY_MAP 统一写法（不在映射中的保持不变）。"""
    df = df.copy()
    df["city"] = df["city"].str.strip().replace(CITY_MAP)
    return df


def parse_signup_dates(df):
    """signup_date 转成 datetime，无法解析的变成 NaT。
    数据中同时存在 "2024-01-15" 和 "2024/03/10" 两种格式。
    """
    df = df.copy()
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce", format="mixed")
    return df


def clean_users(df):
    """清洗流水线，按顺序执行：
    strip_strings -> normalize_emails -> drop_invalid_emails -> drop_duplicate_users
    -> clean_age -> normalize_city -> parse_signup_dates，最后 reset_index(drop=True)。
    提示：可以用 df.pipe(func) 串起来。
    """
    return (
        df.pipe(strip_strings)
        .pipe(normalize_emails)
        .pipe(drop_invalid_emails)
        .pipe(drop_duplicate_users)
        .pipe(clean_age)
        .pipe(normalize_city)
        .pipe(parse_signup_dates)
        .reset_index(drop=True)
    )


def missing_report(df):
    """返回每列缺失值数量的 dict，只包含缺失数 > 0 的列。"""
    counts = df.isna().sum()
    return {col: int(n) for col, n in counts.items() if n > 0}
