"""
练习 16：NumPy 基础
==================

NumPy 是 Python 数值计算的基石，pandas 底层就是它。核心是 ndarray（多维数组）。

知识点
------
    import numpy as np
    a = np.array([1, 2, 3])          np.arange(10)     np.zeros((2, 3))   np.ones(3)
    a.shape  a.dtype  a.reshape(2, 5)
- 向量化运算（不用写循环！）：  a * 2,  a + b,  a ** 2,  np.sqrt(a)
- 聚合：  a.sum()  a.mean()  a.std()  a.max()  a.argmax()
          m.sum(axis=0)  按列   m.sum(axis=1)  按行
- 布尔索引：  a[a > 5]    a[(a > 1) & (a < 5)]    （注意用 & | ~，并加括号）
- 条件选择：  np.where(cond, x, y)
- 广播：不同形状数组自动扩展，如 matrix - matrix.mean(axis=0)

对 JS 开发者：想象一个所有操作都自动 map 的数组，而且快几十倍。

运行测试：  pytest tests/test_ex16_numpy.py
"""
import numpy as np


def create_grid(rows, cols):
    """返回 rows×cols 的二维数组，内容为 0, 1, 2, ... 依次填充。

    >>> create_grid(2, 3)
    array([[0, 1, 2],
           [3, 4, 5]])
    """
    return np.arange(rows * cols).reshape(rows, cols)


def normalize(arr):
    """Min-Max 归一化到 [0, 1]：(x - min) / (max - min)。
    所有值相同时返回全 0 的 float 数组。
    """
    arr = np.asarray(arr, dtype=float)
    span = arr.max() - arr.min()
    if span == 0:
        return np.zeros_like(arr)
    return (arr - arr.min()) / span


def moving_average(arr, window):
    """简单移动平均，只返回完整窗口的结果（长度 len(arr) - window + 1）。
    提示：np.convolve(arr, np.ones(window) / window, mode="valid")，或者用 cumsum 技巧。
    """
    arr = np.asarray(arr, dtype=float)
    return np.convolve(arr, np.ones(window) / window, mode="valid")


def filter_outliers(arr, k=2.0):
    """去除离均值超过 k 个标准差的值（布尔索引）。"""
    arr = np.asarray(arr, dtype=float)
    mean, std = arr.mean(), arr.std()
    return arr[np.abs(arr - mean) <= k * std]


def matrix_stats(matrix):
    """返回 {"row_sums": 每行之和(list), "col_means": 每列均值(list), "max_pos": 最大值位置(行, 列)}
    提示：axis 参数；np.unravel_index(m.argmax(), m.shape)
    """
    m = np.asarray(matrix)
    r, c = np.unravel_index(m.argmax(), m.shape)
    return {
        "row_sums": m.sum(axis=1).tolist(),
        "col_means": m.mean(axis=0).tolist(),
        "max_pos": (int(r), int(c)),
    }


def one_hot(labels, n_classes):
    """独热编码：labels=[0, 2] n_classes=3 -> [[1,0,0],[0,0,1]]（int 数组）。
    提示：np.eye(n_classes, dtype=int)[labels]
    """
    return np.eye(n_classes, dtype=int)[np.asarray(labels)]


def distances_from_origin(points):
    """points 是形状 (N, 2) 的坐标数组，返回每个点到原点的距离数组。"""
    return np.linalg.norm(np.asarray(points, dtype=float), axis=1)


def apply_discount(prices, threshold, rate):
    """价格 >= threshold 的打 rate 折（如 0.8），其余不变。使用 np.where。"""
    prices = np.asarray(prices, dtype=float)
    return np.where(prices >= threshold, prices * rate, prices)


def standardize_columns(matrix):
    """按列标准化（z-score）：(x - 列均值) / 列标准差。利用广播，不要写循环。"""
    m = np.asarray(matrix, dtype=float)
    return (m - m.mean(axis=0)) / m.std(axis=0)
