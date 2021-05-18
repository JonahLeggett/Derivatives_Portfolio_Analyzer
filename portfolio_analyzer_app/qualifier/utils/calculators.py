# -*- coding: utf-8 -*-
"""A Collection of Financial Calculators.

This script contains a variety of financial calculator functions needed to
determine loan qualifications.

"""


def get_current_position(portfolio_data_df, ticker):

    # Create a dataframe for the chosen ticker
    df = portfolio_data_df[portfolio_data_df['Underlying Symbol'] == ticker]
    quantity = df["Quantity"]

    #Creating conditional statements where if there is a Buy Action, then set the 
    df.loc[(df['Action'] == "BUY_TO_OPEN") | (df['Action'] == "BUY_TO_CLOSE"), 'Position'] = -1
    df.loc[(df['Action'] != "BUY_TO_OPEN") & (df['Action'] != "BUY_TO_CLOSE"), 'Position'] = 1

    position = df["Position"]

    df["Total Position"] = quantity * position
    total_position = df["Total Position"].sum()

    print(f"Your current position for {ticker} is {total_position}.")


def credit_spread(portfolio_data_df, ticker):
    return

def debit_spread(ticker):
    return

def short_strangle(ticker):
    return

def iron_condor(ticker):
    return

def rolling_options(ticker):
    return

def covered_calls(ticker):
    return
