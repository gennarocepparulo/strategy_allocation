"""
parameters.py

Global configuration parameters for the
probabilistic DeFi allocation framework.
"""

import numpy as np


# ============================================================
# REGIMES
# ============================================================

REGIMES = [
    "carry",
    "stable_range",
    "bull_trend",
    "stress",
    "panic",
    "recovery"
]


REGIME_TO_INDEX = {
    regime: idx
    for idx, regime in enumerate(REGIMES)
}


INDEX_TO_REGIME = {
    idx: regime
    for idx, regime in enumerate(REGIMES)
}


# ============================================================
# TRANSITION MATRIX
# ============================================================

TRANSITION_MATRIX = np.array([

    # carry
    [0.70, 0.20, 0.05, 0.05, 0.00, 0.00],

    # stable_range
    [0.20, 0.60, 0.10, 0.10, 0.00, 0.00],

    # bull_trend
    [0.10, 0.20, 0.60, 0.10, 0.00, 0.00],

    # stress
    [0.05, 0.10, 0.10, 0.50, 0.20, 0.05],

    # panic
    [0.00, 0.00, 0.00, 0.30, 0.50, 0.20],

    # recovery
    [0.20, 0.30, 0.20, 0.10, 0.00, 0.20],
])


# ============================================================
# REGIME PARAMETERS
# ============================================================

REGIME_PARAMETERS = {

    "carry": {
        "volatility": 0.10,
        "liquidity": 0.90,
        "funding": 0.80,
        "leverage_stress": 0.20,
        "trend": 0.10,
    },

    "stable_range": {
        "volatility": 0.20,
        "liquidity": 0.85,
        "funding": 0.50,
        "leverage_stress": 0.30,
        "trend": 0.00,
    },

    "bull_trend": {
        "volatility": 0.25,
        "liquidity": 0.95,
        "funding": 0.90,
        "leverage_stress": 0.40,
        "trend": 0.80,
    },

    "stress": {
        "volatility": 0.70,
        "liquidity": 0.30,
        "funding": -0.20,
        "leverage_stress": 0.80,
        "trend": -0.50,
    },

    "panic": {
        "volatility": 0.95,
        "liquidity": 0.10,
        "funding": -0.60,
        "leverage_stress": 1.00,
        "trend": -0.90,
    },

    "recovery": {
        "volatility": 0.35,
        "liquidity": 0.60,
        "funding": 0.20,
        "leverage_stress": 0.40,
        "trend": 0.30,
    },
}


# ============================================================
# SIMULATION PARAMETERS
# ============================================================

N_STEPS = 250

N_PATHS = 1000

INITIAL_CAPITAL = 10_000