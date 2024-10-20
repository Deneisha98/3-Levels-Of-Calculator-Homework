from calculator.command import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        """Multiply all given arguments."""
        if not args:
            raise ValueError("At least one argument is required for multiplication.")
        try:
            result = 1.0
            for num in map(float, args):
                result *= num
            return int(result) if result.is_integer() else result 
        except ValueError:
            raise ValueError("All arguments must be numbers.")

    def get_name(self):
        return "multiply"  

