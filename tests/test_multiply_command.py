from calculator.commands.multiply_command import MultiplyCommand

def test_multiply_command():
    command = MultiplyCommand()
    assert command.execute(2, 3, 4) == 24
    assert command.execute(1, 0, 5) == 0
    assert command.execute(5) == 5
    assert command.execute() == 1  # No arguments should return 1
