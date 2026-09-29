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
        self.owner = owner
        self._balance = balance
        self.history = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self._balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须大于 0")
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        self.history.append(("withdraw", amount))

    def __str__(self):
        return f"{self.owner} 的账户，余额 {self._balance:.2f} 元"


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
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __iter__(self):
        yield self.x
        yield self.y


class Shape:
    """图形基类。子类需要实现 area()。

    - name 属性：类名，例如 Rectangle(...).name == "Rectangle"
      提示：type(self).__name__
    - describe()：返回 "Rectangle，面积 6.00"
    """

    @property
    def name(self):
        return type(self).__name__

    def area(self):
        raise NotImplementedError

    def describe(self):
        return f"{self.name}，面积 {self.area():.2f}"


class Rectangle(Shape):
    """矩形：Rectangle(width, height)"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    """圆形：Circle(radius)，面积用 math.pi"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Rectangle):
    """正方形：Square(side)，继承 Rectangle，用 super().__init__ 复用逻辑。"""

    def __init__(self, side):
        super().__init__(side, side)


def total_area(shapes):
    """所有图形面积之和（多态）。"""
    return sum(s.area() for s in shapes)


class Stack:
    """栈。

    - push(item) / pop() / peek()
    - 空栈 pop() 或 peek() 时抛出 IndexError("stack is empty")
    - len(stack) 返回元素个数；空栈在 if 判断中为 False
    - Stack.from_list([1, 2, 3])：类方法，按顺序 push 后返回新栈
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("stack is empty")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("stack is empty")
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    @classmethod
    def from_list(cls, items):
        stack = cls()
        for item in items:
            stack.push(item)
        return stack
