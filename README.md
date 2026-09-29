# Python 练习册：从 JS 到 Python、数据分析与爬虫

这是一个**用练习题学 Python** 的项目，写给已经有 JavaScript 基础的人。

- 每道练习是一个 `.py` 文件，里面有**知识点讲解（附 JS 对比）**和一组待实现的函数
- 每个函数的 docstring（函数下面的三引号字符串）写着题目要求和示例
- 你的任务：把 `raise NotImplementedError` 换成自己写的代码，然后用测试检查对不对
- 一共 **22 个练习、235 个测试**，分 4 个阶段：基础语法 → 进阶 → 数据处理 → 爬虫

```
第一阶段：Python 基础语法
  ✅ ex01_basics                      ██████████  26/26
  🚧 ex02_strings                     ████         5/13
  ⬜ ex03_lists_tuples                             0/9
  ...
总进度：31/235 个测试通过（13%）
```

---

## 1. 环境准备

需要 **Python 3.10 及以上**（用到了 `match` 语句和 `X | None` 类型写法）。

```bash
# 克隆项目后进入目录
cd learn-python

# 创建虚拟环境（相当于给这个项目单独准备一个 node_modules）
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 安装依赖（相当于 npm install）
pip install -r requirements.txt

# 用参考答案跑一遍测试，确认环境没问题（应该全部 ✅）
python check.py --solutions
```

| npm / Node          | Python                            |
|---------------------|-----------------------------------|
| `package.json`      | `requirements.txt` / `pyproject.toml` |
| `node_modules/`     | `.venv/`（虚拟环境）               |
| `npm install x`     | `pip install x`                   |
| `node app.js`       | `python app.py`                   |
| `node`（REPL）      | `python`（输入 `exit()` 退出）     |
| Jest                | pytest                            |

编辑器推荐 VS Code + Python 扩展（记得在右下角选择 `.venv` 里的解释器），或 PyCharm。

## 2. 怎么做题

1. 打开 `exercises/stage1_basics/ex01_basics.py`，先读文件顶部的知识点讲解
2. 看每个函数的 docstring，理解要求和示例
3. 删掉 `# TODO` 和 `raise NotImplementedError`，写上你的实现
4. 运行测试：

```bash
python check.py            # 查看全部进度
python check.py 1          # 只测练习 1，并显示失败详情
python check.py stage2     # 只看第二阶段

# 也可以直接用 pytest（更多选项）
pytest tests/test_ex01_basics.py                 # 测试一个练习
pytest tests/test_ex01_basics.py -k safe_int     # 只测名字包含 safe_int 的测试
pytest tests/test_ex01_basics.py -x              # 遇到第一个失败就停止
```

5. 卡住了？
   - 在终端输入 `python` 进入交互环境，随手试代码：`>>> "abc"[::-1]`
   - 用 `help(str.split)` 或 `dir(list)` 查文档
   - 在代码里 `print()` 调试，或加一行 `breakpoint()` 进入调试器（类似 JS 的 `debugger`）
   - 看测试文件 `tests/test_exXX_*.py`，测试就是最精确的需求说明
   - 实在不会再看 `solutions/` 里的参考答案——**先自己写，再对比**，收获最大

> 💡 所有练习都按顺序设计，后面的练习会用到前面的知识。建议每天 1～2 个练习。

## 3. 学习路线

### 第一阶段：Python 基础语法（`exercises/stage1_basics/`）

| #  | 练习 | 主要内容 |
|----|------|---------|
| 01 | `ex01_basics` | 变量、数字运算、类型、真值判断（和 JS 差别很大！）、类型转换 |
| 02 | `ex02_strings` | f-string、切片、字符串方法 |
| 03 | `ex03_lists_tuples` | 列表操作、排序、元组、解包 |
| 04 | `ex04_dicts_sets` | 字典、集合运算 |
| 05 | `ex05_control_flow` | if/elif、for/range/enumerate/zip、while、`match` 模式匹配 |
| 06 | `ex06_functions` | 默认参数、`*args`/`**kwargs`、lambda、闭包、可变默认参数陷阱 |
| 07 | `ex07_comprehensions` | 列表/字典/集合推导式、生成器表达式、any/all |

### 第二阶段：Python 进阶（`exercises/stage2_advanced/`）

| #  | 练习 | 主要内容 |
|----|------|---------|
| 08 | `ex08_classes` | 类、继承、`@property`、`@classmethod`、魔术方法（运算符重载） |
| 09 | `ex09_exceptions` | try/except/else/finally、自定义异常、异常链 |
| 10 | `ex10_files_json` | 文件读写、pathlib、JSON |
| 11 | `ex11_iterators_generators` | 生成器 yield、迭代器协议、惰性计算 |
| 12 | `ex12_decorators` | 闭包、装饰器、带参数的装饰器 |
| 13 | `ex13_stdlib` | collections、itertools、datetime、re 正则 |
| 14 | `ex14_dataclasses_typing` | 类型注解、`@dataclass` |

