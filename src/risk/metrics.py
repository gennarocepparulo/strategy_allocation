"""
metrics.py

Core portfolio metrics.
"""

import numpy as np

from .tail_risk import (
    compute_var,
    compute_cvar
)

from .distribution import (
    compute_skewness,
    compute_kurtosis
)

from .downside import (
    compute_downside_semivariance
)

from .drawdown import (
    compute_max_drawdown
)

from .volatility import (
    compute_volatility
)


def compute_return_series(history):

    return np.diff(history) / history[:-1]


def compute_cagr(history):

    initial = history[0]

    final = history[-1]

    n_periods = len(history)

    return (
        (final / initial) ** (1 / n_periods)
        - 1
    )


def compute_log_growth(history):

    returns = compute_return_series(history)

    log_returns = np.log1p(returns)

    return np.mean(log_returns)


def compute_terminal_wealth(history):

    return history[-1]