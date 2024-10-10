# calculator/repl.py

import importlib
import os

COMMANDS = {}

def load_commands():
    """Dynamically load command modules from the commands folder."""
    command_folder = 'calculator/commands'
    for filename in os.listdir(command_folder):
        if filename.endswith('_command.py'):
            module_name = filename[:-3]
            try:
                # Dynamically import the module
                module = importlib.import_module(f'calculator.commands.{module_name}')
                command_name = module_name.replace('_command', '').capitalize() + 'Command'
                
                # Add the command to the COMMANDS dictionary if it exists in the module
                if hasattr(module, command_name):
                    COMMANDS[command_name] = getattr(module, command_name)
            except ImportError as e:
                print(f"Error importing module {module_name}: {e}")

def print_help():
    """Display the help menu."""
    print("Available commands:")
    if COMMANDS:
        for command in COMMANDS.keys():
            print(f" - {command}")
    else:
        print("No commands available")
    print("\nType 'menu' to see this list again.")
