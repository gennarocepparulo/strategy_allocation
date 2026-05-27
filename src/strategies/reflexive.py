"""
reflexive.py

Reflexive yield strategy.
"""

import numpy as np

from .strategy_base import Strategy


class ReflexiveYield(Strategy):

    def __init__(self):

        super().__init__("reflexive_yield")

    def generate_return(self, state):

        growth_component = (
            0.10 * state.liquidity
            + 0.08 * state.trend
        )

        leverage_bonus = (
            0.05 * (1 - state.leverage_stress)
        )

        instability_penalty = (
            -0.18 * state.leverage_stress
        )

        mean_return = (
            growth_component
            + leverage_bonus
            + instability_penalty
        )

        # Reflexive collapse dynamics
        if state.regime in ["stress", "panic"]:

            collapse_shock = np.random.normal(
                -0.30,
                0.15
            )

            if np.random.rand() < 0.30:
                return np.random.uniform(-0.70, -0.30)

        else:

            collapse_shock = 0.0

        realized_return = (
            np.random.normal(mean_return, 0.08)
            + collapse_shock
        )

        return realized_return