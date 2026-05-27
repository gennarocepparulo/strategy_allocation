"""
carry.py

Leveraged carry strategy.
"""

import numpy as np

from .strategy_base import Strategy


class LeveragedCarry(Strategy):

    def __init__(self):

        super().__init__("leveraged_carry")


    def generate_return(self, state):

        # --------------------------------------------------
        # Positive carry environment
        # --------------------------------------------------

        carry_component = 0.12 * state.funding

        trend_component = 0.04 * state.trend


        # --------------------------------------------------
        # Convex fragility penalties
        # --------------------------------------------------

        stress_penalty = (
            -0.35
            * state.leverage_stress**2
        )

        volatility_penalty = (
            -0.20
            * state.volatility**2
        )


        # --------------------------------------------------
        # Funding compression during stress
        # --------------------------------------------------

        funding_crash = (
            -0.10
            * state.volatility
            * state.leverage_stress
        )


        # --------------------------------------------------
        # Base expected return
        # --------------------------------------------------

        mean_return = (

            carry_component

            + trend_component

            + stress_penalty

            + volatility_penalty

            + funding_crash
        )


        # --------------------------------------------------
        # Regime-specific tail events
        # --------------------------------------------------

        if state.regime == "panic":

            # liquidation cascade probability

            if np.random.rand() < 0.20:

                jump_loss = np.random.uniform(
                    -0.45,
                    -0.20
                )

                return jump_loss

            realized_vol = 0.15

        elif state.regime == "stress":

            realized_vol = 0.08

        else:

            realized_vol = 0.04


        # --------------------------------------------------
        # Final realized return
        # --------------------------------------------------

        realized_return = np.random.normal(

            mean_return,

            realized_vol
        )

        return realized_return