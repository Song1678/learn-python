"""
练习 15：用标准库处理 CSV（数据处理入门）
=======================================

在学 pandas 之前，先用纯 Python 处理一次数据，理解“读取 → 转换 → 聚合 → 输出”的流程。

数据文件：data/sales.csv
    order_id,date,region,product,category,quantity,unit_price
    1003,2024-01-02,华东,保温杯,生活用品,2,89

知识点
------
- csv.DictReader：每行读成一个 dict（值全部是字符串！需要自己转换类型）
      with open(path, encoding="utf-8", newline="") as f:
          for row in csv.DictReader(f): ...
- csv.DictWriter：写出 dict
      writer = csv.DictWriter(f, fieldnames=[...]); writer.writeheader(); writer.writerows(rows)
  ⚠️ 写 CSV 时 open 要加 newline=""，否则 Windows 下会多出空行
- 聚合常用 dict / defaultdict / Counter

运行测试：  pytest tests/test_ex15_csv_stdlib.py
"""
import csv
from collections import defaultdict


def read_sales(path):
    """读取销售 CSV，返回 dict 列表，并转换类型：
    order_id -> int, quantity -> int, unit_price -> float，其余保持字符串。
    """
    rows = []
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            row["order_id"] = int(row["order_id"])
            row["quantity"] = int(row["quantity"])
            row["unit_price"] = float(row["unit_price"])
            rows.append(row)
    return rows


def total_revenue(rows):
    """总销售额 = Σ quantity × unit_price"""
    return sum(r["quantity"] * r["unit_price"] for r in rows)


def revenue_by_region(rows):
    """各地区销售额：{地区: 销售额}"""
    result = defaultdict(float)
    for r in rows:
        result[r["region"]] += r["quantity"] * r["unit_price"]
    return dict(result)


def top_products(rows, n=3):
    """销售额最高的 n 个商品：[(商品, 销售额), ...]，按销售额降序。"""
    totals = defaultdict(float)
    for r in rows:
        totals[r["product"]] += r["quantity"] * r["unit_price"]
    return sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:n]


def monthly_revenue(rows):
    """按月汇总销售额：{"2024-01": 销售额, ...}，key 按月份升序排列。
    提示：date 字段前 7 个字符就是 "YYYY-MM"。
    """
    totals = defaultdict(float)
    for r in rows:
        totals[r["date"][:7]] += r["quantity"] * r["unit_price"]
    return dict(sorted(totals.items()))


def write_region_report(path, rows):
    """输出地区报表 CSV，列为 region,orders,revenue（订单数、销售额），
    按 revenue 降序；revenue 保留 2 位小数（字符串形式如 "12345.00"）。
    """
    stats = defaultdict(lambda: {"orders": 0, "revenue": 0.0})
    for r in rows:
        s = stats[r["region"]]
        s["orders"] += 1
        s["revenue"] += r["quantity"] * r["unit_price"]
    ordered = sorted(stats.items(), key=lambda kv: kv[1]["revenue"], reverse=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["region", "orders", "revenue"])
        writer.writeheader()
        for region, s in ordered:
            writer.writerow({"region": region, "orders": s["orders"], "revenue": f"{s['revenue']:.2f}"})
