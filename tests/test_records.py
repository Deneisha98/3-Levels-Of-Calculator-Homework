'''Test Records Functionality'''

from decimal import Decimal
import pytest
from calculator.calculation import DualInpCalculation
from calculator.records import Records
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for testing."""
    Records.clear_history()
    Records.add_calculation(DualInpCalculation(Decimal('10'), Decimal('5'), add))
    Records.add_calculation(DualInpCalculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to history."""
    calc = DualInpCalculation(Decimal('2'), Decimal('2'), add)
    Records.add_calculation(calc)
    assert Records.get_latest_record() == calc, "Failed to add the calculation"
    assert Records.get_latest_calculation() == (calc, calc.evaluate()), "Calculation not added with correct value"

def test_get_history(setup_calculations):
    """Test retrieving calculation history."""
    history = Records.get_history()
    assert len(history) == 2, "History count mismatch"

def test_clear_history(setup_calculations):
    """Test clearing history."""
    Records.clear_history()
    assert len(Records.get_history()) == 0, "Failed to clear history"

def test_get_latest_record(setup_calculations):
    """Test retrieving the latest calculation."""
    latest = Records.get_latest_record()
    latest_value = Records.get_latest_calculation()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Incorrect latest calculation"
    assert latest_value[1] == Decimal('17'), "Incorrect latest calculation value"

def test_find_by_operation(setup_calculations):
    """Test finding calculations by operation."""
    assert len(Records.find_by_operation("add")) == 1, "Add operation mismatch"
    assert len(Records.find_by_operation("subtract")) == 1, "Subtract operation mismatch"

def test_get_latest_record_with_empty_history():
    """Test latest calculation with empty history."""
    Records.clear_history()
    assert Records.get_latest_record() is None, "Expected None for empty history"
    assert Records.get_latest_calculation() is None, "Expected None for empty history"
