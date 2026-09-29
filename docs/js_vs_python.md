# JavaScript → Python 速查表

## 基础

| JavaScript | Python | 说明 |
|---|---|---|
| `let x = 1; const Y = 2;` | `x = 1`<br>`Y = 2` | 没有声明关键字；常量靠大写命名约定 |
| `// 注释` `/* */` | `# 注释` | 多行注释通常用多个 `#` 或 docstring |
| `null` / `undefined` | `None` | |
| `true` / `false` | `True` / `False` | 首字母大写 |
| `&&` `\|\|` `!` | `and` `or` `not` | |
| `===` / `!==` | `==` / `!=` | Python 的 `==` 不做隐式类型转换 |
| `typeof x` | `type(x)` / `isinstance(x, int)` | |
| `Math.floor(7 / 2)` | `7 // 2` | 整除 |
| `Math.pow(2, 10)` / `2 ** 10` | `2 ** 10` | |
| `x++` | `x += 1` | 没有 `++` / `--` |
| `cond ? a : b` | `a if cond else b` | |
| `console.log(a, b)` | `print(a, b)` | |
| `parseInt("42")` | `int("42")` | 非法字符串会抛 `ValueError` |
| `String(42)` | `str(42)` | |
| `a ?? b` | `a if a is not None else b` | `a or b` 也常用，但会把 0 和 "" 当成假值 |

## 字符串

| JavaScript | Python |
|---|---|
| `` `Hi ${name}` `` | `f"Hi {name}"` |
| `s.length` | `len(s)` |
| `s.toUpperCase()` | `s.upper()` |
| `s.trim()` | `s.strip()` |
| `s.includes("x")` | `"x" in s` |
| `s.startsWith("x")` | `s.startswith("x")` |
| `s.split(",")` | `s.split(",")` |
| `arr.join(",")` | `",".join(arr)` |
| `s.slice(1, 3)` | `s[1:3]` |
| `s.at(-1)` | `s[-1]` |
| `s.replaceAll("a", "b")` | `s.replace("a", "b")`（默认替换全部） |
| `s.padStart(5, "0")` | `s.zfill(5)` / `s.rjust(5, "0")` / `f"{n:05d}"` |
| `s.split("").reverse().join("")` | `s[::-1]` |

## 数组 → 列表 list

| JavaScript | Python |
|---|---|
| `arr.length` | `len(arr)` |
| `arr.push(x)` | `arr.append(x)` |
| `arr.pop()` / `arr.shift()` | `arr.pop()` / `arr.pop(0)` |
| `arr.unshift(x)` | `arr.insert(0, x)` |
| `[...a, ...b]` | `[*a, *b]` 或 `a + b` |
| `arr.includes(x)` | `x in arr` |
| `arr.indexOf(x)` | `arr.index(x)`（找不到会抛异常） |
| `arr.slice()` | `arr[:]` / `arr.copy()` |
| `arr.map(x => x * 2)` | `[x * 2 for x in arr]` |
| `arr.filter(x => x > 0)` | `[x for x in arr if x > 0]` |
| `arr.reduce((s, x) => s + x, 0)` | `sum(arr)`（通用：`functools.reduce`） |
| `arr.some(x => x > 0)` | `any(x > 0 for x in arr)` |
| `arr.every(x => x > 0)` | `all(x > 0 for x in arr)` |
| `arr.find(x => x > 0)` | `next((x for x in arr if x > 0), None)` |
| `arr.sort((a, b) => a - b)` | `arr.sort()` 或 `sorted(arr)` |
| `arr.sort((a, b) => a.age - b.age)` | `sorted(arr, key=lambda p: p["age"])` |
| `arr.forEach((x, i) => ...)` | `for i, x in enumerate(arr): ...` |
| `Array.from({length: 5}, (_, i) => i)` | `list(range(5))` |
| `const [a, ...rest] = arr` | `a, *rest = arr` |
| `arr.flat()` | `[x for sub in arr for x in sub]` |
| `Math.max(...arr)` | `max(arr)` |

