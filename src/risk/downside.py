"""
downside.py

Downside risk metrics.
"""

import numpy as np


def compute_downside_semivariance(
    returns
):

    downside = returns[
        returns < 0
    ]

    if len(downside) == 0:

        return 0.0

    return np.mean(
        downside**2
    )