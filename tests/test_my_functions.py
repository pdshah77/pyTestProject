import pytest
import source.myFunctions as functions
import time


def test_add():
    assert functions.add(1.5, 2) == 3.5, "Addition Code is not working"


def test_add_strings():
    assert functions.add("PyTest", " is Fun") == "PyTest is Fun"


def test_divide():
    assert functions.divide(10, 5) == 2, "Division not working"


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    assert functions.add(1.5, 2) == 3.5, "Addition Code is not working"


@pytest.mark.skip(reason="Defect DE123 Raised")
def test_defect_skipped():
    pass


@pytest.mark.xfail(reason="We cannot divide by Zero")
def test_divide_zero_broken():
    functions.divide(3,0)
