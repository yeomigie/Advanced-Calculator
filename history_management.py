# src/history_handler.py
import pandas as pd
import os

class HistoryTracker:
    """Manages calculation history using Pandas."""

    def __init__(self, file_path="data/calc_history.csv"):
        self.file_path = file_path
        if os.path.exists(self.file_path):
            self.history_data = pd.read_csv(self.file_path)
        else:
            self.history_data = pd.DataFrame(columns=["Calculation", "Outcome"])

    def add_entry(self, calculation, outcome):
        """Add a new entry to the history."""
        self.history_data = self.history_data.append({"Calculation": calculation, "Outcome": outcome}, ignore_index=True)
        self.save_history()

    def save_history(self):
        """Save history to a CSV file."""
        self.history_data.to_csv(self.file_path, index=False)

    def fetch_history(self):
        """Retrieve the calculation history."""
        return self.history_data

    def reset_history(self):
        """Clear the calculation history."""
        self.history_data = pd.DataFrame(columns=["Calculation", "Outcome"])
        self.save_history()
