import pytest

from tests.utils import load

ex = load("stage2_advanced.ex09_exceptions")


def test_safe_divide():
    assert ex.safe_divide(6, 3) == 2.0
    assert ex.safe_divide(1, 0) is None


def test_parse_age():
    assert ex.parse_age(" 18 ") == 18
    with pytest.raises(ValueError, match="年龄必须是整数: abc"):
        ex.parse_age("abc")
    with pytest.raises(ValueError, match="年龄超出范围: 200"):
        ex.parse_age("200")
    with pytest.raises(ValueError, match="年龄超出范围: -1"):
        ex.parse_age("-1")


def test_insufficient_funds_error():
    e = ex.InsufficientFundsError(100, 150)
    assert isinstance(e, Exception)
    assert (e.balance, e.amount, e.shortfall) == (100, 150, 50)
    assert str(e) == "余额不足：还差 50 元"


def test_withdraw():
    assert ex.withdraw(100, 30) == 70
    with pytest.raises(ex.InsufficientFundsError) as info:
        ex.withdraw(100, 130)
    assert info.value.shortfall == 30


def test_parse_records():
    lines = ["Tom,20", "bad", "Amy,x", "Bob, 30", "Old,999"]
    records, errors = ex.parse_records(lines)
    assert records == [{"name": "Tom", "age": 20}, {"name": "Bob", "age": 30}]
    assert errors == [(2, "格式错误"), (3, "年龄必须是整数: x"), (5, "年龄超出范围: 999")]


def test_retry_eventually_succeeds():
    attempts = []

    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ConnectionError("网络错误")
        return "ok"

    assert ex.retry(flaky, times=3) == "ok"
    assert len(attempts) == 3


def test_retry_gives_up():
    attempts = []

    def always_fail():
        attempts.append(1)
        raise TimeoutError(f"第 {len(attempts)} 次超时")

    with pytest.raises(TimeoutError, match="第 2 次超时"):
        ex.retry(always_fail, times=2)
    assert len(attempts) == 2


def test_get_config():
    assert ex.get_config({"host": "localhost"}, "host") == "localhost"
    with pytest.raises(ex.ConfigError, match="缺少配置项: port") as info:
        ex.get_config({}, "port")
    assert isinstance(info.value.__cause__, KeyError)


def test_cleanup_demo():
    assert ex.cleanup_demo([]) == ["try", "except", "finally"]
