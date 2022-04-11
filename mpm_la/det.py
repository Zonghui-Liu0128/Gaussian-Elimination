def det(mat):
    """
        Given one matrix, `mat`, the determinant of `mat`
        will be returned.

        Parameters
        ----------
        mat : np.array or list of lists
            'n x n' array
    """
    mat = mat.astype('float')
    columns = mat.shape[0]
    res = 1
    for col in range(columns):
        row = col
        res *= mat[row][col]
        while mat[row][col] == 0 and row < columns - 1:
            row += 1
        for i in range(row + 1, columns):
            if mat[i][col] == 0:
                pass
            else:
                lmd = - mat[i][col] / mat[row][col]
                for j in range(col, columns):
                    mat[i][j] += mat[row][j] * lmd
    return res
