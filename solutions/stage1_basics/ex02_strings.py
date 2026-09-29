"""
练习 02：字符串
==============

知识点 & 与 JS 的对比
--------------------
- 单引号双引号等价；三个引号（三个单引号或三个双引号）包裹可以写多行字符串
- f-string（相当于 JS 模板字符串 `${}`）：
      name = "Tom";  f"hello {name}, {1 + 1}"
      格式化：f"{3.14159:.2f}" -> '3.14'，f"{1234567:,}" -> '1,234,567'
- 长度：len(s)（不是 s.length）
- 切片（非常常用！）：s[start:stop:step]
      s[0]  s[-1]（最后一个字符）  s[1:4]  s[::-1]（反转）
- 常用方法：
      s.upper() s.lower() s.title() s.strip() s.split(",") ",".join(lst)
      s.replace(a, b) s.startswith(x) s.endswith(x) s.find(x) s.count(x)
      s.isdigit() s.isalpha() s.isalnum()
- 包含判断：  "py" in "python"   （JS 用 includes）
- 字符串不可变，所有方法都返回新字符串
- 字符串可以直接遍历：for ch in s: ...

运行测试：  pytest tests/test_ex02_strings.py
"""


def greet(name, age):
    """用 f-string 返回问候语。

    >>> greet("小明", 18)
    '你好，小明！明年你就 19 岁了。'
    """
    return f"你好，{name}！明年你就 {age + 1} 岁了。"


def reverse_string(s):
    """反转字符串。提示：切片 s[::-1]

    >>> reverse_string("abc")
    'cba'
    """
    return s[::-1]


def is_palindrome(s):
    """判断是否为回文：忽略大小写，并且只考虑字母和数字。

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("hello")
    False
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """统计英文元音字母 a e i o u 的个数（不区分大小写）。

    >>> count_vowels("Hello World")
    3
    """
    return sum(1 for ch in s.lower() if ch in "aeiou")


def mask_phone(phone):
    """把 11 位手机号中间 4 位替换为 ****。

    >>> mask_phone("13812345678")
    '138****5678'
    """
    return phone[:3] + "****" + phone[-4:]


def format_price(amount):
    """格式化金额：加上 ¥ 符号、千分位逗号、保留两位小数。

    >>> format_price(1234.5)
    '¥1,234.50'
    """
    return f"¥{amount:,.2f}"


def split_and_strip(line):
    """按逗号切分字符串，去掉每一项两侧空白，并丢弃空项。

    >>> split_and_strip(" apple, banana ,, cherry ")
    ['apple', 'banana', 'cherry']
    """
    return [part.strip() for part in line.split(",") if part.strip()]


def to_snake_case(name):
    """把驼峰命名转换成 Python 风格的下划线命名。

    >>> to_snake_case("getUserName")
    'get_user_name'
    >>> to_snake_case("UserName")
    'user_name'
    """
    result = ""
    for i, ch in enumerate(name):
        if ch.isupper():
            if i > 0:
                result += "_"
            result += ch.lower()
        else:
            result += ch
    return result


def center_title(title, width=20, fill="="):
    """把标题居中，两边用 fill 填充到 width 宽度。提示：str.center

    >>> center_title("Menu", 10)
    '===Menu==='
    """
    return title.center(width, fill)
