"""
vol_selling.py

Volatility selling strategy.
"""

import numpy as np

from .strategy_base import Strategy


class VolatilitySelling(Strategy):

    def __init__(self):

        super().__init__("volatility_selling")

    def generate_return(self, state):

        premium_income = 0.12

        volatility_penalty = -0.15 * state.volatility

        stress_penalty = -0.20 * state.leverage_stress

        liquidity_penalty = -0.05 * (
            1 - state.liquidity
        )

        mean_return = (
            premium_income
            + volatility_penalty
            + stress_penalty
            + liquidity_penalty
        )

        # Tail event amplification
        if state.regime in ["stress", "panic"]:

            tail_shock = np.random.normal(-0.25, 0.10)

        else:

            tail_shock = 0.0

        realized_return = (
            np.random.normal(mean_return, 0.05)
            + tail_shock
        )

        return realized_return