from calculator.command import Command
# calculator/commands/add_command.py
class AddCommand:
    def execute(self, *args):
        if not args:
            raise ValueError("At least one argument is required for addition.")
        
        result = 0
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError("All arguments must be numbers")
            result += num
        return result
from calculator.command import Command

class AddCommand(Command):
    def execute(self, *args):
        """Add all given arguments."""
        try:
            return sum(map(float, args))
        except ValueError:
            raise ValueError("All arguments must be numbers.")
