"""
state_simulator.py

Simulates probabilistic regime evolution.
"""

import numpy as np

from src.core.state import MarketState

from src.states.regime import (
    REGIME_PARAMETERS,
    REGIMES,
    REGIME_TO_INDEX,
    INDEX_TO_REGIME
)

from src.parameters import TRANSITION_MATRIX


class StateSimulator:

    def __init__(

        self,

        transition_matrix=None
    ):

        # Use empirical/custom matrix if provided

        if transition_matrix is not None:

            self.transition_matrix = transition_matrix

        else:

            self.transition_matrix = TRANSITION_MATRIX


        # Regime mappings

        self.regimes = REGIMES

        self.regime_to_index = REGIME_TO_INDEX

        self.index_to_regime = INDEX_TO_REGIME

        

    def transition_regime(self, current_regime):

        idx = self.regime_to_index[current_regime]

        probs = self.transition_matrix[idx]

        next_idx = np.random.choice(
            len(self.regimes),
            p=probs
        )

        return self.regimes[next_idx]

    def generate_state(
        self,
        regime,
        timestamp=0
    ):

        params = REGIME_PARAMETERS[regime]

        return MarketState(

            regime=regime,

            volatility=np.random.normal(
                params["volatility"],
                0.05
            ),

            liquidity=np.random.normal(
                params["liquidity"],
                0.05
            ),

            funding=np.random.normal(
                params["funding"],
                0.05
            ),

            leverage_stress=np.random.normal(
                params["leverage_stress"],
                0.05
            ),

            trend=np.random.normal(
                params["trend"],
                0.05
            ),

            timestamp=timestamp
        )

    def step(self, current_state):

        next_regime = self.transition_regime(
            current_state.regime
        )

        next_state = self.generate_state(
            regime=next_regime,
            timestamp=current_state.timestamp + 1
        )

        return next_state