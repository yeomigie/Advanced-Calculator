# src/math_operations.py
class MathEngine:
    """Handles basic arithmetic operations."""

    def addition(self, x, y):
        """Add two numbers."""
        return x + y

    def subtraction(self, x, y):
        """Subtract two numbers."""
        return x - y

    def multiplication(self, x, y):
        """Multiply two numbers."""
        return x * y

    def division(self, x, y):
        """Divide two numbers."""
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return x / y
