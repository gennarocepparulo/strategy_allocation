"""
volatility.py

Volatility and instability metrics.
"""

import numpy as np


def compute_return_series(history):

    return np.diff(history) / history[:-1]


def compute_volatility(history):

    returns = compute_return_series(history)

    if len(returns) < 2:
        return np.nan

        return np.std(returns) * np.sqrt(365)

def compute_sharpe_ratio(
    history,
    risk_free_rate=0.0
):

    returns = compute_return_series(history)

    excess_returns = (
        returns - risk_free_rate
    )

    return (
        np.mean(excess_returns)
        / np.std(excess_returns)
    )