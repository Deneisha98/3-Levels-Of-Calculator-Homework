'''Calculator Test Suite'''

from calculator import Calculator
from decimal import Decimal

def test_addition():
    '''Test that the addition function works correctly'''
    assert Calculator.add(Decimal(2), Decimal(2)) == Decimal(4)

def test_subtraction():
    '''Test that the subtraction function works correctly'''
    assert Calculator.subtract(Decimal(2), Decimal(2)) == Decimal(0)

def test_divide():
    '''Test that the division function works correctly'''
    assert Calculator.divide(Decimal(2), Decimal(2)) == Decimal(1)

def test_multiply():
    '''Test that the multiplication function works correctly'''
    assert Calculator.multiply(Decimal(2), Decimal(2)) == Decimal(4)

def test_sigma():
    '''Test that the sigma function works correctly'''
    assert Calculator.sigma(5) == 15
