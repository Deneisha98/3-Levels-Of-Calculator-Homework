from calculator.command import Command
# calculator/commands/add_command.py
class AddCommand:
    def execute(self, *args):
        if not args:
            raise ValueError("At least one argument is required for addition.")
        
        result = 0
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError("All arguments must be numbers")
            result += num
        return result
