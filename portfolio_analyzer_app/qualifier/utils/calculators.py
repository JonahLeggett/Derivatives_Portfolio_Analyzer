# -*- coding: utf-8 -*-
"""A Collection of Financial Calculators.

This script contains a variety of financial calculator functions needed to
determine loan qualifications.

"""

import pandas as pd
import numpy as np
from pathlib import Path

def get_total_position(portfolio_data_df, ticker):

    # Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]
    #quantity = df["Quantity"]

    #Creating conditional statements where if there is a Buy Action, then create a new column called "Position" and put in the value of 1
    #Else, set the "Position" to -1
    df.loc[(df['Action'] == "BUY_TO_OPEN") | (df['Action'] == "BUY_TO_CLOSE"), 'Position'] = 1
    df.loc[(df['Action'] != "BUY_TO_OPEN") & (df['Action'] != "BUY_TO_CLOSE"), 'Position'] = -1

    #position = df["Position"]

    df["Total Position"] = df["Quantity"] * df["Position"]
    total_position = df["Total Position"].sum()

    print(f"Your current position for {ticker} is {total_position}.")


def credit_spread(portfolio_data_df, ticker):
    return

def debit_spread(ticker):
    return

def short_strangle(portfolio_data_df, ticker):

    #Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]

    #Clean-up and format the datatypes for the DataFrame
    df['Date'] = pd.to_datetime(df['Date'])
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'])

    #Filtering the DataFrame for only transactiosn for OPEN
    df = df.loc[(df['Action'] == "BUY_TO_OPEN") | (df['Action'] == "SELL_TO_OPEN")]

    #Sorting the value in ascending order by Date, and resetting the index of the DataFrame
    df = df.sort_values(by=["Date"])
    df = df.reset_index(drop = True)

    return

def iron_condor(portfolio_data_df, ticker):

    #Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]

    return

def rolling_options(ticker):
    return

def covered_calls(ticker):
    return
