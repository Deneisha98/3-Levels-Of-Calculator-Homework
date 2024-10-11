# tests/test_commands.py

import pytest
from calculator.commands.add_command import AddCommand
from calculator.commands.subtract_command import SubtractCommand
from calculator.commands.multiply_command import MultiplyCommand
from calculator.commands.divide_command import DivideCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(1, 2, 3) == 6
    assert command.execute(0, -1, 5) == 4
    assert command.execute(0) == 0
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(1, 'a')

def test_subtract_command():
    command = SubtractCommand()
    assert command.execute(10, 5) == 5
    assert command.execute(20, 4, 3) == 13
    assert command.execute(-10, -5) == -5
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(10, 'b')
    with pytest.raises(ValueError, match="At least two numbers are required"):
        command.execute(5)

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(2, 3, 4) == 24
    assert command.execute(-1, 5) == -5
    assert command.execute(0, 1) == 0
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(2, 'c')
    with pytest.raises(ValueError, match="At least one argument is required for multiplication"):
        command.execute()

def test_divide_command():
    command = DivideCommand()
    assert command.execute(10, 2) == 5
    assert command.execute(100, 5, 2) == 10
    assert command.execute(-20, 4) == -5
    with pytest.raises(ValueError, match="All arguments must be numbers"):
        command.execute(10, 'd')
    with pytest.raises(ValueError, match="At least two arguments are required for division"):
        command.execute(5)
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
        command.execute(10, 0)
