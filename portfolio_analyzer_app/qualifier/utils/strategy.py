# -*- coding: utf-8 -*-
"""A Collection of Strategy Calculators.

This script contains a variety of strategy calculator functions needed to
determine metrics for the derivatives portfolio.

"""

#Import required libraries
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import warnings
warnings.filterwarnings('ignore')

from qualifier.filters.ss_filters import (ss_filter, ss_match)

#Create a function to get the total position of the user-specfid ticker
def get_total_position(df, ticker):

    #Create variable to get quantity value in each row of the Dataframe
    quantity = df["Quantity"]

    #Creating conditional statements where if there is a Buy Action, then create a new column called "Position" and put in the value of 1
    #Else, set the "Position" to -1
    df.loc[(df['Action'] == "BUY_TO_OPEN") | (df['Action'] == "BUY_TO_CLOSE"), 'Position'] = 1
    df.loc[(df['Action'] != "BUY_TO_OPEN") & (df['Action'] != "BUY_TO_CLOSE"), 'Position'] = -1

    #Create a variable for the actual numerical position of the options trade
    position = df["Position"]

    #Creating a new column in the DataFrame to hold the total position for the row
    df["Total Position"] = quantity * position

    #Getting the total position by summing all values in the Total Position column
    total_position = df["Total Position"].sum()

    #Print out the total position for the user.
    print(f"Your current position for {ticker} is {total_position}.")

