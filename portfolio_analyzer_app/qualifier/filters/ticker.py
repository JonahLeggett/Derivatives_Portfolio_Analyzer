# -*- coding: utf-8 -*-
"""Credit Score Filter.

This script filters a bank list by the user's minimum credit score.

"""


def get_ticker(ticker, portfolio_csv):
    """Filters the bank list by the mininim allowed credit score set by the bank.

    Args:
        credit_score (int): The applicant's credit score.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """

    ticker_filter_list = []
    for row in portfolio_csv:
        if ticker == row[12]:
            ticker_filter_list.append(row)
    return ticker_filter_list