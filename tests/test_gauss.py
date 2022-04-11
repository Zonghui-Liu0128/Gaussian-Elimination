import numpy as np
import pytest

from mpm_la import gauss, matmul, zeromat


class TestGauss(object):
    """
    Class for testing the Gaussian elimination algorithm Gauss
    and its associated functions.
    """

    @pytest.mark.parametrize('a, b, dete, xe, a1, '
                             'b1, dete1, xe1, a2, b2, dete2, xe2', [
                                 ([[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                                  [[1, 0, 0], [0, 1, 0], [0, 0, 1]], -360.0,
                                  [[-0.10277777777777776, 0.18888888888888888,
                                    -0.019444444444444438],
                                   [0.10555555555555554, 0.02222222222222223,
                                    -0.061111111111111116],
                                   [0.0638888888888889, -0.14444444444444446,
                                    0.14722222222222223]],
                                  [[1, 2, 1], [3, 8, 1], [0, 4, 1]],
                                  [[2, 3, 4], [5, 3, 2], [3, 4, 2]], 10.0,
                                  [[0.0, -0.6000000000000001, 0.8],
                                   [0.5, 0.20000000000000007,
                                    -0.6000000000000001],
                                   [1.0, 3.1999999999999997, 4.4]],
                                  [[3.5, 4, 5.5], [6, 7.5, 8],
                                   [9.5, 10, 11.5]],
                                  [[2.5, 3, 4.5], [5, 6.5, 7], [8.5, 9, 10.5]],
                                  -12.000000000000002,
                                  [[1.4999999999999993, 0.4999999999999994,
                                    0.49999999999999967],
                                   [1.8750433304780424e-16, 1.0000000000000002,
                                    4.2188474935755956e-16],
                                   [-0.49999999999999967, -0.49999999999999967,
                                    0.4999999999999999]]
                                  )
                             ])
    def test_gauss(self, a, b, dete, xe, a1,
                   b1, dete1, xe1, a2, b2, dete2, xe2):
        """ Test the gauss function """
        det, x = gauss(a, b)
        det1, x1 = gauss(a1, b1)
        det2, x2 = gauss(a2, b2)

        assert np.isclose(det, dete)
        assert np.allclose(x, xe)
        assert np.isclose(det1, dete1)
        assert np.allclose(x1, xe1)
        assert np.isclose(det2, dete2)
        assert np.allclose(x2, xe2)

    @pytest.mark.parametrize('a, b, mule, a1, b1, mule1, a2, b2, mule2', [
        ([[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[1, 2, 1], [3, 8, 1], [0, 4, 1]],
         [[2, 3, 4], [5, 3, 2], [3, 4, 2]],
         [[15, 13, 10], [49, 37, 30], [23, 16, 10]],
         [[3.5, 4, 5.5], [6, 7.5, 8], [9.5, 10, 11.5]],
         [[2.5, 3, 4.5], [5, 6.5, 7], [8.5, 9, 10.5]],
         [[75.5, 86.0, 101.5], [120.5, 138.75, 163.5], [171.5, 197.0, 233.5]]
         )
    ])
    def test_matmul(self, a, b, mule, a1, b1, mule1, a2, b2, mule2):
        mul = matmul(a, b)
        mul1 = matmul(a1, b1)
        mul2 = matmul(a2, b2)

        assert np.allclose(mul, mule)
        assert np.allclose(mul1, mule1)
        assert np.allclose(mul2, mule2)

    @pytest.mark.parametrize('a, b, zere, a1, b1, zere1',
                             [([[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                               [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                               [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                               [[2, 9], [7, 5]],
                               [[1, 0], [0, 1]],
                               [[0, 0], [0, 0]])
                              ])
    def test_zeromat(self, a, b, zere, a1, b1, zere1):
        zer = zeromat(len(a), len(b[0]))
        zer1 = zeromat(len(a1), len(b1[0]))

        assert np.allclose(zer, zere)
        assert np.allclose(zer1, zere1)
