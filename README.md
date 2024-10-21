# Homework 3 (with Logging and Plugins)

This project implements a calculator with basic arithmetic operations and features an object-oriented design. It now supports automated testing with `pytest`, includes logging functionality, and uses a plugin-based architecture for operations.

## Features

- Basic Operations:Add, Subtract, Multiply, Divide
- Handles Division by Zero
- Plugin-based Command System:Add new operations as plugins
- Calculation History
- Integration with Faker for Test Data Generation
- Logging: Provides application logs for better debugging and monitoring

## What's New

### Plugin-based Architecture
- Operations (Add, Subtract, Multiply, Divide) are implemented as separate plugins, making the system extensible. New operations can be added by simply creating a new plugin.

### Logging
- The application now includes logging using Python's built-in `logging` module. Logs are stored to provide insights into the flow of the application, such as start-up and calculation events.
- To view logs, configure `logging.conf`.

### How to Run

1. Clone the repo.
2. Set up a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
