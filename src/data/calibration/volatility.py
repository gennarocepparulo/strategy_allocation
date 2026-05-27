"""
volatility.py

Empirical volatility estimation.
"""

import numpy as np


def compute_log_returns(prices):

    return np.log(
        prices / prices.shift(1)
    ).dropna()


def realized_volatility(log_returns):

    return np.std(log_returns)


def annualized_volatility(log_returns):

    return (
        np.sqrt(356)
        * np.std(log_returns)
    )