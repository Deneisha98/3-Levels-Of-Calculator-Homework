from calculator.commands.add_command import AddCommand

def test_add_command():
    command = AddCommand()
    assert command.execute(1, 2, 3) == 6
    assert command.execute(5, -5, 10) == 10
    assert command.execute() == 0
