from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Adds two decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtracts the second decimal number from the first."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiplies two decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Divides the first decimal number by the second. Raises an error for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sigma(n: int) -> int:
    """Returns the sum of numbers from 1 to n (sigma notation)."""
    if n <= 0:
        raise ValueError("Please enter an integer greater than 0")
    return n * (n + 1) // 2