#Create a function to calculate gross and net values of short puts on specified ticker
def short_put_gross_net_value(df, ticker):

    # Filter the dataframe by the short actions
    df = df.loc[(df["Action"] == "SELL_TO_OPEN") | (df["Action"] == "SELL_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "PUT"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")
    
    else:

        #Create variables to hold the gross value, total commission fees, and total fees to help calculate the net value
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees
	
        #Print statements to show the metrics
        print(f"Your short put gross value for {ticker} is ${round(gross_value,2)}.")
        print(f"Your total short put commission fees for {ticker} is ${round(total_commissions,2)}.")
        print(f"Your total short put fees for {ticker} is ${round(total_fees,2)}.")
        print(f"Your short put net value for {ticker} is ${round(net_value,2)}.")

#Create a function to calculate gross and net values of long puts on specified ticker
def long_put_gross_net_value(df, ticker):

    #Filter the dataframe by the long actions
    df = df.loc[(df["Action"] == "BUY_TO_OPEN") | (df["Action"] == "BUY_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "PUT"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")

    else:

        #Convert values into integer values for calculation
        df['Value'] = pd.to_numeric(df['Value'].str.replace(",", ""))
        df['Average Price'] = pd.to_numeric(df['Average Price'].str.replace(",", ""))
        df['Commissions'] = pd.to_numeric(df['Commissions'].str.replace("--", ""))
        df['Expiration Date'] = pd.to_datetime(df['Expiration Date'])

        #Create variables to hold the gross value, total commission fees, and total fees to help calculate the net value
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees
	
        #Print statements to show the metrics
        print(f"Your long put gross value for {ticker} is ${round(gross_value,2)}.")
        print(f"Your total long put commission fees for {ticker} is ${round(total_commissions,2)}.")
        print(f"Your total long put fees for {ticker} is ${round(total_fees,2)}.")
        print(f"Your long put net value for {ticker} is ${round(net_value,2)}.")

#Create a function to calculate gross and net values of short calls on specified ticker
def short_call_gross_net_value(df, ticker):

    #Filter the dataframe by the short actions
    df = df.loc[(df["Action"] == "SELL_TO_OPEN") | (df["Action"] == "SELL_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "CALL"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")
    
    else:

        #Create variables to hold the gross value, total commission fees, and total fees to help calculate the net value
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees
        
        #Print statements to show the metrics
        print(f"Your short call gross value for {ticker} is ${round(gross_value,2)}.")
        print(f"Your total short call commission fees for {ticker} is ${round(total_commissions,2)}.")
        print(f"Your total short call fees for {ticker} is ${round(total_fees,2)}.")
        print(f"Your short call net value for {ticker} is ${round(net_value,2)}.")

#Create a function to calculate gross and net values of long calls on specified ticker
def long_call_gross_net_value(df, ticker):

    #Filter the dataframe by the long actions
    df = df.loc[(df["Action"] == "BUY_TO_OPEN") | (df["Action"] == "BUY_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "CALL"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")
    
    else:
        #Create variables to hold the gross value, total commission fees, and total fees to help calculate the net value
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees

        #Print statements to show the metrics
        print(f"Your long call gross value for {ticker} is ${round(gross_value,2)}.")
        print(f"Your total long call commission fees for {ticker} is ${round(total_commissions,2)}.")
        print(f"Your total long call fees for {ticker} is ${round(total_fees,2)}.")
        print(f"Your long call net value for {ticker} is ${round(net_value,2)}.")

#Create a function to calculate averege and net average values of short puts on specified ticker
def short_put_avg_net_value(df, ticker):

    #Filter the dataframe by the short actions
    df = df.loc[(df["Action"] == "SELL_TO_OPEN") | (df["Action"] == "SELL_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "PUT"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")

    else:

        #Create variables to hold the average value, gross value, total commission fees, and total fees to help calculate the average net value
        avg_value = df["Value"].mean()
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees
        rows = len(df.index)
        avg_net_value = net_value / rows

        #Print statements to show the metrics
        print(f"Your short put average value for {ticker} is ${round(avg_value,2)}.")
        print(f"Your short put average net value for {ticker} is ${round(avg_net_value,2)}.")

#Create a function to calculate averege and net average values of long puts on specified ticker
def long_put_avg_net_value(df, ticker):

    #Filter the dataframe by the short actions
    df = df[(df["Action"] == "BUY_TO_OPEN") | (df["Action"] == "BUY_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "PUT"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")
    
    else:

        #Create variables to hold the average value, gross value, total commission fees, and total fees to help calculate the average net value
        avg_value = df["Value"].mean()
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees
        rows = len(df.index)
        avg_net_value = net_value / rows

        #Print statements to show the metrics
        print(f"Your long put average value for {ticker} is ${round(avg_value,2)}.")
        print(f"Your long put average net value for {ticker} is ${round(avg_net_value,2)}.")

#Create a function to calculate averege and net average values of long puts on specified ticker
def short_call_avg_net_value(df, ticker):

    #Filter the dataframe by the short actions
    df = df.loc[(df["Action"] == "SELL_TO_OPEN") | (df["Action"] == "SELL_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "CALL"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")

    else:

        #Create variables to hold the average value, gross value, total commission fees, and total fees to help calculate the average net value
        avg_value = df["Value"].mean()
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value + total_commissions + total_fees
        rows = len(df.index)
        avg_net_value = net_value / rows
        
        #Print statements to show the metrics
        print(f"Your short call average value for {ticker} is ${round(avg_value,2)}.")
        print(f"Your short call average net value for {ticker} is ${round(avg_net_value,2)}.")

#Create a function to calculate averege and net average values of long puts on specified ticker
def long_call_avg_net_value(df, ticker):

    #Filter the dataframe by the short actions
    df = df[(df["Action"] == "BUY_TO_OPEN") | (df["Action"] == "BUY_TO_CLOSE")]
    df = df.loc[df["Call or Put"] == "CALL"]

    if len(df) == 0:
        print("You did not employ this strategy for this ticker.")

    else:

        #Create variables to hold the average value, gross value, total commission fees, and total fees to help calculate the average net value
        avg_value = df["Value"].mean()
        gross_value = df["Value"].sum()
        total_commissions = df["Commissions"].sum()
        total_fees = df["Fees"].sum()
        net_value = gross_value - total_commissions - total_fees
        rows = len(df.index)
        avg_net_value = net_value / rows

        #Print statements to show the metrics
        print(f"Your long call average value for {ticker} is ${round(avg_value,2)}.")
        print(f"Your long call average net value for {ticker} is ${round(avg_net_value,2)}.")


def credit_spread(df):
    return

def debit_spread(df):
    return

def short_strangle(df):
    return

"""
def short_strangle(portfolio_data_df, ticker, start_exp_date, start_strike_price, start_call_put, match_exp_date, match_strike_price, match_call_put):

    ss_filter(portfolio_data_df, ticker)
    result_df = ss_match(portfolio_data_df, start_exp_date, start_strike_price, start_call_put, match_exp_date, match_strike_price, match_call_put)

    return result_df

    #Create a dataframe for the chosen ticker
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
    return

def rolling_options(ticker):
    return

def covered_calls(ticker):
    return
