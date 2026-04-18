"""Core calculator API operations."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def sqrt(a: float) -> float:
    """Return the square root of a number.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return a ** 0.5