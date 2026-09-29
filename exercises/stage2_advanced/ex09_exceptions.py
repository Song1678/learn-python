"""
练习 09：异常处理
================

知识点 & 与 JS 的对比
--------------------
    JS                              Python
    try { ... }                     try:
    catch (e) { ... }               except ValueError as e:
                                    except (KeyError, IndexError):
                                    else:        # 没有异常时执行
    finally { ... }                 finally:
    throw new Error("x")            raise ValueError("x")

- 常见内置异常：ValueError, TypeError, KeyError, IndexError, ZeroDivisionError,
  FileNotFoundError, AttributeError
- 只捕获你预期的异常，不要写空的 except:（会吞掉所有错误）
- 自定义异常：继承 Exception
      class MyError(Exception):
          pass
- 异常链：  raise NewError("...") from original_error   保留原始错误信息
- 不带参数的 raise 会重新抛出当前捕获的异常
- 读取异常信息：str(e)，e.args

运行测试：  pytest tests/test_ex09_exceptions.py
"""


def safe_divide(a, b):
    """a / b，除数为 0 时返回 None。

    >>> safe_divide(6, 3)
    2.0
    >>> safe_divide(1, 0)
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def parse_age(text):
    """把字符串解析成年龄：
    - 不能转成整数时抛出 ValueError("年龄必须是整数: <text>")
    - 小于 0 或大于 150 时抛出 ValueError("年龄超出范围: <age>")

    >>> parse_age(" 18 ")
    18
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


class InsufficientFundsError(Exception):
    """自定义异常：余额不足。

    InsufficientFundsError(balance, amount) 需要：
    - 保存 self.balance 和 self.amount 属性
    - 保存 self.shortfall = amount - balance
    - 错误信息 str(e) 为 "余额不足：还差 <shortfall> 元"
      提示：调用 super().__init__(message)
    """

    def __init__(self, balance, amount):
        # TODO: 在这里写你的代码
        raise NotImplementedError


def withdraw(balance, amount):
    """返回取款后的余额；余额不足时抛出 InsufficientFundsError。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def parse_records(lines):
    """每行格式 "姓名,年龄"。返回 (有效记录列表, 错误列表)：
    - 有效记录：{"name": 姓名, "age": 年龄(int)}，年龄校验复用 parse_age
    - 错误：(行号(从1开始), 错误信息字符串)
    - 格式不对（不是恰好 2 个字段）时错误信息为 "格式错误"

    >>> parse_records(["Tom,20", "bad", "Amy,x"])[1]
    [(2, '格式错误'), (3, '年龄必须是整数: x')]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def retry(func, times=3):
    """调用 func()，出现异常就重试，最多尝试 times 次。
    成功返回结果；全部失败则重新抛出最后一次的异常。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


class ConfigError(Exception):
    """配置错误。"""


def get_config(config, key):
    """读取 config[key]。key 不存在时抛出 ConfigError(f"缺少配置项: {key}")，
    并使用 `raise ... from e` 保留原始 KeyError（测试会检查 __cause__）。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def cleanup_demo(log):
    """演示 try / except / else / finally 的执行顺序。
    依次把以下字符串追加到 log 列表：
      "try" -> 执行 int("abc") 触发异常 -> "except" -> "finally"
    然后返回 log。（思考：else 为什么没有执行？）
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError
