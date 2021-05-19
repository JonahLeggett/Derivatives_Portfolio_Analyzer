# -*- coding: utf-8 -*-
"""A Collection of Financial Calculators.

This script contains a variety of financial calculator functions needed to
determine loan qualifications.

"""

import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

from qualifier.filters.ss_filters import (ss_filter, ss_match)


def get_total_position(portfolio_data_df, ticker):

    # Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]
    quantity = df["Quantity"]

    #Creating conditional statements where if there is a Buy Action, then create a new column called "Position" and put in the value of 1
    #Else, set the "Position" to -1
    df.loc[(df['Action'] == "BUY_TO_OPEN") | (df['Action'] == "BUY_TO_CLOSE"), 'Position'] = 1
    df.loc[(df['Action'] != "BUY_TO_OPEN") & (df['Action'] != "BUY_TO_CLOSE"), 'Position'] = -1

    position = df["Position"]

    df["Total Position"] = quantity * position
    total_position = df["Total Position"].sum()

    print(f"Your current position for {ticker} is {total_position}.")

def short_put(portfolio_data_df, ticker):
    # Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]
    return



def credit_spread(portfolio_data_df, ticker):
    return

def debit_spread(ticker):
    return

def short_strangle(portfolio_data_df, ticker, start_exp_date, start_strike_price, start_call_put, match_exp_date, match_strike_price, match_call_put):

    ss_filter(portfolio_data_df, ticker)
    result_df = ss_match(portfolio_data_df, start_exp_date, start_strike_price, start_call_put, match_exp_date, match_strike_price, match_call_put)

    return result_df

    """ #Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]

    #Clean-up and format the datatypes for the DataFrame
    df['Date'] = pd.to_datetime(df['Date'])
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'])

    #Filtering the DataFrame for only transactiosn for OPEN
    open_df = df.loc[(df['Action'] == "BUY_TO_OPEN") | (df['Action'] == "SELL_TO_OPEN")]

    #Sorting the value in ascending order by Date, and resetting the index of the DataFrame
    open_df = open_df.sort_values(by=["Date"])
    open_df = open_df.reset_index(drop = True)

    row = 0
    order = open_df.iloc[row]["Order #"]
    call_put = open_df.iloc[row]["Call or Put"]

    while order == open_df.iloc[row + 1]["Order #"] and open_df.iloc[row + 1]["Call or Put"] != call_put:
        open_df.at[row, "Strategy"] = "SS OPEN"
        open_df.at[row + 1, "Strategy"] = "SS OPEN"
        row += 1
    
    print(open_df)
       
    close_df = df.loc[(df['Action'] == "BUY_TO_CLOSE") | (df['Action'] == "SELL_TO_CLOSE")]
    #close_df.insert(18, "Strategy", 0)
    close_df = close_df.sort_values(by=["Date"])
    close_df = close_df.reset_index(drop = True)    

    print(close_df)

    combined_df = open_df.append(close_df, ignore_index = True)

    start_exp_date = open_df.iloc[row]["Expiration Date"]
    start_strike_price = open_df.iloc[row]["Strike Price"]
    start_call_put = open_df.iloc[row]["Call or Put"]

    match_exp_date = close_df.iloc[row]["Expiration Date"]
    match_strike_price = close_df.iloc[row]["Strike Price"]
    match_call_put = close_df.iloc[row]["Call or Put"]"""

def iron_condor(portfolio_data_df, ticker):

    #Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]

    return

def rolling_options(ticker):
    return

def covered_calls(ticker):
    return
