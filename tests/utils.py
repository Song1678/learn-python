"""测试辅助：决定测试加载 exercises/（你的答案）还是 solutions/（参考答案）。"""
import importlib
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(name: str):
    """load("stage1_basics.ex01_basics") -> 对应模块

    设置环境变量 LEARN_PY_SOLUTIONS=1 时加载参考答案（python check.py --solutions）。
    """
    pkg = "solutions" if os.environ.get("LEARN_PY_SOLUTIONS") else "exercises"
    return importlib.import_module(f"{pkg}.{name}")
