"""
strategy_result.py

Stores strategy payoff outputs.
"""

from dataclasses import dataclass


@dataclass
class StrategyResult:

    strategy_name: str

    return_value: float

    volatility: float = 0.0

    tail_risk: float = 0.0