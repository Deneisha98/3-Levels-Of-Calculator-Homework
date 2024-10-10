import pytest
from calculator.commands.subtract_command import SubtractCommand

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(10, 5) == 5
    assert command.execute(20, 5, 5) == 10
    assert command.execute(0, 5) == -5

    # Test for ValueError when fewer than two arguments are provided
    with pytest.raises(ValueError):
        command.execute(5)
