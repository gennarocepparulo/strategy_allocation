"""
transition_matrix.py

Defines the probabilistic regime transition matrix.
"""

import numpy as np

from .regime import REGIMES

TRANSITION_MATRIX = np.array([

    # carry
    [0.60, 0.20, 0.10, 0.08, 0.00, 0.02],

    # range
    [0.15, 0.55, 0.15, 0.10, 0.00, 0.05],

    # bull
    [0.10, 0.15, 0.60, 0.10, 0.00, 0.05],

    # stress
    [0.00, 0.05, 0.00, 0.55, 0.30, 0.10],

    # cascade
    [0.00, 0.00, 0.00, 0.20, 0.60, 0.20],

    # recovery
    [0.20, 0.35, 0.10, 0.05, 0.00, 0.30],
])

def validate_transition_matrix(matrix):
    """
    Ensure rows sum to 1.
    """

    row_sums = matrix.sum(axis=1)

    return np.allclose(row_sums, 1.0)

if __name__ == "__main__":

    valid = validate_transition_matrix(TRANSITION_MATRIX)

    print("Transition matrix valid:", valid)