"""
练习 11：迭代器与生成器
======================

知识点 & 与 JS 的对比
--------------------
- 生成器函数：包含 yield 的函数（JS 里是 function* 和 yield，概念完全一致）
      def count_up(n):
          for i in range(n):
              yield i
      gen = count_up(3)
      next(gen)          # 0      （JS: gen.next().value）
      list(count_up(3))  # [0, 1, 2]
- yield from 子生成器  （JS: yield*）
- 生成器是惰性的：只在需要时计算，适合处理大文件 / 无限序列
- 迭代器协议：实现 __iter__() 返回自身、__next__() 返回下一个值，
  没有值时 raise StopIteration  （JS: [Symbol.iterator] 和 next() 返回 {done: true}）
- itertools 模块提供大量工具：islice, count, cycle, chain, groupby ...

运行测试：  pytest tests/test_ex11_iterators_generators.py
"""
from itertools import islice


def countdown(n):
    """生成 n, n-1, ..., 1。

    >>> list(countdown(3))
    [3, 2, 1]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def fibonacci():
    """无限斐波那契数列生成器：0, 1, 1, 2, 3, 5, ...

    >>> list(islice(fibonacci(), 6))
    [0, 1, 1, 2, 3, 5]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def take(iterable, n):
    """取前 n 个元素返回列表（iterable 可能是无限的！）。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def chunked(iterable, size):
    """把任意可迭代对象按 size 分组，逐组 yield 列表。

    >>> list(chunked(range(5), 2))
    [[0, 1], [2, 3], [4]]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def running_total(nums):
    """逐个 yield 累计和。

    >>> list(running_total([1, 2, 3]))
    [1, 3, 6]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def flatten_deep(nested):
    """递归拍平任意深度的嵌套列表。提示：yield from

    >>> list(flatten_deep([1, [2, [3, [4]]], 5]))
    [1, 2, 3, 4, 5]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def grep_lines(lines, keyword):
    """生成器管道的一环：只 yield 含有 keyword 的行（去掉首尾空白）。
    思考：用它处理几 GB 的日志文件也不会爆内存。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


class MyRange:
    """手写一个迭代器类，行为类似 range(start, stop, step)（只需支持正 step）。

    >>> list(MyRange(0, 10, 3))
    [0, 3, 6, 9]

    需要实现 __init__、__iter__、__next__。
    """

    def __init__(self, start, stop, step=1):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __iter__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError

    def __next__(self):
        # TODO: 在这里写你的代码
        raise NotImplementedError
