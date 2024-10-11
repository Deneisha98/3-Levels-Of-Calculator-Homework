# tests/test_add_command.py

import pytest
from calculator.commands.add_command import AddCommand

def test_add_command():
    command = AddCommand()
    
    # Test basic addition
    assert command.execute(2, 3, 4) == 9
    assert command.execute(10, 20) == 30
    assert command.execute(0, 5, 10) == 15
    
    # Test addition with negative numbers
    assert command.execute(-2, 3) == 1
    assert command.execute(-5, -10) == -15
    
    # Test addition with zero
    assert command.execute(0, 0, 0) == 0
    assert command.execute(10, 0) == 10
    
    # Test no arguments (should raise ValueError)
    with pytest.raises(ValueError, match="At least one argument is required for addition."):
        command.execute()
    
    # Test non-numeric input (should raise ValueError)
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(5, 'a')

    # Test addition with floating-point numbers
    assert command.execute(1.5, 2.5) == 4.0
    assert command.execute(0.1, 0.2, 0.3) == pytest.approx(0.6)
