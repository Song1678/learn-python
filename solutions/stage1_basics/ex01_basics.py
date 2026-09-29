"""
练习 01：变量、数字与类型
========================

知识点 & 与 JS 的对比
--------------------
- 没有 let / const / var，直接赋值：  x = 1
- 常用类型：int, float, str, bool, None, list, dict, tuple, set
    * JS 的 null / undefined  →  Python 只有 None
    * JS 的 true / false      →  Python 是 True / False（首字母大写）
- 整数除法：  7 // 2 == 3，取余：7 % 2 == 1，普通除法永远得到 float：6 / 2 == 3.0
- 幂运算：    2 ** 10 == 1024（JS 也是 **）
- 查看类型：  type(x)  /  isinstance(x, int)   （JS 用 typeof）
- 真值判断（重要区别！）：
    * Python 中 空列表 []、空字典 {}、空字符串 ""、0、None 都是 False
    * JS 中 [] 和 {} 是 truthy，Python 中不是！
- 逻辑运算符：and / or / not（不是 && || !）
- 比较：== 就是“值相等”，没有 ===；is 用来判断“是不是同一个对象”（一般只用于 x is None）
- 类型转换：int("42"), float("3.14"), str(42), bool(0)
- 多重赋值 / 交换：  a, b = b, a

运行测试：  pytest tests/test_ex01_basics.py
"""


def celsius_to_fahrenheit(celsius):
    """把摄氏度转换为华氏度，公式 F = C * 9 / 5 + 32。

    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(0)
    32.0
    """
    return celsius * 9 / 5 + 32


def divide_with_remainder(a, b):
    """返回 (商, 余数) 组成的元组。提示：用 // 和 %。

    >>> divide_with_remainder(17, 5)
    (3, 2)
    """
    return a // b, a % b


def describe_type(value):
    """返回值的类型名称字符串。

    提示：type(value).__name__

    >>> describe_type(1)
    'int'
    >>> describe_type("hi")
    'str'
    >>> describe_type(None)
    'NoneType'
    """
    return type(value).__name__


def is_truthy(value):
    """返回 value 在 Python 中的真值（True/False）。

    注意和 JS 的区别：is_truthy([]) 在 Python 里是 False！

    >>> is_truthy([])
    False
    >>> is_truthy("0")
    True
    """
    return bool(value)


def safe_int(text, default=0):
    """把字符串转成 int，转换失败时返回 default。

    提示：int() 转换失败会抛出 ValueError，用 try / except 捕获。
    （JS 的 parseInt("12abc") 会得到 12，但 Python 的 int("12abc") 会报错。）

    >>> safe_int("42")
    42
    >>> safe_int("abc", -1)
    -1
    """
    try:
        return int(text)
    except ValueError:
        return default


def swap(a, b):
    """交换两个值并返回 (b, a)。试试 Python 的多重赋值。

    >>> swap(1, 2)
    (2, 1)
    """
    a, b = b, a
    return a, b


def bmi(weight_kg, height_m):
    """计算 BMI = 体重 / 身高²，结果用 round() 保留 1 位小数。

    >>> bmi(70, 1.75)
    22.9
    """
    return round(weight_kg / height_m ** 2, 1)


def is_valid_age(age):
    """age 是 int 且在 0~150 之间（含边界）时返回 True。

    提示：Python 支持链式比较 0 <= age <= 150。
    注意：True 也是 int 的子类，但这里不用特别处理。

    >>> is_valid_age(18)
    True
    >>> is_valid_age("18")
    False
    """
    return isinstance(age, int) and 0 <= age <= 150
