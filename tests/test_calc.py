import pytest

from calc import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1.5) == pytest.approx(0.5)


def test_subtract() -> None:
    assert subtract(10, 7) == 3


def test_multiply() -> None:
    assert multiply(4, 2.5) == 10


def test_divide() -> None:
    assert divide(9, 3) == 3


def test_divide_by_zero_raises() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
