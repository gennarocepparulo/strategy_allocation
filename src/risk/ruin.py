"""
ruin.py

Ruin probability metrics.
"""

import numpy as np


def compute_ruin_probability(
    wealth_paths,
    ruin_threshold=0.5
):

    ruined = 0

    for path in wealth_paths:

        initial_wealth = path[0]

        threshold = (
            ruin_threshold
            * initial_wealth
        )

        if np.min(path) < threshold:

            ruined += 1

    return ruined / len(wealth_paths)