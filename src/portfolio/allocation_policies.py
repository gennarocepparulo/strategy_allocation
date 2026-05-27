"""
allocation_policy.py

Portfolio allocation policies for the
probabilistic DeFi allocation framework.
"""

from abc import ABC, abstractmethod


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
    Aggressive yield-seeking policy.

    Prioritizes:
    - leverage,
    - carry,
    - reflexive growth,
    - volatility selling.
    """

    def compute_weights(self, state, portfolio):

        return {

            "passive_lending": 0.05,

            "leveraged_carry": 0.35,

            "amm_lp": 0.15,

            "basis_arbitrage": 0.00,

            "volatility_selling": 0.20,

            "reflexive_yield": 0.25,
        }


# ============================================================
# 2. REGIME ADAPTIVE POLICY
# ============================================================

class RegimeAdaptivePolicy(AllocationPolicy):

    """
    Dynamically adapts positioning
    according to market regimes.
    """

    def compute_weights(self, state, portfolio):

        regime = state.regime


        # ----------------------------------------------------
        # CARRY REGIME
        # ----------------------------------------------------

        if regime == "carry":

            return {

                "passive_lending": 0.10,

                "leveraged_carry": 0.40,

                "amm_lp": 0.20,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.05,
            }


        # ----------------------------------------------------
        # STABLE RANGE
        # ----------------------------------------------------

        elif regime == "stable_range":

            return {

                "passive_lending": 0.25,

                "leveraged_carry": 0.20,

                "amm_lp": 0.25,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.05,
            }


        # ----------------------------------------------------
        # BULL TREND
        # ----------------------------------------------------

        elif regime == "bull_trend":

            return {

                "passive_lending": 0.05,

                "leveraged_carry": 0.35,

                "amm_lp": 0.35,

                "basis_arbitrage": 0.10,

                "volatility_selling": 0.05,

                "reflexive_yield": 0.10,
            }


        # ----------------------------------------------------
        # STRESS
        # ----------------------------------------------------

        elif regime == "stress":

            return {

                "passive_lending": 0.50,

                "leveraged_carry": 0.05,

                "amm_lp": 0.15,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.00,

                "reflexive_yield": 0.10,
            }


        # ----------------------------------------------------
        # PANIC
        # ----------------------------------------------------

        elif regime == "panic":

            return {

                "passive_lending": 0.80,

                "leveraged_carry": 0.00,

                "amm_lp": 0.05,

                "basis_arbitrage": 0.10,

                "volatility_selling": 0.00,

                "reflexive_yield": 0.05,
            }


        # ----------------------------------------------------
        # RECOVERY
        # ----------------------------------------------------

        elif regime == "recovery":

            return {

                "passive_lending": 0.35,

                "leveraged_carry": 0.15,

                "amm_lp": 0.20,

                "basis_arbitrage": 0.20,

                "volatility_selling": 0.00,

                "reflexive_yield": 0.10,
            }


        # ----------------------------------------------------
        # DEFAULT
        # ----------------------------------------------------

        return {

            "passive_lending": 0.30,

            "leveraged_carry": 0.20,

            "amm_lp": 0.20,

            "basis_arbitrage": 0.20,

            "volatility_selling": 0.05,

            "reflexive_yield": 0.05,
        }


# ============================================================
# 3. ROBUST GROWTH POLICY
# ============================================================

class RobustGrowthPolicy(AllocationPolicy):

    """
    Long-horizon geometric growth policy.

    Prioritizes:
    - compounding robustness,
    - drawdown control,
    - lower fragility,
    - stable capital growth.
    """

    def compute_weights(self, state, portfolio):

        volatility = state.volatility

        stress = state.leverage_stress


        # Dynamic defensive scaling
        defensive_multiplier = min(
            1.0,
            volatility + stress
        )


        lending_weight = 0.30 + 0.30 * defensive_multiplier

        basis_weight = 0.25

        amm_weight = max(
            0.10,
            0.25 - 0.10 * defensive_multiplier
        )

        carry_weight = max(
            0.05,
            0.15 - 0.10 * defensive_multiplier
        )

        vol_weight = max(
            0.00,
            0.05 - 0.05 * defensive_multiplier
        )

        reflexive_weight = max(
            0.00,
            0.05 - 0.05 * defensive_multiplier
        )


        total = (
            lending_weight
            + basis_weight
            + amm_weight
            + carry_weight
            + vol_weight
            + reflexive_weight
        )


        return {

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