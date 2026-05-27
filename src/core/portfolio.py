"""
portfolio.py

Portfolio state representation.
"""

from dataclasses import dataclass, field


@dataclass
class Portfolio:

    capital: float

    weights: dict = field(default_factory=dict)

    history: list = field(default_factory=list)