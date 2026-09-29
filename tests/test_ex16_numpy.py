import numpy as np
import pytest

from tests.utils import load

ex = load("stage3_data.ex16_numpy")


def test_create_grid():
    g = ex.create_grid(2, 3)
    assert isinstance(g, np.ndarray)
    assert g.shape == (2, 3)
    assert g.tolist() == [[0, 1, 2], [3, 4, 5]]


def test_normalize():
    result = ex.normalize([10, 20, 30])
    assert isinstance(result, np.ndarray)
    np.testing.assert_allclose(result, [0, 0.5, 1])
    np.testing.assert_allclose(ex.normalize([5, 5, 5]), [0, 0, 0])


def test_moving_average():
    np.testing.assert_allclose(ex.moving_average([1, 2, 3, 4, 5], 3), [2, 3, 4])
    np.testing.assert_allclose(ex.moving_average([2, 4], 1), [2, 4])


def test_filter_outliers():
    data = [10, 11, 9, 10, 12, 10, 100]
    result = ex.filter_outliers(data, k=2)
    assert 100 not in result
    assert len(result) == 6


def test_matrix_stats():
    m = [[1, 2, 3], [4, 9, 6]]
    stats = ex.matrix_stats(m)
    assert stats["row_sums"] == [6, 19]
    assert stats["col_means"] == pytest.approx([2.5, 5.5, 4.5])
    assert stats["max_pos"] == (1, 1)


def test_one_hot():
    result = ex.one_hot([0, 2, 1], 3)
    assert result.tolist() == [[1, 0, 0], [0, 0, 1], [0, 1, 0]]


def test_distances_from_origin():
    np.testing.assert_allclose(ex.distances_from_origin([[3, 4], [0, 0], [1, 1]]), [5, 0, np.sqrt(2)])


def test_apply_discount():
    np.testing.assert_allclose(ex.apply_discount([50, 100, 200], 100, 0.8), [50, 80, 160])


def test_standardize_columns():
    m = np.array([[1, 10], [2, 20], [3, 30]])
    z = ex.standardize_columns(m)
    np.testing.assert_allclose(z.mean(axis=0), [0, 0], atol=1e-12)
    np.testing.assert_allclose(z.std(axis=0), [1, 1])
