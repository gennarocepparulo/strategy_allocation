"""
lending.py

Passive lending strategy.
"""

import numpy as np

from .strategy_base import Strategy


class PassiveLending(Strategy):

    def __init__(self):

        super().__init__("passive_lending")

    def generate_return(self, state):

        base_yield = 0.04

        liquidity_component = 0.03 * state.liquidity

        funding_component = 0.04 * state.funding

        stress_penalty = -0.05 * state.leverage_stress

        volatility_penalty = -0.02 * state.volatility

        mean_return = (
            base_yield
            + liquidity_component
            + funding_component
            + stress_penalty
            + volatility_penalty
        )

        realized_return = np.random.normal(
            mean_return,
            0.02
        )

        if state.regime in ["panic"]:
            if np.random.rand() < 0.08:
                return np.random.uniform(-0.40, -0.15)

        return realized_return