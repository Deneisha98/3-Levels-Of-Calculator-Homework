from calculator.commands.add_command import AddCommand
from calculator.commands.subtract_command import SubtractCommand

add = AddCommand()
subtract = SubtractCommand()

print("Add 1, 2, 3:", add.execute(1, 2, 3))  # Should output 6
print("Subtract 10, 5:", subtract.execute(10, 5))  # Should output 5
