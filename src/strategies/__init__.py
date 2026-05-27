"""
Strategy registry.

Exports instantiated strategies.
"""

from .lending import PassiveLending

from .amm import AMMLiquidityProvision

from .carry import LeveragedCarry

from .basis import BasisArbitrage

from .vol_selling import VolatilitySelling

from .reflexive import ReflexiveYield


strategies = {

    "passive_lending":
        PassiveLending(),

    "amm_lp":
        AMMLiquidityProvision(),

    "leveraged_carry":
        LeveragedCarry(),

    "basis_arbitrage":
        BasisArbitrage(),

    "volatility_selling":
        VolatilitySelling(),

    "reflexive_yield":
        ReflexiveYield(),
}