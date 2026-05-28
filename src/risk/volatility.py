import numpy as np


def compute_volatility(
    returns,
    annualize=True,
    periods_per_year=365
):
    """
    Compute realized volatility from a return series.

    Parameters
    ----------
    returns : array-like
        Periodic portfolio returns.
    annualize : bool
        Whether to annualize volatility.
    periods_per_year : int
        Number of return observations per year.
        Use 365 for daily crypto data, 252 for traditional markets.

    Returns
    -------
    float
        Realized volatility.
    """

    returns = np.asarray(returns, dtype=float)

    # Remove NaNs and infinities
    returns = returns[np.isfinite(returns)]

    # Need at least 2 observations for sample volatility
    if len(returns) < 2:
        return 0.0

    # Sample standard deviation
    volatility = np.std(
        returns,
        ddof=1
    )

    # Annualize if requested
    if annualize:
        volatility *= np.sqrt(periods_per_year)

    return volatility