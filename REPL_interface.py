# src/cli_interface.py
from src.math_operations import MathEngine
from src.history_handler import HistoryTracker
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def command_line_interface():
    """Command-line interface for the calculator."""
    engine = MathEngine()
    tracker = HistoryTracker()

    while True:
        try:
            user_input = input(">>> ").strip().lower()
            if user_input == "quit":
                break
            elif user_input == "help":
                print("Available commands: add, subtract, multiply, divide, show_history, clear_history, quit")
            elif user_input == "show_history":
                print(tracker.fetch_history())
            elif user_input == "clear_history":
                tracker.reset_history()
                print("History cleared.")
            else:
                # Parse and execute arithmetic commands
                parts = user_input.split()
                if len(parts) != 3:
                    print("Invalid command. Usage: <operation> <num1> <num2>")
                    continue
                operation, num1, num2 = parts
                num1, num2 = float(num1), float(num2)
                if operation == "add":
                    result = engine.addition(num1, num2)
                elif operation == "subtract":
                    result = engine.subtraction(num1, num2)
                elif operation == "multiply":
                    result = engine.multiplication(num1, num2)
                elif operation == "divide":
                    result = engine.division(num1, num2)
                else:
                    print("Invalid operation. Use add, subtract, multiply, or divide.")
                    continue
                print(f"Result: {result}")
                tracker.add_entry(f"{num1} {operation} {num2}", result)
        except Exception as e:
            logger.error(f"Error: {e}")
