"""
risk_engine.py

Centralized portfolio risk evaluation.
"""

from .metrics import (
    compute_cagr,
    compute_log_growth,
)

from .drawdown import (
    compute_max_drawdown,
)

from .volatility import (
    compute_volatility,
)


class RiskEngine:

    def evaluate(
        self,
        portfolio,
        state
    ):

        history = portfolio.history

        if len(history) < 2:

            return {}

        return {

            "cagr":
                compute_cagr(history),

            "log_growth":
                compute_log_growth(history),

            "volatility":
                compute_volatility(history),

            "max_drawdown":
                compute_max_drawdown(history),

            "regime":
                state.regime,
        }