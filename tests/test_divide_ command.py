import pytest
from calculator.commands.divide_command import DivideCommand

def test_divide_command():
    command = DivideCommand()
    
    # Test basic division
    assert command.execute(20, 4) == 5
    
    # Test division by zero error
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        command.execute(10, 0)
    
    # Test regex matching for division output
    output = "The result of 20 divide 4 is equal to 5.0"
    assert output == "The result of 20 divide 4 is equal to 5.0"
