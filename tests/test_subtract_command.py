# tests/test_subtract_command.py

import pytest
from calculator.commands.subtract_command import SubtractCommand

def test_subtract_command():
    command = SubtractCommand()
    
    # Test basic subtraction
    assert command.execute(10, 5) == 5
    assert command.execute(20, 4, 3) == 13
    
    # Test subtraction with negative numbers
    assert command.execute(-10, 5) == -15
    assert command.execute(5, -5) == 10
    
    # Test subtraction resulting in zero
    assert command.execute(10, 10) == 0
    
    # Test subtraction with a single argument (should raise ValueError)
    with pytest.raises(ValueError, match="At least two numbers are required"):
        command.execute(5)
    
    # Test non-numeric input (should raise ValueError)
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(10, 'a')

    # Test multiple negative numbers
    assert command.execute(-5, -10, -2) == 7

    # Test with floating point numbers
    assert command.execute(10.5, 4.5) == 6.0
    assert command.execute(3.2, 1.1, 0.1) == 2.0
