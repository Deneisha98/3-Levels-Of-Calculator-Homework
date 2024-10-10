from calculator.command import Command

class AddCommand(Command):
    def execute(self, *args):
        """Add all given arguments."""
        try:
            return sum(map(float, args))
        except ValueError:
            raise ValueError("All arguments must be numbers.")
