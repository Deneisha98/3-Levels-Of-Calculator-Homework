'''Test Arithmetic Operations'''

from decimal import Decimal
import pytest
from calculator.calculation import SingleInpCalculation, DualInpCalculation
from calculator.operations import add, subtract, multiply, divide, sigma

def test_add():
    '''Test addition operation'''
    calc = DualInpCalculation(Decimal('10'), Decimal('5'), add)
    assert calc.evaluate() == Decimal('15'), "Addition failed"

def test_subtract():
    '''Test subtraction operation'''
    calc = DualInpCalculation(Decimal('10'), Decimal('5'), subtract)
    assert calc.evaluate() == Decimal('5'), "Subtraction failed"

def test_multiply():
    '''Test multiplication operation'''
    calc = DualInpCalculation(Decimal('10'), Decimal('5'), multiply)
    assert calc.evaluate() == Decimal('50'), "Multiplication failed"

def test_divide():
    '''Test division operation'''
    calc = DualInpCalculation(Decimal('10'), Decimal('5'), divide)
    assert calc.evaluate() == Decimal('2'), "Division failed"

def test_divide_by_zero():
    '''Test division by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc = DualInpCalculation(Decimal('10'), Decimal('0'), divide)
        calc.evaluate()

def test_sigma():
    '''Test sigma (sum) operation'''
    calc = SingleInpCalculation(100, sigma)
    assert calc.evaluate() == 5050, "Sigma operation failed"
