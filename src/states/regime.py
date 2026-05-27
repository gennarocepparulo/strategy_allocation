"""
regime.py

Market regime definitions and parameters.
"""

# ============================================================
# REGIME NAMES
# ============================================================

REGIMES = [

    "carry",

    "stable_range",

    "stress",

    "panic"
]


# ============================================================
# REGIME ↔ INDEX MAPPINGS
# ============================================================

REGIME_TO_INDEX = {

    regime: idx

    for idx, regime in enumerate(REGIMES)
}


INDEX_TO_REGIME = {

    idx: regime

    for idx, regime in enumerate(REGIMES)
}


# ============================================================
# REGIME PARAMETERS
# ============================================================

REGIME_PARAMETERS = {

    "carry": {

        "volatility": 0.20,

        "liquidity": 0.90,

        "funding": 0.80,

        "trend": 0.30,

        "leverage_stress": 0.20,
    },


    "stable_range": {

        "volatility": 0.15,

        "liquidity": 0.95,

        "funding": 0.50,

        "trend": 0.00,

        "leverage_stress": 0.10,
    },



    "stress": {

        "volatility": 0.60,

        "liquidity": 0.40,

        "funding": -0.20,

        "trend": -0.50,

        "leverage_stress": 0.70,
    },


    "panic": {

        "volatility": 0.90,

        "liquidity": 0.20,

        "funding": -0.50,

        "trend": -0.90,

        "leverage_stress": 1.00,
    },


    
}