# tests/test_multiply_command.py

import pytest
from calculator.commands.multiply_command import MultiplyCommand

def test_multiply_command():
    command = MultiplyCommand()
    
    # Test basic multiplication
    assert command.execute(2, 3, 4) == 24
    assert command.execute(1, 0, 5) == 0
    assert command.execute(7) == 7
    
    # Test multiplication with negative numbers
    assert command.execute(-2, 3) == -6
    assert command.execute(-2, -3) == 6
    
    # Test multiplication with zero
    assert command.execute(0, 5, 2) == 0
    assert command.execute(10, 0) == 0
    
    # Test no arguments (should raise ValueError)
    with pytest.raises(ValueError, match="At least one argument is required for multiplication"):
        command.execute()
    
    # Test non-numeric input (should raise ValueError)
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(5, 'a')

    # Test multiplication with floating point numbers
    assert command.execute(2.5, 4) == pytest.approx(10.0)
    assert command.execute(0.1, 0.2) == pytest.approx(0.02)