### 第三阶段：数据处理与分析（`exercises/stage3_data/`）

数据文件在 `data/`：`sales.csv`（销售订单）、`users_dirty.csv`（待清洗的用户数据）、`sales_targets.csv`。

| #  | 练习 | 主要内容 |
|----|------|---------|
| 15 | `ex15_csv_stdlib` | 不用 pandas，纯 Python 读写 CSV 并聚合（理解原理） |
| 16 | `ex16_numpy` | ndarray、向量化运算、布尔索引、广播 |
| 17 | `ex17_pandas_basics` | DataFrame 读取、选择、过滤、排序、新增列 |
| 18 | `ex18_pandas_cleaning` | 缺失值、字符串清洗、类型转换、去重、清洗流水线 |
| 19 | `ex19_pandas_analysis` | groupby 聚合、透视表、merge、环比 |

### 第四阶段：网络爬虫（`exercises/stage4_scraping/`）

为了让测试稳定、不依赖网络，网页都保存在 `data/pages/`（可以用浏览器直接打开看结构）。

| #  | 练习 | 主要内容 |
|----|------|---------|
| 20 | `ex20_html_parsing` | BeautifulSoup：find / select（CSS 选择器）、提取文本/属性/表格、urljoin |
| 21 | `ex21_requests` | requests：请求头、超时、状态码、JSON 接口、重试与指数退避、限速 |
| 22 | `ex22_book_scraper` | **综合项目**：多页图书爬虫 → pandas 分析 → 导出 Excel 友好的 CSV |

## 4. 目录结构

```
learn-python/
├── exercises/        ← 你要写代码的地方
├── tests/            ← 测试（不用改，但值得读）
├── solutions/        ← 参考答案（先自己做！）
├── data/             ← 练习用的数据和网页
├── docs/
│   └── js_vs_python.md   ← JS → Python 速查表
├── check.py          ← 进度检查器
└── requirements.txt
```

## 5. 给 JS 开发者的建议

- 先看 [`docs/js_vs_python.md`](docs/js_vs_python.md) 速查表，10 分钟建立对应关系
- **缩进就是语法**：统一用 4 个空格，别混用 Tab
- **命名风格**：变量和函数用 `snake_case`，类用 `PascalCase`，常量用 `UPPER_CASE`
- **最容易踩的坑**：
  - `[]`、`{}`、`""`、`0` 在 Python 里都是假值（JS 中 `[]` 和 `{}` 是真值）
  - `dict` 不能用 `.key` 访问，要用 `d["key"]` 或 `d.get("key")`
  - `is` 不是 `===`，比较值永远用 `==`，`is` 只用于 `x is None`
  - 函数的默认参数 `def f(x=[])` 会被所有调用共享
  - `sorted([10, 9, 1])` 按数字排序；JS 的 `[10, 9, 1].sort()` 按字符串排序
  - 整数不会溢出，`2 ** 100` 可以直接算
- 多写“Pythonic”的代码：推导式、解包、`enumerate`、`zip`、`with`
- 在交互环境中输入 `import this` 读一读《Python 之禅》

## 6. 完成之后：进阶方向

**数据分析**
- 可视化：学习 `matplotlib` / `seaborn`，把练习 19 的结果画成柱状图、折线图
- 使用 Jupyter Notebook（`pip install jupyterlab`）做交互式分析
- 找真实数据集练手：Kaggle、国家统计局、天池
- 进一步：`openpyxl` 读写 Excel、`SQLAlchemy` 连接数据库、`polars`（更快的 DataFrame）

**爬虫**
- 把练习 22 的 `fetch` 换成真实请求，去爬 <https://books.toscrape.com/> 或 <https://quotes.toscrape.com/>（专门用来练习爬虫的网站）
- 动态渲染的页面（数据由 JS 加载）：先在浏览器 F12 的 Network 面板找接口直接请求 JSON；不行再用 `playwright`
- 大规模爬取：`Scrapy` 框架；异步请求：`httpx` + `asyncio`
- ⚠️ 爬虫礼仪与法律：遵守 robots.txt 和网站条款，控制频率，不抓取个人隐私和受保护的数据

**工程化**
- 代码风格检查：`ruff`；类型检查：`mypy`
- 包管理：`uv` 或 `poetry`（类似 pnpm）
- Web 后端：`FastAPI`（你的 JS 经验会很有帮助）

## 常见问题

**Q: 运行测试报 `ModuleNotFoundError: No module named 'exercises'`？**
请在项目根目录（`learn-python/`）下运行命令。

**Q: 读写文件时中文乱码 / `UnicodeDecodeError`？**
`open()` 时加上 `encoding="utf-8"`（Windows 默认编码不是 UTF-8）。

**Q: 我想重新做某个练习？**
`git checkout exercises/stage1_basics/ex01_basics.py` 可以恢复到初始状态。建议每完成一个练习就 `git commit` 一次，记录学习轨迹。
