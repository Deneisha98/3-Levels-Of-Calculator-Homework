# tests/test_divide_command.py

import pytest
from calculator.commands.divide_command import DivideCommand

def test_divide_command():
    command = DivideCommand()
    
    # Test basic division
    assert command.execute(20, 4) == 5
    assert command.execute(100, 5, 2) == 10
    assert command.execute(1, 1) == 1
    
    # Test division by zero (should raise ZeroDivisionError)
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
        command.execute(10, 0)
    
    # Test fewer than two arguments (should raise ValueError)
    with pytest.raises(ValueError, match="At least two arguments are required for division."):
        command.execute(5)
    
    # Test with negative numbers
    assert command.execute(-20, 4) == -5
    assert command.execute(20, -4) == -5
    assert command.execute(-20, -4) == 5

    # Test division with floating-point numbers
    assert command.execute(9.0, 3.0) == 3.0
    assert command.execute(5.5, 2.0) == pytest.approx(2.75)
    
    # Test multiple divisions resulting in a fraction
    assert command.execute(100, 2, 5) == 10.0
    assert command.execute(10, 3) == pytest.approx(3.3333, rel=1e-4)
