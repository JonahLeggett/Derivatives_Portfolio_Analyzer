# -*- coding: utf-8 -*-
"""Dataframe Cleanup Filter.

This script cleans up the Dataframe by converting all values to its appropriate type
to prepare for calculations and analysis.

"""
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def df_clean_up(df):
    
    #Convert dates to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date']) 

    #Convert values into integer values for calculation
    df['Value'] = pd.to_numeric(df['Value'].str.replace(",", ""))
    df['Average Price'] = pd.to_numeric(df['Average Price'].str.replace(",", ""))
    df['Commissions'] = pd.to_numeric(df['Commissions'].str.replace("--", ""))
    df['Expiration Date'] = pd.to_datetime(df['Expiration Date'])

    return df