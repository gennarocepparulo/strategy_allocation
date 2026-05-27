"""
distribution.py

Distribution diagnostics.
"""

import numpy as np

from scipy.stats import (
    skew,
    kurtosis
)


def compute_skewness(returns):

    if len(returns) < 3:
        return np.nan

        return pd.Series(
        returns
    ).skew()
    


def compute_kurtosis(returns):

    if len(returns) < 3:
        return np.nan
        return pd.Series(
        returns   ).kurtosis()  
    

       