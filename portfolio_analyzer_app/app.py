# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
from os import startfile
import sys
import fire
import questionary
import csv
from pathlib import Path
import pandas as pd

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import get_current_position
from qualifier.utils.calculators import credit_spread
from qualifier.utils.calculators import debit_spread
from qualifier.utils.calculators import short_strangle
from qualifier.utils.calculators import iron_condor
from qualifier.utils.calculators import rolling_options
from qualifier.utils.calculators import covered_calls


from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

#from qualifier.filters.ticker import get_ticker

#Impot save_csv() function from fileio.py module
from qualifier.utils.fileio import save_csv 


def load_portfolio_csv():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter the file path for your portfolio CSV file to analyze:").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)

def get_ticker():
    """Prompt dialog to get the stocker ticker to analyze from the portfolio csv file.

    Returns:
        Returns the stock ticker
    """
    ticker = questionary.text("Choose your stock that you would like to analyze:").ask()
    ticker = str(ticker)
    
    return ticker

def choose_strategy():

    #Figure out how to display stock tickers from CSV file
    strategy = questionary.select(
        "Choose the strategy that you want to get analysis on:",
        choices = [
            "Current Position",
            "Credit Spread",
            "Debit Spread",
            "Short Strangle",
            "Iron Condor",
            "Rolling Options",
            "Covered Calls"
            ]).ask()
    return strategy


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    # @TODO: Complete the usability dialog for saving the CSV Files.
    # YOUR CODE HERE!

    #Setting a condition where if the user does not qualify for any loans, the app will print a message and exit the app
    if qualifying_loans == []:
        sys.exit("You have no qualifying loans at this time.  Please try again at another time.  Thank you.")

    #Using Quesionary confirm() to get user input of whether they want to save their CSV file or not
    else:
        confirm_save = questionary.confirm("Would you like to save your file?  Type 'y' for Yes or 'n' for No.").ask()
        
        if confirm_save == True:
            csvoutpath = questionary.text("Enter a file path of where you would like to save your file.").ask()
            csvoutpath = Path(csvoutpath)
            print (f"Your file has been saved in {csvoutpath}.  Thank you for using our app!")

            #Deleted save_csv from run(), and calling it here to save the file from user's input
            return save_csv(qualifying_loans)

        else:
            sys.exit("Your file has not been saved.  Thank you for using our app!")




def run():
    """The main function for running the script."""

    # Load the latest portfolio data
    portfolio_data = load_portfolio_csv()
    portfolio_data_df = pd.DataFrame(portfolio_data)
    print(portfolio_data_df)

    # Get the stock ticker
    ticker = get_ticker()
    
    #Choose how to analyze the stock ticker trades
    strategy = choose_strategy()

    if strategy == "Current Position":
        position = get_current_position(portfolio_data_df, ticker)
    elif strategy == "Credit Spread":
        credit_spread(portfolio_data_df, ticker)
    elif strategy == "Debit Spread":
        debit_spread(portfolio_data_df, ticker)
    elif strategy == "Short Strangle":
        short_strangle(portfolio_data_df, ticker)
    elif strategy == "Iron Condor":
        iron_condor(portfolio_data_df, ticker)
    elif strategy == "Rolling Options":
        rolling_options(portfolio_data_df, ticker)
    elif strategy == "Covered Calls":
        covered_calls(portfolio_data_df, ticker)

    # Save qualifying loans
    #save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
