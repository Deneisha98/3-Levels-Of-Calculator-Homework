from calculator.command import Command

class DivideCommand(Command):
    def execute(self, *args):
        """Divide the first argument by each subsequent argument."""
        if len(args) < 2:
            raise ValueError("At least two numbers are required to perform division.")
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
