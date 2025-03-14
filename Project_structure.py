# Create the project folder
mkdir advanced-calculator-2024
cd advanced-calculator-2024

# Create the folder structure
mkdir -p src utils tests data .github/workflows

# Create the virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install pandas pytest pylint

# Create initial files
touch src/__init__.py src/math_operations.py src/history_handler.py src/plugin_loader.py src/cli_interface.py
touch tests/__init__.py tests/test_math_operations.py tests/test_history_handler.py tests/test_plugins.py
touch data/calc_history.csv .github/workflows/ci.yml .coveragerc .pylintrc logging_config.conf app.py pytest.ini README.md requirements.txt
