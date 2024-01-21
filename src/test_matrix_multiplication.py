from numpy.testing import assert_array_equal
from unittest import TestCase
from matrix_multiplication import MatrixMultiplication
import numpy as np


class TestMatrixMultiplication(TestCase):
    def test_small(self):
        # given
        x = np.array([[1, 2, 3, 4],
                      [4, 3, 0, 1],
                      [5, 6, 1, 1],
                      [0, 2, 5, 6]])
        y = np.array([[1, 0, 5, 1],
                      [1, 2, 0, 2],
                      [0, 3, 2, 3],
                      [1, 2, 1, 2]])

        expected_result = np.array([[7, 21, 15, 22],
                                    [8, 8, 21, 12],
                                    [12, 17, 28, 22],
                                    [8, 31, 16, 31]])
        # when
        result = MatrixMultiplication().multiply(x, y)
        # then
        assert_array_equal(result, expected_result)
