"""
amm.py

AMM LP strategy with convex IL dynamics.
"""

import numpy as np

from .strategy_base import Strategy


class AMMLiquidityProvision(Strategy):

    def __init__(self):

        super().__init__("amm_lp")


    def generate_return(self, state):

        # ------------------------------------------
        # Fee income
        # ------------------------------------------

        fee_income = (
            0.06
            * state.liquidity
        )


        # ------------------------------------------
        # Convex impermanent loss
        # ------------------------------------------

        volatility_drag = (
            -0.25
            * state.volatility**2
        )

        trend_drag = (
            -0.18
            * state.trend**2
        )


        # ------------------------------------------
        # Liquidity deterioration
        # ------------------------------------------

        liquidity_penalty = (
            -0.10
            * state.leverage_stress
        )


        mean_return = (

            fee_income

            + volatility_drag

            + trend_drag

            + liquidity_penalty
        )


        # ------------------------------------------
        # Tail depegging / liquidity events
        # ------------------------------------------

        if state.regime == "panic":

            if np.random.rand() < 0.12:

                return np.random.uniform(
                    -0.35,
                    -0.12
                )

            realized_vol = 0.10

        elif state.regime == "stress":

            realized_vol = 0.06

        else:

            realized_vol = 0.03


        return np.random.normal(
            mean_return,
            realized_vol
        )