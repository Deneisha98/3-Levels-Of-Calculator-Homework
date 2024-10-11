import sys
from calculator.plugin_manager import PluginManager
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name, manager):
    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = manager.execute_plugin(operation_name.capitalize(), a_decimal, b_decimal)
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        # Handle the case where the operation is not found
        print(e)
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    # Get command-line arguments
    _, a, b, operation = sys.argv

    # Initialize the PluginManager and load plugins
    manager = PluginManager("calculator.commands")
    manager.load_plugins()

    # Perform calculation
    calculate_and_print(a, b, operation, manager)

if __name__ == '__main__':
    main()
