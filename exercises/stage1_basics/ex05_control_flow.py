"""
练习 05：流程控制
================

知识点 & 与 JS 的对比
--------------------
- 用缩进（4 个空格）代替 { }，条件后面加冒号：
      if x > 0:
          ...
      elif x == 0:        # 不是 else if
          ...
      else:
          ...
- 三元表达式：  a if cond else b   （JS：cond ? a : b）
- for 循环只有“遍历”一种形式（类似 JS 的 for...of）：
      for i in range(5):           # 0,1,2,3,4
      for i in range(1, 10, 2):    # 1,3,5,7,9
      for i, item in enumerate(lst):   # 同时拿到下标
      for a, b in zip(list1, list2):   # 并行遍历
- while 循环、break、continue 与 JS 相同
- for ... else：循环没有被 break 时执行 else 块
- match / case（Python 3.10+，类似 switch 但更强大，支持解构）：
      match command:
          case "start":
              ...
          case "stop" | "quit":
              ...
          case _:
              ...          # 默认分支
- pass：什么都不做的占位语句

运行测试：  pytest tests/test_ex05_control_flow.py
"""


def fizzbuzz(n):
    """返回 1..n 的 FizzBuzz 列表（元素都是字符串）：
    3 的倍数 -> "Fizz"，5 的倍数 -> "Buzz"，同时是 -> "FizzBuzz"，否则数字本身。

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def grade(score):
    """90+ -> 'A'，80+ -> 'B'，70+ -> 'C'，60+ -> 'D'，否则 'F'。
    score 不在 0~100 时抛出 ValueError。

    >>> grade(85)
    'B'
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def first_negative_index(nums):
    """返回第一个负数的下标，没有就返回 -1。提示：enumerate

    >>> first_negative_index([3, 5, -1, -4])
    2
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def is_prime(n):
    """判断质数（n < 2 不是质数）。

    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def collatz_steps(n):
    """考拉兹猜想：n 为偶数则 n//2，奇数则 3n+1，返回变成 1 需要的步数。

    >>> collatz_steps(6)   # 6→3→10→5→16→8→4→2→1
    8
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def multiplication_table(n):
    """返回 n×n 乘法表的“下三角”，每行是一个字符串，式子之间用一个空格分隔。

    >>> multiplication_table(3)
    ['1x1=1', '1x2=2 2x2=4', '1x3=3 2x3=6 3x3=9']
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def dot_product(a, b):
    """两个等长向量的点积。提示：zip

    >>> dot_product([1, 2, 3], [4, 5, 6])
    32
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def http_status_text(code):
    """用 match / case 实现：
    200 -> 'OK'，301 或 302 -> 'Redirect'，404 -> 'Not Found'，
    其他 500~599 -> 'Server Error'，其余 -> 'Unknown'

    提示：case int() if 500 <= code < 600:  可以带条件（守卫）

    >>> http_status_text(302)
    'Redirect'
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def handle_command(command):
    """用 match 解构列表形式的命令：
      ["go", 方向]         -> f"向{方向}移动"
      ["pick", 物品]       -> f"捡起{物品}"
      ["drop", *物品们]    -> f"丢下{n}件物品"（n 为物品数量）
      ["quit"]             -> "再见"
      其他                 -> "未知命令"

    >>> handle_command(["go", "北"])
    '向北移动'
    >>> handle_command(["drop", "剑", "盾"])
    '丢下2件物品'
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError
