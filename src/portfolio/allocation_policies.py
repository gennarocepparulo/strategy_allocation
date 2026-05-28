"""
allocation_policies.py

Portfolio allocation policies for the
probabilistic DeFi allocation framework.
"""

from abc import ABC, abstractmethod

import numpy as np


# ============================================================
# REGIME LEVERAGE CONSTRAINTS
# ============================================================

REGIME_MAX_LEVERAGE = {

    "carry": 2.0,

    "stable_range": 1.5,

    "bull_trend": 2.0,

    "stress": 0.75,

    "panic": 0.25,

    "recovery": 1.0,
}


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def normalize_weights(

    weights,

    max_gross_leverage=1.0
):
    """
    Scale weights so that total gross exposure
    does not exceed leverage constraint.
    """

    gross_exposure = sum(

        abs(w)

        for w in weights.values()
    )

    if gross_exposure <= max_gross_leverage:

        return weights

    scaling = (

        max_gross_leverage
        / gross_exposure
    )

    normalized = {

        k: v * scaling

        for k, v in weights.items()
    }

    return normalized


def apply_volatility_targeting(

    weights,

    state,

    target_volatility=0.20
):
    """
    Reduce gross exposure when realized
    regime volatility becomes elevated.
    """

    realized_vol = max(

        state.volatility,

        1e-6
    )

    scaling = min(

        1.0,

        target_volatility
        / realized_vol
    )

    adjusted = {

        k: v * scaling

        for k, v in weights.items()
    }

    return adjusted


# ============================================================
# BASE CLASS
# ============================================================

class AllocationPolicy(ABC):

    @abstractmethod
    def compute_weights(self, state, portfolio):

        pass


# ============================================================
# 1. CARRY MAXIMIZER POLICY
# ============================================================

class CarryMaximizerPolicy(AllocationPolicy):

    """
    Aggressive carry-seeking policy.

    Prioritizes:
    - leveraged carry,
    - volatility harvesting,
    - reflexive systems.
    """

    def compute_weights(self, state, portfolio):

        weights = {

            "passive_lending": 0.05,

            "leveraged_carry": 0.35,

            "amm_lp": 0.20,

            "basis_arbitrage": 0.05,

            "volatility_selling": 0.20,

            "reflexive_yield": 0.15,
        }

        weights = apply_volatility_targeting(

            weights,

            state,

            target_volatility=0.35
        )

        weights = normalize_weights(

            weights,

            max_gross_leverage=
                REGIME_MAX_LEVERAGE[
                    state.regime
                ]
        )

        return weights


# ============================================================
# 2. REGIME ADAPTIVE POLICY
# ============================================================

class RegimeAdaptivePolicy(AllocationPolicy):

    """
    Dynamically adapts positioning
    across market regimes.
    """

    def compute_weights(self, state, portfolio):

        regime = state.regime

        # ----------------------------------------------------
        # CARRY
        # ----------------------------------------------------

        if regime == "carry":

            weights = {

                "passive_lending": 0.10,

                "leveraged_carry": 0.35,

                "amm_lp": 0.25,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.05,
            }

        # ----------------------------------------------------
        # STABLE RANGE
        # ----------------------------------------------------

        elif regime == "stable_range":

            weights = {

                "passive_lending": 0.25,

                "leveraged_carry": 0.15,

                "amm_lp": 0.30,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.05,
            }

        # ----------------------------------------------------
        # BULL TREND
        # ----------------------------------------------------

        elif regime == "bull_trend":

            weights = {

                "passive_lending": 0.05,

                "leveraged_carry": 0.30,

                "amm_lp": 0.35,

                "basis_arbitrage": 0.10,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.15,
            }

        # ----------------------------------------------------
        # STRESS
        # ----------------------------------------------------

        elif regime == "stress":

            weights = {

                "passive_lending": 0.45,

                "leveraged_carry": 0.05,

                "amm_lp": 0.10,

                "basis_arbitrage": 0.30,

                "volatility_selling": 0.00,

                "reflexive_yield": 0.10,
            }

        # ----------------------------------------------------
        # PANIC
        # ----------------------------------------------------

        elif regime == "panic":

            weights = {

                "passive_lending": 0.70,

                "leveraged_carry": 0.00,

                "amm_lp": 0.05,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.00,

                "reflexive_yield": 0.05,
            }

        # ----------------------------------------------------
        # RECOVERY
        # ----------------------------------------------------

        elif regime == "recovery":

            weights = {

                "passive_lending": 0.30,

                "leveraged_carry": 0.15,

                "amm_lp": 0.25,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.00,

                "reflexive_yield": 0.10,
            }

        # ----------------------------------------------------
        # DEFAULT
        # ----------------------------------------------------

        else:

            weights = {

                "passive_lending": 0.30,

                "leveraged_carry": 0.20,

                "amm_lp": 0.20,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.05,
            }

        weights = apply_volatility_targeting(

            weights,

            state,

            target_volatility=0.25
        )

        weights = normalize_weights(

            weights,

            max_gross_leverage=
                REGIME_MAX_LEVERAGE[
                    state.regime
                ]
        )

        return weights


# ============================================================
# 3. ROBUST GROWTH POLICY
# ============================================================

class RobustGrowthPolicy(AllocationPolicy):

    """
    Long-horizon geometric growth policy.

    Focuses on:
    - compounding stability,
    - drawdown minimization,
    - robustness under stress.
    """

    def compute_weights(self, state, portfolio):

        volatility = state.volatility

        stress = state.leverage_stress

        defensive_multiplier = min(

            1.0,

            volatility + stress
        )

        lending_weight = (

            0.30
            + 0.30 * defensive_multiplier
        )

        basis_weight = 0.25

        amm_weight = max(

            0.10,

            0.25
            - 0.10 * defensive_multiplier
        )

        carry_weight = max(

            0.05,

            0.15
            - 0.10 * defensive_multiplier
        )

        vol_weight = max(

            0.00,

            0.05
            - 0.05 * defensive_multiplier
        )

        reflexive_weight = max(

            0.00,

            0.05
            - 0.05 * defensive_multiplier
        )

        total = (

            lending_weight
            + basis_weight
            + amm_weight
            + carry_weight
            + vol_weight
            + reflexive_weight
        )

        weights = {

            "passive_lending":
                lending_weight / total,

            "leveraged_carry":
                carry_weight / total,

            "amm_lp":
                amm_weight / total,

            "basis_arbitrage":
                basis_weight / total,

            "volatility_selling":
                vol_weight / total,

            "reflexive_yield":
                reflexive_weight / total,
        }

        weights = apply_volatility_targeting(

            weights,

            state,

            target_volatility=0.15
        )

        weights = normalize_weights(

            weights,

            max_gross_leverage=
                REGIME_MAX_LEVERAGE[
                    state.regime
                ]
        )

        return weights