import doctest


def test_docstrings():
    res = doctest.testfile("gauss.py", package="mpm_la", name="gauss")
    assert res.failed == 0
    res1 = doctest.testfile("det.py", package="mpm_la", name="det")
    assert res1.failed == 0
