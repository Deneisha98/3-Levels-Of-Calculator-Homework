from calculator.command import Command

class SubtractCommand(Command):
    def execute(self, *args):
        """Subtract all subsequent arguments from the first argument."""
        if len(args) < 2:
            raise ValueError("At least two numbers are required to perform subtraction.")
        try:
            result = float(args[0])
            for num in args[1:]:
                result -= float(num)
            return result
        except ValueError:
            raise ValueError("All arguments must be numbers.")
