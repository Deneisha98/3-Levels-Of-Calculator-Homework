# calculator/commands/subtract_command.py
from calculator.command import Command

class SubtractCommand(Command):
    def execute(self, *args):
        """Subtract all given arguments sequentially."""
        if not args:
            raise ValueError("At least one argument is required for subtraction.")
        try:
            result = float(args[0])
            for num in args[1:]:
                result -= float(num)
            return result
        except ValueError:
            raise ValueError("All arguments must be numbers.")

    def get_name(self):
        return "Subtraction"