## 对象 → 字典 dict

| JavaScript | Python |
|---|---|
| `{name: "Tom"}` | `{"name": "Tom"}`（key 要加引号） |
| `obj.name` / `obj["name"]` | `d["name"]` |
| `obj.email ?? "无"` | `d.get("email", "无")` |
| `"name" in obj` | `"name" in d` |
| `delete obj.name` | `del d["name"]` / `d.pop("name")` |
| `Object.keys(obj)` | `d.keys()` / `list(d)` |
| `Object.values(obj)` | `d.values()` |
| `Object.entries(obj)` | `d.items()` |
| `{...a, ...b}` | `{**a, **b}` 或 `a \| b` |
| `const {name, age} = obj` | `name, age = d["name"], d["age"]` |
| `JSON.stringify(obj)` | `json.dumps(d, ensure_ascii=False)` |
| `JSON.parse(s)` | `json.loads(s)` |
| `new Set([1, 2])` | `{1, 2}` / `set([1, 2])` |
| `new Map()` | `dict()`（Python 的 dict 可以用任意可哈希值做 key） |

## 流程控制

```js
// JavaScript
if (x > 0) {
  console.log("正");
} else if (x === 0) {
  console.log("零");
} else {
  console.log("负");
}

for (let i = 0; i < 5; i++) { }
for (const item of items) { }
for (const [key, value] of Object.entries(obj)) { }

switch (cmd) {
  case "a": ...; break;
  default: ...
}
```

```python
# Python
if x > 0:
    print("正")
elif x == 0:
    print("零")
else:
    print("负")

for i in range(5): ...
for item in items: ...
for key, value in d.items(): ...

match cmd:
    case "a":
        ...
    case _:
        ...
```

## 函数

```js
function greet(name, greeting = "Hi") { return `${greeting}, ${name}`; }
const add = (a, b) => a + b;
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
function f({ verbose = false } = {}) { }
```

```python
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}"

add = lambda a, b: a + b          # lambda 只能写一个表达式，复杂逻辑请用 def

def total(*nums):
    return sum(nums)

def f(*, verbose=False):          # 仅限关键字参数：f(verbose=True)
    ...
```

## 类

```js
class Dog extends Animal {
  static count = 0;
  constructor(name) { super(name); this.name = name; }
  get upperName() { return this.name.toUpperCase(); }
  bark() { return `${this.name}: 汪`; }
  toString() { return `Dog(${this.name})`; }
}
const d = new Dog("旺财");
```

```python
class Dog(Animal):
    count = 0                              # 类属性

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    @property
    def upper_name(self):
        return self.name.upper()

    def bark(self):
        return f"{self.name}: 汪"

    def __str__(self):
        return f"Dog({self.name})"

d = Dog("旺财")                            # 不需要 new
```

## 异常

| JavaScript | Python |
|---|---|
| `try { } catch (e) { } finally { }` | `try: ... except ValueError as e: ... finally: ...` |
| `throw new Error("x")` | `raise ValueError("x")` |
| `class MyError extends Error {}` | `class MyError(Exception): pass` |
| `e.message` | `str(e)` |

## 模块

| JavaScript | Python |
|---|---|
| `import fs from "fs"` | `import os` |
| `import { join } from "path"` | `from os.path import join` |
| `import * as np from "numpy"`（假想） | `import numpy as np` |
| `export function f() {}` | 不需要 export，文件里定义的名字都可以被导入 |
| `if (require.main === module)` | `if __name__ == "__main__":` |

## 异步（了解即可）

| JavaScript | Python |
|---|---|
| `async function f() { await g(); }` | `async def f(): await g()` |
| `Promise.all([a(), b()])` | `await asyncio.gather(a(), b())` |
| 运行：事件循环自动存在 | `asyncio.run(main())` |
| `fetch(url)` | `httpx.AsyncClient().get(url)`（第三方库） |

> 和 JS 不同，Python 大部分代码是同步的，爬虫和数据处理入门阶段用同步代码就够了。
