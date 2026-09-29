"""
练习 06：函数
============

知识点 & 与 JS 的对比
--------------------
- 定义：  def add(a, b=0):  return a + b
- 调用时可以用关键字参数：  add(b=2, a=1)   （JS 没有这个）
- 可变参数：
      def f(*args):     args 是元组       （类似 JS 的 ...args）
      def f(**kwargs):  kwargs 是字典
      f(*lst)  f(**d)   调用时展开
- 仅限关键字参数：  def f(a, *, verbose=False)   verbose 只能写成 verbose=True
- lambda：  lambda x: x * 2    （类似箭头函数 x => x * 2，但只能写一个表达式）
- 函数是一等公民，可以传参、返回、存到变量里
- 闭包修改外层变量需要 nonlocal 声明（JS 不需要）
- ⚠️ 默认参数陷阱：默认值只在定义时计算一次！
      def bad(item, lst=[]):   # 所有调用共享同一个列表！
      def good(item, lst=None):
          if lst is None: lst = []
- 没有 return 的函数返回 None
- 类型注解（可选，不影响运行）：  def add(a: int, b: int) -> int:

运行测试：  pytest tests/test_ex06_functions.py
"""


def make_greeting(name, greeting="你好", punctuation="！"):
    """使用默认参数。

    >>> make_greeting("小红")
    '你好，小红！'
    >>> make_greeting("Tom", greeting="Hi", punctuation="?")
    'Hi，Tom?'
    """
    return f"{greeting}，{name}{punctuation}"


def average(*nums):
    """接收任意个数字返回平均值；没有参数时返回 0.0。

    >>> average(1, 2, 3, 4)
    2.5
    """
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def build_profile(name, **info):
    """返回一个字典，包含 name 以及所有额外的关键字参数。

    >>> build_profile("Tom", age=20, city="北京")
    {'name': 'Tom', 'age': 20, 'city': '北京'}
    """
    return {"name": name, **info}


def apply_n_times(func, n, x):
    """把函数 func 连续作用在 x 上 n 次。

    >>> apply_n_times(lambda v: v * 2, 3, 1)
    8
    """
    for _ in range(n):
        x = func(x)
    return x


def compose(*funcs):
    """函数组合：compose(f, g, h)(x) == f(g(h(x)))。没有函数时返回恒等函数。

    >>> inc = lambda x: x + 1
    >>> dbl = lambda x: x * 2
    >>> compose(inc, dbl)(5)
    11
    """
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed


def make_counter(start=0):
    """返回一个计数器函数，每调用一次返回值 +1。提示：nonlocal

    >>> c = make_counter()
    >>> c(), c(), c()
    (1, 2, 3)
    """
    count = start

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def sort_by_length(words):
    """按长度排序，长度相同按字母顺序。使用 lambda 作为 key。

    >>> sort_by_length(["pear", "fig", "apple", "kiwi"])
    ['fig', 'kiwi', 'pear', 'apple']
    """
    return sorted(words, key=lambda w: (len(w), w))


def append_item(item, items=None):
    """把 item 加入列表并返回列表。不传 items 时每次都应该得到一个新列表。
    （避开“可变默认参数”陷阱）

    >>> append_item(1)
    [1]
    >>> append_item(2)
    [2]
    """
    if items is None:
        items = []
    items.append(item)
    return items


def format_record(name, *, sep=": ", upper=False):
    """sep 和 upper 是“仅限关键字参数”（参数列表中的 * 之后）。

    >>> format_record("id", sep="=")
    'id=?'
    >>> format_record("id", upper=True)
    'ID: ?'
    """
    key = name.upper() if upper else name
    return f"{key}{sep}?"
