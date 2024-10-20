# calculator/commands/divide_command.py
from calculator.command import Command

class DivideCommand(Command):
    def execute(self, *args):
        """Divide the first argument by each subsequent argument."""
        if not args:
            raise ValueError("At least one argument is required for division.")
        try:
            result = float(args[0])
            for num in args[1:]:
                divisor = float(num)
                if divisor == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result /= divisor
            return result
        except ValueError:
            raise ValueError("All arguments must be numbers.")

    def get_name(self):
        return "Division"
