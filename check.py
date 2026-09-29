"""
学习进度检查器
============

用法：
    python check.py              # 查看所有练习的完成情况
    python check.py 3            # 只看第 3 个练习（显示失败详情）
    python check.py stage2       # 只看第二阶段
    python check.py --solutions  # 用参考答案跑一遍（验证环境是否正常）
"""
import contextlib
import os
import sys
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests"

STAGES = {
    "stage1": ("第一阶段：Python 基础语法", range(1, 8)),
    "stage2": ("第二阶段：Python 进阶", range(8, 15)),
    "stage3": ("第三阶段：数据处理与分析", range(15, 20)),
    "stage4": ("第四阶段：网络爬虫", range(20, 23)),
}


class Collector:
    def __init__(self):
        self.results = defaultdict(lambda: {"passed": 0, "failed": 0, "todo": 0})

    def pytest_runtest_logreport(self, report):
        if report.when == "call" or (report.when == "setup" and report.outcome != "passed"):
            name = Path(report.nodeid.split("::")[0]).stem
            bucket = self.results[name]
            if report.passed:
                bucket["passed"] += 1
            elif "NotImplementedError" in str(report.longrepr):
                bucket["todo"] += 1
            else:
                bucket["failed"] += 1

    def pytest_collectreport(self, report):
        if report.failed:
            name = Path(report.nodeid).stem
            self.results[name]["failed"] += 1


def number_of(test_file):
    return int(test_file.stem.split("_")[1][2:])


def main(argv):
    if "--solutions" in argv:
        os.environ["LEARN_PY_SOLUTIONS"] = "1"
        argv = [a for a in argv if a != "--solutions"]

    files = sorted(TESTS.glob("test_ex*.py"))
    verbose = False
    if argv:
        arg = argv[0].lower()
        if arg.isdigit():
            files = [f for f in files if number_of(f) == int(arg)]
            verbose = True
        elif arg in STAGES:
            files = [f for f in files if number_of(f) in STAGES[arg][1]]
        if not files:
            print(f"找不到对应的练习：{argv[0]}")
            return 1

    collector = Collector()
    args = [str(f) for f in files] + ["-p", "no:cacheprovider"]
    if verbose:
        pytest.main(args + ["--tb=short"], plugins=[collector])
    else:
        with open(os.devnull, "w") as devnull, contextlib.redirect_stdout(devnull):
            pytest.main(args + ["--tb=no"], plugins=[collector])

    total_passed = total_tests = 0
    for key, (title, numbers) in STAGES.items():
        stage_files = [f for f in files if number_of(f) in numbers]
        if not stage_files:
            continue
        print(f"\n{title}")
        for f in stage_files:
            r = collector.results[f.stem]
            n = r["passed"] + r["failed"] + r["todo"]
            total_passed += r["passed"]
            total_tests += n
            if n and r["passed"] == n:
                icon = "✅"
            elif r["passed"] or r["failed"]:
                icon = "🚧"
            else:
                icon = "⬜"
            bar = "█" * round(10 * r["passed"] / n) if n else ""
            name = f.stem.removeprefix("test_")
            print(f"  {icon} {name:<32} {bar:<10} {r['passed']:>3}/{n}")

    pct = 100 * total_passed / total_tests if total_tests else 0
    print(f"\n总进度：{total_passed}/{total_tests} 个测试通过（{pct:.0f}%）")
    if not verbose and total_passed < total_tests:
        print("提示：python check.py <练习编号>  查看某个练习的失败详情")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
