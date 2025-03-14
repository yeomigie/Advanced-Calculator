# tests/test_math_operations.py
from src.math_operations import MathEngine

def test_addition():
    engine = MathEngine()
    assert engine.addition(2, 3) == 5

def test_subtraction():
    engine = MathEngine()
    assert engine.subtraction(5, 3) == 2

def test_multiplication():
    engine = MathEngine()
    assert engine.multiplication(2, 3) == 6

def test_division():
    engine = MathEngine()
    assert engine.division(6, 3) == 2

def test_division_by_zero():
    engine = MathEngine()
    try:
        engine.division(6, 0)
    except ZeroDivisionError as e:
        assert str(e) == "Division by zero is not allowed"
