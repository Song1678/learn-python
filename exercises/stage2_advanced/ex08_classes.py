"""
练习 08：类与面向对象
====================

知识点 & 与 JS 的对比
--------------------
    JS                                   Python
    class Dog extends Animal {           class Dog(Animal):
      constructor(name) {                    def __init__(self, name):
        super(name);                             super().__init__(name)
        this.name = name;                        self.name = name
      }
      bark() { return this.name }            def bark(self):
    }                                            return self.name

- 方法的第一个参数必须是 self（相当于 this，但要显式写出来）
- 创建实例不需要 new：  d = Dog("旺财")
- 约定：以 _ 开头的属性表示“内部使用”（Python 没有真正的 private）
- @property：把方法变成只读属性（类似 JS 的 get xxx()）
- @classmethod / @staticmethod：类方法 / 静态方法
- “魔术方法”（dunder methods）让对象支持内置操作：
      __repr__  -> repr(obj) / 调试时显示        __str__  -> str(obj) / print
      __eq__    -> ==        __lt__ -> <         __add__  -> +     __mul__ -> *
      __len__   -> len(obj)  __iter__ -> for 循环  __bool__ -> 真值判断
      __getitem__ -> obj[i]  __contains__ -> in

运行测试：  pytest tests/test_ex08_classes.py
"""
import math


class BankAccount:
    """银行账户。

    - BankAccount("Tom") 初始余额为 0；也可以 BankAccount("Tom", 100)
    - deposit(amount)：存款，amount <= 0 时抛 ValueError
    - withdraw(amount)：取款，amount <= 0 或余额不足时抛 ValueError
    - balance：只读属性（@property），不能直接 acc.balance = 1000
    - history：列表，记录每次成功操作，如 ("deposit", 50)、("withdraw", 20)
    - str(acc) == "Tom 的账户，余额 80.00 元"
    """

    def __init__(self, owner, balance=0):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    @property
    def balance(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def deposit(self, amount):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def withdraw(self, amount):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __str__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError


class Vector:
    """二维向量，支持运算符。

    >>> Vector(1, 2) + Vector(3, 4)
    Vector(4, 6)
    >>> Vector(1, 2) * 3
    Vector(3, 6)
    >>> abs(Vector(3, 4))
    5.0
    >>> x, y = Vector(7, 8)     # 支持解包（实现 __iter__）
    """

    def __init__(self, x, y):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __repr__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __eq__(self, other):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __add__(self, other):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __sub__(self, other):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __mul__(self, scalar):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __abs__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __iter__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError


class Shape:
    """图形基类。子类需要实现 area()。

    - name 属性：类名，例如 Rectangle(...).name == "Rectangle"
      提示：type(self).__name__
    - describe()：返回 "Rectangle，面积 6.00"
    """

    @property
    def name(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def area(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def describe(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError


class Rectangle(Shape):
    """矩形：Rectangle(width, height)"""

    def __init__(self, width, height):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def area(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError


class Circle(Shape):
    """圆形：Circle(radius)，面积用 math.pi"""

    def __init__(self, radius):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def area(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError


class Square(Rectangle):
    """正方形：Square(side)，继承 Rectangle，用 super().__init__ 复用逻辑。"""

    def __init__(self, side):
        # TODO: 在这里写你的代码
        raise NotImplementedError


def total_area(shapes):
    """所有图形面积之和（多态）。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


class Stack:
    """栈。

    - push(item) / pop() / peek()
    - 空栈 pop() 或 peek() 时抛出 IndexError("stack is empty")
    - len(stack) 返回元素个数；空栈在 if 判断中为 False
    - Stack.from_list([1, 2, 3])：类方法，按顺序 push 后返回新栈
    """

    def __init__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def push(self, item):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def pop(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def peek(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __len__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __bool__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    @classmethod
    def from_list(cls, items):
        # TODO: 在这里写你的代码
        raise NotImplementedError
