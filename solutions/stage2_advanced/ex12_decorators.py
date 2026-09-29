"""
练习 12：闭包与装饰器
====================

知识点
------
- 装饰器本质：一个“接收函数、返回新函数”的高阶函数
      def my_decorator(func):
          @functools.wraps(func)          # 保留原函数的 __name__ / __doc__
          def wrapper(*args, **kwargs):
              print("before")
              result = func(*args, **kwargs)
              print("after")
              return result
          return wrapper

      @my_decorator        # 等价于 say = my_decorator(say)
      def say(): ...
- 带参数的装饰器需要再套一层：
      def repeat(times):
          def decorator(func):
              @functools.wraps(func)
              def wrapper(*args, **kwargs): ...
              return wrapper
          return decorator

      @repeat(3)
      def hi(): ...
- JS 中类似于手写高阶函数 const logged = withLog(fn)（Python 只是多了 @ 语法糖）
- 标准库里的装饰器：@functools.lru_cache / @functools.cache、@property、@staticmethod、
  @dataclass ……

运行测试：  pytest tests/test_ex12_decorators.py
"""
import functools


def make_multiplier(n):
    """返回一个函数，把参数乘以 n。

    >>> triple = make_multiplier(3)
    >>> triple(5)
    15
    """
    def multiply(x):
        return x * n
    return multiply


def count_calls(func):
    """装饰器：统计函数被调用次数，存在 wrapper.calls 属性中（初始为 0）。
    记得使用 functools.wraps。

    >>> @count_calls
    ... def f(): pass
    >>> f(); f()
    >>> f.calls
    2
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def memoize(func):
    """装饰器：缓存函数结果（参数都是可哈希的位置参数）。
    缓存字典暴露为 wrapper.cache，key 是参数元组。
    （实际项目直接用 functools.lru_cache，这里练习手写。）
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper


def repeat(times):
    """带参数的装饰器：把函数执行 times 次，返回所有结果组成的列表。

    >>> @repeat(3)
    ... def hi(): return "hi"
    >>> hi()
    ['hi', 'hi', 'hi']
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


def validate_positive(func):
    """装饰器：如果任何位置参数或关键字参数是负数（int/float），抛出 ValueError。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for value in (*args, *kwargs.values()):
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"参数不能为负数: {value}")
        return func(*args, **kwargs)
    return wrapper


def log_calls(log):
    """带参数的装饰器：每次调用后向 log 列表追加字符串 "函数名(参数) -> 结果"。
    参数格式：位置参数用 repr，关键字参数写成 k=repr(v)，用 ", " 连接。

    >>> logs = []
    >>> @log_calls(logs)
    ... def add(a, b=0): return a + b
    >>> add(1, b=2)
    3
    >>> logs
    ['add(1, b=2) -> 3']
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            parts = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
            log.append(f"{func.__name__}({', '.join(parts)}) -> {result!r}")
            return result
        return wrapper
    return decorator
