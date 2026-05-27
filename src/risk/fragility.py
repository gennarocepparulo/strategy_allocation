"""
fragility.py

Fragility and instability metrics.
"""

import numpy as np


def compute_fragility_index(history):

    returns = np.diff(history) / history[:-1]

    negative_returns = returns[
        returns < 0
    ]

    if len(negative_returns) == 0:

        return 0.0

    return (
        np.mean(np.abs(negative_returns))
        * len(negative_returns)
    )


def compute_tail_fragility(
    returns,
    alpha=0.05
):

    threshold = np.quantile(
        returns,
        alpha
    )

    tail_losses = returns[
        returns <= threshold
    ]

    return np.mean(np.abs(tail_losses))