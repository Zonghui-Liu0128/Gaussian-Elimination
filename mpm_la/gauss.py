import copy

__all__ = ['gauss', 'matmul', 'zeromat']


def gauss(a, b):
    """
    Given two matrices, `a` and `b`, with `a` square, the determinant
    of `a` and a matrix `x` such that a*x = b are returned.
    If `b` is the identity, then `x` is the inverse of `a`.

    Parameters
    ----------
    a : np.array or list of lists
        'n x n' array
    b : np. array or list of lists
        'm x n' array

    Examples
    --------
    >>> from mpm_la import gauss
    >>> a=[[2,0,-1],[0,5,6],[0,-1,1]]
    >>> b=[[2],[1],[2]]
    >>> det,x=gauss(a,b)
    >>> det
    22.0
    >>> x
    [[1.5], [-1.0], [1.0]]
    >>> from mpm_la import gauss
    >>> A=[[1,0,-1],[-2,3,0],[1,-3,2]]
    >>> I=[[1,0,0],[0,1,0],[0,0,1]]
    >>> Det,Ainv=gauss(A, I)
    >>> Det
    3.0

    Notes
    -----
        See https://en.wikipedia.org/wiki/Gaussian_elimination \
        for further details.
    """
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    # 获得方程的个数
    n = len(a)
    p = len(b[0])
    det = 1.
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b


def matmul(a, b):
    """
        Given two matrices, `a` and `b`. First, determine the shape \
        of the result matrix after multiplication
        according to the shapes of the matrices a and b, and generate \
        a zero matrix of the corresponding shape.
        Next, complete the matrix multiplication and return the result matrix.

        Parameters
        ----------
        a : np.array or list of lists
        'n x n' array
        b : np. array or list of lists
        'm x n' array

        Examples
        --------
        >>> from mpm_la import matmul
        >>> a=[[1,2],[3,4]]
        >>> b=[[5],[6]]
        >>> res_mul=matmul(a,b)
        >>> res_mul
        [[17], [39]]

        >>> from mpm_la import matmul
        >>> a=[[1,2],[3,4]]
        >>> b=[[5,1],[6,2]]
        >>> mul=matmul(a,b)
        >>> mul
        [[17, 5], [39, 11]]

        """
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Incompatible dimensions")
    c = zeromat(n, q)
    for i in range(n):
        for j in range(q):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(p))
    return c


def zeromat(p, q):
    """
        Given two integers, `p` and `q`. `p` is the \
        number of rows in the first matrix,
        and `q` is the number of columns in the second matrix. \
        The function will return a matrix with all zero values.
        The shape of the returned matrix is the same as the shape \
        as a result of multiplying two matrices.

        Parameters
        ----------
        p : Integer
        q : Integer

        Examples
        --------
        >>> from mpm_la import zeromat
        >>> p = 3
        >>> q = 1
        >>> res_zero = zeromat(p, q)
        >>> res_zero
        [[0], [0], [0]]


        >>> from mpm_la import zeromat
        >>> p = 4
        >>> q = 4
        >>> res_zero = zeromat(p, q)
        >>> res_zero
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        """
    return [[0] * q for i in range(p)]
