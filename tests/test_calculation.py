'''Test calculation operations and behaviors.'''

# Import necessary modules for testing and arithmetic.
from decimal import Decimal
import pytest
from calculator.calculation import SingleInpCalculation, DualInpCalculation
from calculator.operations import add, subtract, multiply, divide, sigma

# Parameterize multiple test cases for arithmetic operations.
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculation_operations(a, b, operation, expected):
    """Test various dual-input calculations."""
    calc = DualInpCalculation(a, b, operation)
    assert calc.evaluate() == expected, f"Failed {operation.__name__} with {a} and {b}"

def test_calculation_repr():
    """Test string representation of calculation objects."""
    calc = DualInpCalculation(Decimal('10'), Decimal('5'), add)
    assert repr(calc) == "DualInpCalculation(10, 5, add)"
    
    calc = SingleInpCalculation(int(5), sigma)
    assert repr(calc) == "SingleInpCalculation(5, sigma)"

def test_divide_by_zero():
    """Test handling of division by zero."""
    calc = DualInpCalculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.evaluate()

def test_sum_of_negative():
    """Test sigma function with negative input."""
    calc = SingleInpCalculation(int(-5), sigma)
    with pytest.raises(ValueError, match="Please enter an integer greater than 0"):
        calc.evaluate()
