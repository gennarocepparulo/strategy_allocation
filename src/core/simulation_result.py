"""
simulation_result.py

Simulation step container.
"""

from dataclasses import dataclass


@dataclass
class SimulationResult:

    state: object

    portfolio: object

    returns: dict

    weights: dict

    risk_metrics: dict