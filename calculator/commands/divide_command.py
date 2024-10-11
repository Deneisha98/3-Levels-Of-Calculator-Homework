from calculator.command import Command
# calculator/commands/divide_command.py
class DivideCommand:
    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("At least two arguments are required for division.")
        
        result = float(args[0])
        for num in args[1:]:
            if not isinstance(num, (int, float)):
                raise ValueError("All arguments must be numbers")
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result /= num
        return result
