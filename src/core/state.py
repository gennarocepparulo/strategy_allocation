"""
state.py

Core market state representation.
"""

from dataclasses import dataclass


@dataclass
class MarketState:

    regime: str

    volatility: float

    liquidity: float

    funding: float

    leverage_stress: float

    trend: float

    timestamp: int = 0