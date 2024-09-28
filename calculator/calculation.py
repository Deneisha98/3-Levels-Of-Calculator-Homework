from decimal import Decimal
from typing import Callable

class DualInpCalculation:
    """Represents a calculation involving two inputs."""
    
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return DualInpCalculation(a, b, operation)
    
    def evaluate(self) -> Decimal:
        """Evaluates the operation on the two inputs."""
        return self.operation(self.a, self.b)
    
    def __repr__(self) -> str:
        return f"DualInpCalculation({self.a}, {self.b}, {self.operation.__name__})"


class SingleInpCalculation:
    """Represents a calculation involving a single input."""
    
    def __init__(self, a: Decimal, operation: Callable[[Decimal], Decimal]):
        self.a = a
        self.operation = operation
    
    @staticmethod
    def create(a: Decimal, operation: Callable[[Decimal], Decimal]):
        return SingleInpCalculation(a, operation)
    
    def evaluate(self) -> Decimal:
        """Evaluates the operation on the input."""
        return self.operation(self.a)
    
    def __repr__(self) -> str:
        return f"SingleInpCalculation({self.a}, {self.operation.__name__})"
