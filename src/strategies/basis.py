"""
basis.py

Basis arbitrage / relative value strategy.
"""

import numpy as np

from .strategy_base import Strategy


class BasisArbitrage(Strategy):

    def __init__(self):

        super().__init__("basis_arbitrage")

    def generate_return(self, state):

        funding_component = 0.10 * state.funding

        liquidity_bonus = 0.03 * state.liquidity

        stress_penalty = -0.08 * state.leverage_stress

        volatility_penalty = -0.03 * state.volatility

        mean_return = (
            funding_component
            + liquidity_bonus
            + stress_penalty
            + volatility_penalty
        )

        realized_return = np.random.normal(
            mean_return,
            0.03
        )

        if state.regime in ["stress", "panic"]:

            funding_component *= -1.5

        return realized_return