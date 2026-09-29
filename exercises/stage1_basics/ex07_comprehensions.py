"""
练习 07：推导式（Pythonic 写法的核心）
====================================

知识点 & 与 JS 的对比
--------------------
- 列表推导式 ≈ JS 的 map + filter：
      JS:      nums.filter(n => n % 2 === 0).map(n => n * n)
      Python:  [n * n for n in nums if n % 2 == 0]
- 字典推导式：  {k: v for k, v in pairs}
- 集合推导式：  {len(w) for w in words}
- 嵌套：        [x for row in matrix for x in row]   （顺序和写 for 循环一样）
- 条件表达式放在前面：  ["偶" if n % 2 == 0 else "奇" for n in nums]
- 生成器表达式（惰性，不占内存）：  sum(n * n for n in range(10**6))
- Python 也有 map / filter 函数，但推导式更常用、更易读
- any() / all()：  any(n < 0 for n in nums)   （类似 JS 的 some / every）

本练习请尽量每题只用一行推导式完成！

运行测试：  pytest tests/test_ex07_comprehensions.py
"""


def squares_of_evens(nums):
    """偶数的平方。

    >>> squares_of_evens([1, 2, 3, 4])
    [4, 16]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def word_lengths(words):
    """单词 -> 长度 的字典。

    >>> word_lengths(["hi", "hello"])
    {'hi': 2, 'hello': 5}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def transpose(matrix):
    """矩阵转置。

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def flatten_matrix(matrix):
    """二维列表拍平。

    >>> flatten_matrix([[1, 2], [3, 4]])
    [1, 2, 3, 4]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def label_numbers(nums):
    """偶数标记为 '偶'，奇数标记为 '奇'。

    >>> label_numbers([1, 2])
    ['奇', '偶']
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def filter_by_value(d, threshold):
    """只保留值 >= threshold 的键值对。

    >>> filter_by_value({"a": 1, "b": 5, "c": 3}, 3)
    {'b': 5, 'c': 3}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def unique_lengths(words):
    """所有单词长度组成的集合。

    >>> unique_lengths(["a", "bb", "cc", "ddd"]) == {1, 2, 3}
    True
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def pythagorean_triples(n):
    """找出所有 a < b < c <= n 且 a² + b² = c² 的三元组，按 (a, b, c) 顺序返回列表。

    >>> pythagorean_triples(13)
    [(3, 4, 5), (5, 12, 13), (6, 8, 10)]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def sum_of_squares(n):
    """1² + 2² + ... + n²，请用生成器表达式配合 sum。

    >>> sum_of_squares(3)
    14
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def has_negative(nums):
    """是否存在负数。提示：any()

    >>> has_negative([1, -2, 3])
    True
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def index_users(users):
    """users 是字典列表，返回 id -> name 的字典，跳过没有 id 的用户。

    >>> index_users([{"id": 1, "name": "A"}, {"name": "B"}])
    {1: 'A'}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError
