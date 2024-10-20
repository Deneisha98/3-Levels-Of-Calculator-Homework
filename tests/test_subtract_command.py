import pytest
from calculator.commands.subtract_command import SubtractCommand

def test_subtract_command():
    command = SubtractCommand()
    
    # Test basic subtraction
    assert command.execute(10, 2) == 8
    
    # Test regex matching for floats
    output = "The result of 10 subtract 2 is equal to 8.0"
    assert output == "The result of 10 subtract 2 is equal to 8.0"
    
    # Test subtraction with negative numbers
    assert command.execute(-10, 5) == -15
    assert command.execute(5, 5) == 0
    
    # Test raising ValueError with less than two arguments
    with pytest.raises(ValueError, match="At least two arguments are required for subtraction."):
        command.execute(10)
