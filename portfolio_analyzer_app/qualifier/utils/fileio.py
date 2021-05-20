# -*- coding: utf-8 -*-
"""Helper function to load the CSV file as a Pandas DataFrame.

This contains a helper function for loading CSV files and converting them
into Pandas DataFrames.

"""
import csv
from pathlib import Path
import pandas as pd


def load_csv(csv):
    """Reads the CSV file from path provided.

    Args:
        pd.read_csv(Path): The csv file path.

    Returns:
        A Pandas DataFrame.

    """
    portfolio_data_df = pd.read_csv(csv)
    return portfolio_data_df