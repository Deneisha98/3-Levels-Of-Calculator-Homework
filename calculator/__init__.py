from calculator.records import Records
from calculator.operations import add, subtract, multiply, divide, sigma
from calculator.calculation import DualInpCalculation, SingleInpCalculation
from decimal import Decimal
from typing import Callable

class Calculator:
    """Main Calculator class that performs arithmetic operations and stores calculations in history."""

    @staticmethod
    def _perform_dual_input(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Performs a dual-input operation (e.g., add, subtract) and stores it in history."""
        calculation = DualInpCalculation.create(a, b, operation)
        Records.add_calculation(calculation)
        return calculation.evaluate()
    
    @staticmethod
    def _perform_single_input(a: Decimal, operation: Callable[[Decimal], Decimal]) -> Decimal:
        """Performs a single-input operation (e.g., sigma) and stores it in history."""
        calculation = SingleInpCalculation.create(a, operation)
        Records.add_calculation(calculation)
        return calculation.evaluate()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Performs addition of two numbers."""
        return Calculator._perform_dual_input(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Performs subtraction of two numbers."""
        return Calculator._perform_dual_input(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Performs multiplication of two numbers."""
        return Calculator._perform_dual_input(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Performs division of two numbers, raises error if dividing by zero."""
        return Calculator._perform_dual_input(a, b, divide)
    
    @staticmethod
    def sigma(a: int) -> int:
        """Calculates the sum of numbers from 1 to a."""
        return Calculator._perform_single_input(Decimal(a), sigma)
