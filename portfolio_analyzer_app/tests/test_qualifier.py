# Import pathlib
from pathlib import Path

#Import fileio functions
from qualifier.utils.fileio import load_csv
from qualifier.utils.fileio import save_csv

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# Import sys
import sys

#Import csv
import csv

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

    qualifying_loans = "test"

    csvpath = Path("./data/output/save_file.csv")
    save_csv(qualifying_loans)

    assert csvpath.exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = load_csv(Path('../data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!

    return test_save_csv()