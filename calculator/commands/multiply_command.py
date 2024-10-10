from calculator.command import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        """Multiply all given arguments."""
        result = 1
        try:
            for num in args:
                result *= float(num)
            return result
        except ValueError:
            raise ValueError("All arguments must be numbers.")
