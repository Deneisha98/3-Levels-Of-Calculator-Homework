import sys
from calculator.plugin_manager import PluginManager
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv # type: ignore
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Log application start
logger.info("Application starting...")

# Get environment variable
environment = os.getenv("ENVIRONMENT", "development")
logger.info(f"Running in {environment} environment")

def calculate_and_print(a, b, operation_name, manager):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = manager.execute_plugin(operation_name.capitalize(), a_decimal, b_decimal)
        # Format the result to avoid trailing .0 if it's a whole number
        formatted_result = "{:.0f}".format(result) if result % 1 == 0 else str(result)
        print(f"The result of {a} {operation_name} {b} is equal to {formatted_result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        logger.error("Invalid number of arguments")
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
from app import App    
if __name__ == "__main__":
    app = App().start()  
