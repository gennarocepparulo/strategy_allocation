"""
simulation_step.py

Stores the output of a simulation timestep.
"""

from dataclasses import dataclass


@dataclass
class SimulationStep:

    state: object

    portfolio: object

    returns: dict

    weights: dict

    risk_metrics: dict
    