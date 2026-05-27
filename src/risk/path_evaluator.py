"""
path_evaluator.py

Unified portfolio path evaluation.
"""

import numpy as np

from .metrics import (
    compute_cagr,
    compute_log_growth,
)

from .drawdown import (
    compute_max_drawdown,
    compute_time_under_water
)

from .volatility import (
    compute_volatility
)

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

from .ruin import (
    compute_ruin_probability
)


# --------------------------------------------------
# Wealth -> returns
# --------------------------------------------------

def wealth_to_returns(
    wealth_history
):

    wealth = np.array(
        wealth_history
    )

    returns = (
    wealth[1:] / wealth[:-1]
) - 1

    returns = returns[
    np.isfinite(returns)
]

    return returns


# --------------------------------------------------
# Single path evaluation
# --------------------------------------------------

def evaluate_path_metrics(
    wealth_history
):

    returns = wealth_to_returns(
        wealth_history
    )

    results = {

        "terminal_wealth":
            wealth_history[-1],

        "cagr":
            compute_cagr(
                wealth_history
            ),

        "log_growth":
            compute_log_growth(
                wealth_history
            ),

        "volatility":
            compute_volatility(
                returns
            ),

        "max_drawdown":
            compute_max_drawdown(
                wealth_history
            ),

        "time_under_water":
            compute_time_under_water(
                wealth_history
            ),

        "VaR_5":
            compute_var(
                returns,
                alpha=0.05
            ),

        "CVaR_5":
            compute_cvar(
                returns,
                alpha=0.05
            ),

        "skewness":
            compute_skewness(
                returns
            ),

        "kurtosis":
            compute_kurtosis(
                returns
            ),

        "downside_semivariance":
            compute_downside_semivariance(
                returns
            ),
    }

    return results


# --------------------------------------------------
# Multi-path evaluation
# --------------------------------------------------

def evaluate_many_paths(
    wealth_paths
):

    all_metrics = []

    for wealth_history in wealth_paths:

        metrics = evaluate_path_metrics(
        )
        wealth_history = wealth_history[
    np.isfinite(wealth_history)
]
         
        all_metrics.append(metrics)

    results = {

        "mean_terminal_wealth":
            np.mean([
                m["terminal_wealth"]
                for m in all_metrics
            ]),

        "median_terminal_wealth":
            np.median([
                m["terminal_wealth"]
                for m in all_metrics
            ]),

        "mean_cagr":
            np.mean([
                m["cagr"]
                for m in all_metrics
            ]),

        "median_cagr":
            np.median([
                m["cagr"]
                for m in all_metrics
            ]),

        "mean_log_growth":
            np.mean([
                m["log_growth"]
                for m in all_metrics
            ]),

        "mean_volatility":
            np.mean([
                m["volatility"]
                for m in all_metrics
            ]),

        "mean_drawdown":
            np.mean([
                m["max_drawdown"]
                for m in all_metrics
            ]),

        "worst_drawdown":
            np.min([
                m["max_drawdown"]
                for m in all_metrics
            ]),

        "mean_time_under_water":
            np.mean([
                m["time_under_water"]
                for m in all_metrics
            ]),

        "mean_VaR_5":
            np.mean([
                m["VaR_5"]
                for m in all_metrics
            ]),

        "mean_CVaR_5":
            np.mean([
                m["CVaR_5"]
                for m in all_metrics
            ]),

        "mean_skewness":
            np.mean([
                m["skewness"]
                for m in all_metrics
            ]),

        "mean_kurtosis":
            np.mean([
                m["kurtosis"]
                for m in all_metrics
            ]),

        "mean_downside_semivariance":
            np.mean([
                m["downside_semivariance"]
                for m in all_metrics
            ]),

        "ruin_probability":
            compute_ruin_probability(
                wealth_paths,
                ruin_threshold=0.5
            ),
    }

    return results