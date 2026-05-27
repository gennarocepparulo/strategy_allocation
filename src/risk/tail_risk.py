"""
tail_risk.py

Tail and collapse risk metrics.
"""

import numpy as np


def compute_var(
    returns,
    alpha=0.05
):

    return np.quantile(
        returns,
        alpha
    )


def compute_cvar(
    returns,
    alpha=0.05
):

    var = compute_var(
        returns,
        alpha
    )

    tail_losses = returns[
        returns <= var
    ]

    return np.mean(
        tail_losses
    )


def compute_ruin_probability(
    terminal_wealths,
    threshold=0.5
):

    ruined = [
        wealth < threshold
        for wealth in terminal_wealths
    ]

    return np.mean(ruined)