from calculator.command import Command

class AddCommand(Command):
    def execute(self, *args):
        """Add all given arguments."""
        if not args:
            raise ValueError("At least one argument is required for addition.")
        try:
            result = sum(map(float, args))
            return int(result) if result.is_integer() else result 
        except ValueError:
            raise ValueError("All arguments must be numbers.")

    def get_name(self):
        return "add"  
