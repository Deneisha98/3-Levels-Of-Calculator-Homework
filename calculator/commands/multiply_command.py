from calculator.command import Command

class MultiplyCommand:
    def execute(self, *args):
        if not args:
            raise ValueError("At least one argument is required for multiplication.")
        
        result = 1
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError("All arguments must be numbers")
            result *= num
        return result
