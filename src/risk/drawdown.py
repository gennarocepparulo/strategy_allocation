"""
drawdown.py

Drawdown and impairment metrics.
"""

import numpy as np


def compute_drawdowns(history):

    history = np.array(history)

    running_max = np.maximum.accumulate(history)

    drawdowns = (
        history - running_max
    ) / running_max

    return drawdowns


def compute_max_drawdown(history):

    drawdowns = compute_drawdowns(history)

    return np.min(drawdowns)


def compute_average_drawdown(history):

    drawdowns = compute_drawdowns(history)

    return np.mean(drawdowns)

def compute_time_under_water(history):

    history = np.array(history)

    running_max = np.maximum.accumulate(history)

    underwater = history < running_max

    return np.sum(underwater)