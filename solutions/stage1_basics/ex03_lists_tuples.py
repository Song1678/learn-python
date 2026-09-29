"""
练习 03：列表 list 与元组 tuple
==============================

知识点 & 与 JS 的对比
--------------------
- list 相当于 JS 的 Array：  nums = [1, 2, 3]
      nums.append(4)      # push
      nums.pop()          # pop（也可 pop(0) 取第一个）
      nums.insert(0, x)   # 在指定位置插入
      nums.extend([5, 6]) # 拼接，也可以 nums + [5, 6]
      nums.remove(x)      # 删除第一个值为 x 的元素
      x in nums           # includes
      nums.index(x)       # indexOf（找不到会报错）
      len(nums)           # length
- 切片同字符串：nums[1:3]，nums[::-1]，复制列表：nums[:] 或 nums.copy()
- 排序：
      nums.sort()                 # 原地排序
      sorted(nums)                # 返回新列表
      sorted(people, key=lambda p: p[1], reverse=True)
  注意：Python 排序默认就是按数字大小，不会像 JS 那样按字符串排序！
- 常用内置函数：sum(), max(), min(), len(), sorted(), reversed(), enumerate(), zip()
- tuple 是不可变的列表：  point = (3, 4)，常用于函数返回多个值
- 解包：  a, b = (1, 2)；  first, *rest = [1, 2, 3]  （类似 JS 的 const [first, ...rest] = arr）

运行测试：  pytest tests/test_ex03_lists_tuples.py
"""


def second_largest(nums):
    """返回列表中第二大的不重复数字；如果不存在返回 None。

    >>> second_largest([3, 1, 4, 4, 2])
    3
    >>> second_largest([5, 5])
    """
    unique = sorted(set(nums), reverse=True)
    return unique[1] if len(unique) >= 2 else None


def chunk(items, size):
    """把列表按 size 分块。

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    return [items[i:i + size] for i in range(0, len(items), size)]


def flatten(nested):
    """把二层嵌套列表拍平成一层。

    >>> flatten([[1, 2], [3], [], [4, 5]])
    [1, 2, 3, 4, 5]
    """
    result = []
    for sub in nested:
        result.extend(sub)
    return result


def rotate(items, k):
    """把列表向右旋转 k 位（k 可能大于长度），返回新列表。

    >>> rotate([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    """
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else items[:]


def dedupe(items):
    """去除重复元素，保留第一次出现的顺序。

    >>> dedupe([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def min_max(nums):
    """返回 (最小值, 最大值) 元组。

    >>> min_max([3, 9, 1])
    (1, 9)
    """
    return min(nums), max(nums)


def merge_sorted(a, b):
    """合并两个已排序列表，结果仍然有序（请尝试不用 sorted 实现，练习 while 循环）。

    >>> merge_sorted([1, 4, 7], [2, 3, 8])
    [1, 2, 3, 4, 7, 8]
    """
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def sort_people(people):
    """people 是 (姓名, 年龄) 元组的列表，按年龄升序排序，年龄相同时按姓名排序。

    提示：sorted(..., key=lambda p: (p[1], p[0]))，元组可以直接比较大小。

    >>> sort_people([("Tom", 20), ("Amy", 25), ("Bob", 20)])
    [('Bob', 20), ('Tom', 20), ('Amy', 25)]
    """
    return sorted(people, key=lambda p: (p[1], p[0]))


def head_and_tail(items):
    """返回 (第一个元素, 其余元素列表)。提示：first, *rest = items

    >>> head_and_tail([1, 2, 3])
    (1, [2, 3])
    """
    first, *rest = items
    return first, rest
