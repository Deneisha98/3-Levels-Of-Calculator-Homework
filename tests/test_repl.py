# tests/test_repl.py

import pytest
import os
from unittest.mock import patch, MagicMock
from calculator.repl import load_commands, print_help, COMMANDS

def test_load_commands_success():
    # Clear existing commands
    COMMANDS.clear()
    
    # Use a mock to simulate command modules
    with patch('calculator.repl.os.listdir', return_value=['add_command.py', 'subtract_command.py']):
        with patch('calculator.repl.importlib.import_module') as mock_import:
            # Mock module and command class
            mock_module = MagicMock()
            mock_command_class = MagicMock()
            mock_module.AddCommand = mock_command_class
            mock_import.return_value = mock_module
            
            load_commands()
            
            # Check if the commands were loaded
            assert 'AddCommand' in COMMANDS
            assert COMMANDS['AddCommand'] is mock_command_class

def test_load_commands_import_error():
    # Clear existing commands
    COMMANDS.clear()
    
    # Mock a failing import
    with patch('calculator.repl.os.listdir', return_value=['failing_command.py']):
        with patch('calculator.repl.importlib.import_module', side_effect=ImportError("Mocked ImportError")):
            load_commands()
            
            # Ensure the command is not added due to the ImportError
            assert 'FailingCommand' not in COMMANDS

def test_load_commands_with_non_python_files():
    # Mocking the directory to include non-Python files
    COMMANDS.clear()
    with patch('calculator.repl.os.listdir', return_value=['add_command.py', 'README.md', 'config.txt']):
        with patch('calculator.repl.importlib.import_module') as mock_import:
            mock_module = MagicMock()
            mock_command_class = MagicMock()
            mock_module.AddCommand = mock_command_class
            mock_import.return_value = mock_module
            
            load_commands()
            
            # Only the .py file should be loaded
            assert 'AddCommand' in COMMANDS
            assert 'README' not in COMMANDS
            assert 'config' not in COMMANDS

def test_load_commands_with_existing_commands():
    # Mock an existing command
    COMMANDS.clear()
    COMMANDS['ExistingCommand'] = MagicMock()
    
    # Mock directory with new command file
    with patch('calculator.repl.os.listdir', return_value=['new_command.py']):
        with patch('calculator.repl.importlib.import_module') as mock_import:
            mock_module = MagicMock()
            mock_command_class = MagicMock()
            mock_module.NewCommand = mock_command_class
            mock_import.return_value = mock_module
            
            load_commands()
            
            # Ensure both the existing and new commands are present
            assert 'ExistingCommand' in COMMANDS
            assert 'NewCommand' in COMMANDS

def test_print_help(capsys):
    # Mock the COMMANDS dictionary
    COMMANDS.clear()
    COMMANDS['AddCommand'] = MagicMock()
    COMMANDS['SubtractCommand'] = MagicMock()
    
    # Call the function
    print_help()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check if the help message contains the command names
    assert "Available commands" in captured.out
    assert "AddCommand" in captured.out
    assert "SubtractCommand" in captured.out

def test_print_help_with_no_commands(capsys):
    # Clear the commands
    COMMANDS.clear()
    
    # Call the function
    print_help()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Ensure it indicates that there are no available commands
    assert "Available commands" in captured.out
    assert "No commands available" in captured.out

