"""
fragility_score.py

Composite systemic fragility functional.
"""

import numpy as np


def normalize_metric(
    value,
    min_value,
    max_value
):

    if max_value == min_value:

        return 0.0

    return (
        value - min_value
    ) / (
        max_value - min_value
    )


DEFAULT_FRAGILITY_WEIGHTS = {

    "drawdown": 0.20,

    "cvar": 0.30,

    "ruin": 0.30,

    "panic": 0.10,

    "underwater": 0.10
}


DEFAULT_NORMALIZATION_RANGES = {

    "drawdown": (0.0, 1.0),

    "cvar": (0.0, 1.0),

    "ruin": (0.0, 1.0),

    "panic": (0.0, 1.0),

    "underwater": (0.0, 365.0)
}


def compute_fragility_score(

    metrics,

    weights=None,

    normalization_ranges=None
):

    if weights is None:

        weights = DEFAULT_FRAGILITY_WEIGHTS

    if normalization_ranges is None:

        normalization_ranges = (
            DEFAULT_NORMALIZATION_RANGES
        )

    raw_components = {

        "drawdown":
            abs(metrics["mean_drawdown"]),

        "cvar":
            abs(metrics["mean_CVaR_5"]),

        "ruin":
            metrics["ruin_probability"],

        "panic":
            metrics["mean_panic_fraction"],

        "underwater":
            metrics["mean_time_under_water"]
    }

    normalized_components = {}

    for key, value in raw_components.items():

        min_value, max_value = (
            normalization_ranges[key]
        )

        normalized_components[key] = (
            normalize_metric(
                value,
                min_value,
                max_value
            )
        )

    fragility_score = 0.0

    for key, value in normalized_components.items():

        fragility_score += (
            weights[key] * value
        )

    return {

        "fragility_score":
            fragility_score,

        "raw_components":
            raw_components,

        "normalized_components":
            normalized_components,

        "weights":
            weights
    }