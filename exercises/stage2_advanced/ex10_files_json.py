"""
练习 10：文件读写、pathlib 与 JSON
=================================

知识点 & 与 JS(Node) 的对比
-------------------------
- 用 with 打开文件，结束时自动关闭（类似 try/finally）：
      with open(path, "r", encoding="utf-8") as f:
          text = f.read()          # 全部读入
          # 或 for line in f:      # 逐行读取（省内存）
      模式："r" 读  "w" 覆盖写  "a" 追加  "rb"/"wb" 二进制
  ⚠️ 中文环境务必写 encoding="utf-8"（Windows 默认编码可能是 gbk）
- pathlib（推荐，比 os.path 更现代）：
      from pathlib import Path
      p = Path("data") / "a.txt"      # 用 / 拼接路径
      p.exists()  p.name  p.stem  p.suffix  p.parent
      p.read_text(encoding="utf-8")   p.write_text(s, encoding="utf-8")
      p.mkdir(parents=True, exist_ok=True)
      p.glob("*.txt")  p.iterdir()
- json 模块（类似 JSON.parse / JSON.stringify）：
      json.loads(s)  /  json.dumps(obj, ensure_ascii=False, indent=2)
      json.load(f)   /  json.dump(obj, f, ...)       # 直接读写文件
  ensure_ascii=False 可以让中文不被转义成 \\uXXXX

运行测试：  pytest tests/test_ex10_files_json.py
（测试使用 pytest 的 tmp_path 临时目录，不会弄乱你的项目）
"""
import json
from pathlib import Path


def write_lines(path, lines):
    """把字符串列表写入文件，每个元素一行（utf-8）。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def read_lines(path):
    """读取文件，返回去掉首尾空白后的非空行列表。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def count_words(path):
    """统计文件中的单词数（按空白切分）。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def append_log(path, message):
    """以追加模式写入一行日志 "[LOG] message"。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def save_json(path, data):
    """把数据保存为 JSON 文件：中文不转义、缩进 2 个空格。
    如果父目录不存在，需要先创建。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def load_json(path, default=None):
    """读取 JSON 文件；文件不存在时返回 default。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def list_files(folder, suffix):
    """返回文件夹中（不递归）指定后缀文件的文件名列表，按名称排序。

    >>> # list_files("docs", ".md") -> ['a.md', 'b.md']
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def update_json_counter(path, key):
    """JSON 文件中存储 {key: 次数}。把 key 的次数 +1 后写回，返回新的次数。
    文件不存在时视为空字典。（复用上面的 load_json / save_json）
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError
