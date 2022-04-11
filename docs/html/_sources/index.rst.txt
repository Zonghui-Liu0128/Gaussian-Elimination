#######
mpm_la
#######

A Gaussian Elimination routine
------------------------------

This package implements Gaussian elimination [1]_ for :obj:`numpy.ndarray` objects, along with hand-written matrix multiplication.

See :func:`mpm_la.gauss` and :func:`mpm_la.gauss.matmul` for more information.

.. automodule:: mpm_la
  :members: gauss

.. automodule:: mpm_la.gauss
  :members: matmul, zeromat
  :noindex: gauss



Another Algorithm to Compute the Determinant
------------------------------

This package also implements another algorithm for :obj:`numpy.ndarray` objects, to compute the determinant of a single square matrix.

See :func:`mpm_la.det` for more information.

.. automodule:: mpm_la
  :members: det

.. automodule:: mpm_la.det
  :members: det
  :noindex: det

.. rubric:: References
.. [1] https://mathworld.wolfram.com/GaussianElimination.html

