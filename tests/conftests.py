import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

# Function to generate test data
def generate_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Prevent division by zero
        if operation_func == divide and b == Decimal('0'):
            b = Decimal('1')

        expected = operation_func(a, b) if operation_func != divide or b != Decimal('0') else "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected

# Add the --num_records option to pytest
def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

# Fixture to get the value of num_records from the command line
@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")

# Generate the test cases dynamically
def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a,b,operation,expected", [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters
        ])
