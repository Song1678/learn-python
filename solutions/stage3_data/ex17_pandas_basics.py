"""
练习 17：pandas 基础 —— 读取、选择、过滤
=======================================

pandas 的两个核心结构：
- Series：带索引的一维数据（一列）
- DataFrame：二维表格（像 Excel 表 / SQL 表）

知识点
------
    import pandas as pd
    df = pd.read_csv(path, parse_dates=["date"])     # 读取并把 date 列解析成日期
    df.head()  df.info()  df.describe()  df.shape  df.columns  df.dtypes
- 选列：    df["col"] -> Series；  df[["a", "b"]] -> DataFrame
- 新增列：  df["revenue"] = df["quantity"] * df["unit_price"]   （向量化，不写循环）
- 过滤：    df[df["region"] == "华东"]；多个条件 df[(cond1) & (cond2)]
            df.query("quantity > 5")      df[df["x"].isin([...])]
- 按标签取：df.loc[行条件, 列名]；  按位置取：df.iloc[0:5, 0:2]
- 排序：    df.sort_values("revenue", ascending=False)
- 重命名：  df.rename(columns={"a": "A"})
- 日期列：  df["date"].dt.year / .dt.month / .dt.strftime("%Y-%m")
- 重置索引：df.reset_index(drop=True)
- 避免修改传入的 df：先 df = df.copy()

运行测试：  pytest tests/test_ex17_pandas_basics.py
"""
import pandas as pd


def load_sales(path):
    """读取销售数据：date 列解析为日期，并新增 revenue = quantity * unit_price 列。"""
    df = pd.read_csv(path, parse_dates=["date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df


def basic_info(df):
    """返回 {"rows": 行数, "columns": 列名列表, "regions": 去重排序后的地区列表}"""
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "regions": sorted(df["region"].unique().tolist()),
    }


def filter_by_region(df, region):
    """筛选某个地区的订单。"""
    return df[df["region"] == region]


def big_orders(df, min_revenue):
    """revenue >= min_revenue 的订单，按 revenue 降序，并重置索引（drop=True）。"""
    result = df[df["revenue"] >= min_revenue].sort_values("revenue", ascending=False)
    return result.reset_index(drop=True)


def electronics_in_region(df, region, min_quantity):
    """地区为 region、类别为“电子产品”且数量 >= min_quantity 的订单（多条件过滤）。"""
    mask = (df["region"] == region) & (df["category"] == "电子产品") & (df["quantity"] >= min_quantity)
    return df[mask]


def add_month_column(df):
    """返回新增 month 列（字符串 "YYYY-MM"）的副本，不修改原 df。"""
    df = df.copy()
    df["month"] = df["date"].dt.strftime("%Y-%m")
    return df


def select_and_rename(df):
    """只保留 date, product, revenue 三列，并重命名为 日期, 商品, 销售额。"""
    return df[["date", "product", "revenue"]].rename(
        columns={"date": "日期", "product": "商品", "revenue": "销售额"}
    )


def revenue_stats(df):
    """revenue 列的统计：{"sum", "mean", "max", "min"}，均为 round 到 2 位的 float。"""
    s = df["revenue"]
    return {k: round(float(v), 2) for k, v in
            {"sum": s.sum(), "mean": s.mean(), "max": s.max(), "min": s.min()}.items()}


def orders_between(df, start, end):
    """日期在 [start, end] 之间（含两端，参数是 "YYYY-MM-DD" 字符串）的订单。
    提示：Series.between
    """
    return df[df["date"].between(pd.Timestamp(start), pd.Timestamp(end))]


def category_counts(df):
    """每个类别的订单数量 dict。提示：value_counts()"""
    return {k: int(v) for k, v in df["category"].value_counts().items()}
