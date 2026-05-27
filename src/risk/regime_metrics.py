"""
regime_metrics.py

Regime-dependent performance metrics.
"""

from collections import defaultdict

import numpy as np


def compute_regime_returns(path):

    regime_returns = defaultdict(list)

    for step in path:

        regime = step.state.regime

        capital = step.portfolio.capital

        regime_returns[regime].append(capital)

    return regime_returns


def compute_regime_growth(path):

    regime_data = compute_regime_returns(path)

    results = {}

    for regime, capitals in regime_data.items():

        if len(capitals) < 2:
            continue

        returns = (
            np.diff(capitals)
            / capitals[:-1]
        )

        results[regime] = np.mean(returns)

    return results