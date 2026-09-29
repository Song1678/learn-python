"""
练习 19：pandas 分组聚合与分析
============================

这是数据分析最核心的部分，相当于 SQL 的 GROUP BY / JOIN。

知识点
------
- 分组聚合：
      df.groupby("region")["revenue"].sum()
      df.groupby(["region", "category"])["revenue"].sum()
      df.groupby("region").agg(orders=("order_id", "count"), revenue=("revenue", "sum"))
- 透视表：   df.pivot_table(index="region", columns="category", values="revenue",
                            aggfunc="sum", fill_value=0)
- 合并：     pd.merge(left, right, on="region", how="left")   （类似 SQL JOIN）
- 排序与取最大：  s.sort_values(ascending=False)   s.idxmax()   s.nlargest(3)
- 变化率：   s.pct_change()
- 占比：     s / s.sum()

本练习中传入的 df 已经包含 revenue 列（即练习 17 中 load_sales 的结果）。

运行测试：  pytest tests/test_ex19_pandas_analysis.py
"""
import pandas as pd


def revenue_by_region(df):
    """各地区销售额 Series，按销售额降序。"""
    return df.groupby("region")["revenue"].sum().sort_values(ascending=False)


def region_summary(df):
    """每个地区的汇总 DataFrame（index 为 region），列：
    orders（订单数）、quantity（总数量）、revenue（总销售额）、avg_order（平均每单销售额，保留 2 位）
    按 revenue 降序。
    """
    summary = df.groupby("region").agg(
        orders=("order_id", "count"),
        quantity=("quantity", "sum"),
        revenue=("revenue", "sum"),
    )
    summary["avg_order"] = (summary["revenue"] / summary["orders"]).round(2)
    return summary.sort_values("revenue", ascending=False)


def category_share(df):
    """各类别销售额占比（百分比，保留 1 位小数），按占比降序。例如 {"电子产品": 80.5, ...} 形式的 Series。"""
    s = df.groupby("category")["revenue"].sum()
    return (s / s.sum() * 100).round(1).sort_values(ascending=False)


def monthly_revenue(df):
    """按月销售额 Series，index 为 "YYYY-MM" 字符串，按月份升序。"""
    return df.groupby(df["date"].dt.strftime("%Y-%m"))["revenue"].sum().sort_index()


def month_over_month(df):
    """月环比增长率 Series（保留 4 位小数），第一个月为 NaN。复用 monthly_revenue。"""
    return monthly_revenue(df).pct_change().round(4)


def pivot_region_category(df):
    """透视表：行为 region，列为 category，值为 revenue 之和，缺失填 0。"""
    return df.pivot_table(index="region", columns="category", values="revenue",
                          aggfunc="sum", fill_value=0)


def top_product_by_region(df):
    """每个地区销售额最高的商品：{地区: 商品}"""
    totals = df.groupby(["region", "product"])["revenue"].sum()
    return {region: product for region, product in totals.groupby(level="region").idxmax()}


def compare_with_targets(df, targets):
    """targets 是包含 region,target 的 DataFrame。返回 DataFrame，列：
    region, revenue, target, achievement（revenue / target，保留 2 位）
    按 achievement 降序，重置索引。
    """
    actual = df.groupby("region", as_index=False)["revenue"].sum()
    merged = pd.merge(actual, targets, on="region", how="inner")
    merged["achievement"] = (merged["revenue"] / merged["target"]).round(2)
    return merged.sort_values("achievement", ascending=False).reset_index(drop=True)
