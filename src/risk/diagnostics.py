"""
diagnostics.py

Monte Carlo portfolio diagnostics.
"""

import numpy as np

from .metrics import (
    compute_cagr,
    compute_log_growth,
    compute_volatility,
    compute_max_drawdown,
    compute_terminal_wealth,
)


class Diagnostics:

    def evaluate_paths(self, paths):

        cagrs = []

        log_growths = []

        volatilities = []

        drawdowns = []

        terminal_wealths = []


        for path in paths:

            portfolio_history = [
                step.portfolio.capital
                for step in path
            ]

            cagrs.append(
                compute_cagr(portfolio_history)
            )

            log_growths.append(
                compute_log_growth(portfolio_history)
            )

            volatilities.append(
                compute_volatility(portfolio_history)
            )

            drawdowns.append(
                compute_max_drawdown(
                    portfolio_history
                )
            )

            terminal_wealths.append(
                compute_terminal_wealth(
                    portfolio_history
                )
            )


        return {

            "mean_cagr":
                np.mean(cagrs),

            "mean_log_growth":
                np.mean(log_growths),

            "mean_volatility":
                np.mean(volatilities),

            "mean_max_drawdown":
                np.mean(drawdowns),

            "mean_terminal_wealth":
                np.mean(terminal_wealths),

            "wealth_dispersion":
                np.std(terminal_wealths),
        }