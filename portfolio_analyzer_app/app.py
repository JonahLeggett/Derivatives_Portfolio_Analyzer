# -*- coding: utf-8 -*-
"""Derivatives Portfolio Metrics Analyzer App.

This is a command line application to get the user strategy metrics for his derivaties portfolio.

Example:
    $ python app.py
"""

#Import all libraries required to run the application
from os import startfile
import sys
import fire
import questionary
import csv
from pathlib import Path
import pandas as pd

from qualifier.utils.fileio import load_csv

from qualifier.filters.clean_up_df_filter import df_clean_up

#Import the strategy calculators
from qualifier.utils.strategy import (
    get_total_position,
    short_put_gross_net_value,
    long_put_gross_net_value,
    short_call_gross_net_value,
    long_call_gross_net_value,
    short_call_avg_net_value,
    long_call_avg_net_value,
    short_put_avg_net_value,
    long_put_avg_net_value,
    credit_spread,
    debit_spread,
    short_strangle,
    iron_condor,
    rolling_options,
    covered_calls)


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
    """Prompt dialog to get the user to choose the strategy that they want metrics on.

    Returns:
        Returns the strategy
    """
    strategy = questionary.select(
        "Choose the strategy that you want to get analysis on:",
        choices = [
            "Total Position",
            "Short Put - Gross & Net Value",
            "Long Put - Gross & Net Value",
            "Short Call - Gross & Net Value",
            "Long Call - Gross & Net Value",
            "Short Put - Average Values",
            "Long Put - Average Values",
            "Short Call - Average Values",
            "Long Call - Average Values",
            "Credit Spread - *Feature Coming Soon!*",
            "Debit Spread - *Feature Coming Soon!*",
            "Short Strangle - *Feature Coming Soon!*",
            "Iron Condor - *Feature Coming Soon!*",
            "Rolling Options - *Feature Coming Soon!*",
            "Covered Calls - *Feature Coming Soon!*"
            ]).ask()

    return strategy

def run():
    """The main function for running the script."""

    print("Hello!  Welcome to the Derivatives Portfolio Analyzer!")

    # Load the latest portfolio data
    portfolio_data = load_portfolio_csv()
    portfolio_data_df = pd.DataFrame(portfolio_data)

    # Get the stock ticker from user input
    ticker = get_ticker()

    #Filter the dataframe by the ticker
    portfolio_data_df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]

    #Clean up the dataframe by converting its values to appropriate types for calculations
    portfolio_data_df = df_clean_up(portfolio_data_df)
    print(portfolio_data_df.info())

    #Choose how to analyze the stock ticker trades
    strategy = choose_strategy()

    #Runs the chosen strategy by the user.
    if strategy == "Total Position":
        position = get_total_position(portfolio_data_df, ticker)
    elif strategy == "Short Put - Gross & Net Value":
        short_put_gross_net_value(portfolio_data_df, ticker)
    elif strategy == "Long Put - Gross & Net Value":
        long_put_gross_net_value(portfolio_data, ticker)
    elif strategy == "Short Call - Gross & Net Value":
        short_call_gross_net_value(portfolio_data_df, ticker)
    elif strategy == "Long Call - Gross & Net Value":
        long_call_gross_net_value(portfolio_data_df, ticker)
    elif strategy == "Short Put - Average Values":
        short_put_avg_net_value(portfolio_data_df, ticker)
    elif strategy == "Long Put - Average Values":
        long_put_avg_net_value(portfolio_data_df, ticker)
    elif strategy == "Short Call - Average Values":
        short_call_avg_net_value(portfolio_data_df, ticker)
    elif strategy == "Long Call - Average Values":
        long_call_avg_net_value(portfolio_data_df, ticker)
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

if __name__ == "__main__":
    fire.Fire(run)
