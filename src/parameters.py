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
    "stress",
    "panic",
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
    [0.92, 0.08, 0.00, 0.00],

    # stable_range
    [0.03, 0.92, 0.05, 0.00],

    # stress
    [0.00, 0.08, 0.88, 0.04],

    # panic
    [0.00, 0.00, 0.18, 0.82]
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

    
}


# ============================================================
# SIMULATION PARAMETERS
# ============================================================

N_STEPS = 250

N_PATHS = 1000

INITIAL_CAPITAL = 10_000