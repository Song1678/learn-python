"""
练习 14：dataclass 与类型注解
============================

知识点
------
- 类型注解（类似 TypeScript，但运行时不强制检查，主要给编辑器 / mypy 用）：
      def total(prices: list[float], rate: float = 1.0) -> float: ...
      name: str | None = None          # 可空类型（3.10+ 写法）
      dict[str, int]  tuple[int, int]  list[dict[str, str]]
- @dataclass 自动生成 __init__ / __repr__ / __eq__，非常适合“数据对象”：
      from dataclasses import dataclass, field

      @dataclass
      class User:
          name: str
          age: int = 0
          tags: list[str] = field(default_factory=list)   # 可变默认值必须这样写

  @dataclass(order=True)  自动生成比较方法（按字段顺序比较）
  @dataclass(frozen=True) 不可变
- __post_init__：生成的 __init__ 执行完后调用，可用于校验 / 计算字段

说明：本练习中 dataclass 的字段已经给出，你需要实现方法。

运行测试：  pytest tests/test_ex14_dataclasses_typing.py
"""
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def __post_init__(self) -> None:
        """价格为负数时抛出 ValueError。"""
        # TODO: 在这里写你的代码
        raise NotImplementedError

    @property
    def total_value(self) -> float:
        """库存总价值 = 价格 × 数量"""
        # TODO: 在这里写你的代码
        raise NotImplementedError


@dataclass
class Inventory:
    products: list[Product] = field(default_factory=list)

    def add(self, product: Product) -> None:
        """添加商品；如果同名商品已存在，则把数量累加到已有商品上。"""
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def find(self, name: str) -> Product | None:
        """按名称查找商品，找不到返回 None。"""
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def total_value(self) -> float:
        """所有商品的库存总价值。"""
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def low_stock(self, threshold: int = 5) -> list[str]:
        """数量低于 threshold 的商品名称列表（按名称排序）。"""
        # TODO: 在这里写你的代码
        raise NotImplementedError


@dataclass(order=True)
class Student:
    # 排序时按字段顺序比较：先比 score，再比 name
    score: int
    name: str = field(compare=False)


def top_students(students: list[Student], n: int) -> list[str]:
    """返回分数最高的 n 个学生的名字（分数从高到低）。
    提示：Student 使用了 order=True，可以直接 sorted(students, reverse=True)。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def summarize(products: list[Product]) -> dict[str, float]:
    """返回 {"count": 商品种类数, "total_quantity": 总数量, "avg_price": 平均价格(保留2位)}。
    空列表时 avg_price 为 0.0。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError
