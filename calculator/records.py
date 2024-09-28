from typing import Dict, Tuple, Union
from decimal import Decimal
from calculator.calculation import SingleInpCalculation, DualInpCalculation

class Records:
    """Stores all calculations performed by the Calculator class along with their results in a dictionary."""
    
    history: Dict[Union[SingleInpCalculation, DualInpCalculation], Decimal] = {}

    @classmethod
    def add_calculation(cls, calculation: Union[SingleInpCalculation, DualInpCalculation]):
        """Adds a new calculation record to the history."""
        cls.history[calculation] = calculation.evaluate()

    @classmethod
    def get_history(cls) -> Dict[Union[SingleInpCalculation, DualInpCalculation], Decimal]:
        """Returns the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest_record(cls) -> Union[SingleInpCalculation, DualInpCalculation, None]:
        """Returns the latest calculation performed or None if no history exists."""
        if cls.history:
            return list(cls.history.keys())[-1]
        return None
    
    @classmethod
    def get_latest_calculation(cls) -> Union[Tuple[Union[SingleInpCalculation, DualInpCalculation], Decimal], None]:
        """Returns the latest calculation and its result as a tuple, or None if no history exists."""
        if cls.history:
            return list(cls.history.items())[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> Dict[Union[SingleInpCalculation, DualInpCalculation], Decimal]:
        """Finds and returns a list of calculations by the operation name."""
        return {calc: result for calc, result in cls.history.items() if calc.operation.__name__ == operation_name}
