"""
练习 04：字典 dict 与集合 set
============================

知识点 & 与 JS 的对比
--------------------
- dict 类似 JS 的对象 / Map：  user = {"name": "Tom", "age": 20}
      user["name"]                 # 取值，key 不存在会抛 KeyError
      user.get("email")            # 不存在返回 None（类似 JS 的 user.email 得到 undefined）
      user.get("email", "无")      # 带默认值
      user["age"] = 21             # 修改 / 新增
      del user["age"]              # 删除
      "name" in user               # 判断 key 是否存在
      user.keys() / user.values() / user.items()
      for key, value in user.items(): ...   # 类似 Object.entries
      {**a, **b}  或  a | b         # 合并（类似 JS 的 {...a, ...b}）
      d.setdefault(k, []).append(x) # 不存在就先设置默认值
- 注意：dict 的 key 必须用引号（除非是变量）；不能用 user.name 访问
- set 是无重复元素的集合：  s = {1, 2, 3}；空集合必须写 set()（{} 是空字典）
      s.add(x)  s.remove(x)  s.discard(x)
      a | b 并集   a & b 交集   a - b 差集   a ^ b 对称差

运行测试：  pytest tests/test_ex04_dicts_sets.py
"""


def word_count(text):
    """统计每个单词出现的次数（按空白切分，转小写）。

    >>> word_count("the cat and The dog")
    {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def invert_dict(d):
    """交换字典的键和值。

    >>> invert_dict({"a": 1, "b": 2})
    {1: 'a', 2: 'b'}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def merge_counts(a, b):
    """合并两个“计数字典”，相同的 key 数值相加，返回新字典（不修改原字典）。

    >>> merge_counts({"x": 1, "y": 2}, {"y": 3, "z": 4})
    {'x': 1, 'y': 5, 'z': 4}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def group_by_first_letter(words):
    """按首字母（小写）分组，组内保持原顺序。

    >>> group_by_first_letter(["apple", "Banana", "avocado", "blueberry"])
    {'a': ['apple', 'avocado'], 'b': ['Banana', 'blueberry']}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def common_elements(a, b):
    """返回两个列表的公共元素，去重并升序排列。提示：集合交集 &

    >>> common_elements([1, 2, 2, 3, 5], [2, 3, 4, 3])
    [2, 3]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def get_nested(data, path, default=None):
    """按点号路径读取嵌套字典的值，任何一层不存在就返回 default。

    >>> get_nested({"a": {"b": {"c": 42}}}, "a.b.c")
    42
    >>> get_nested({"a": {}}, "a.x.y", "N/A")
    'N/A'
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def unique_visitors(*days):
    """每个参数是一天的访客列表，返回 (所有不重复访客数, 每天都来的访客集合)。

    >>> unique_visitors(["a", "b"], ["b", "c"], ["b", "a"])
    (3, {'b'})
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def sort_dict_by_value(d, reverse=True):
    """按值排序，返回 (key, value) 列表，默认从大到小。

    >>> sort_dict_by_value({"a": 1, "b": 3, "c": 2})
    [('b', 3), ('c', 2), ('a', 1)]
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError
