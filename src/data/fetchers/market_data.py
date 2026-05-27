"""
market_data.py

Historical market data retrieval for
empirical volatility calibration.
"""

import yfinance as yf
import pandas as pd


def fetch_price_data(
    ticker="BTC-USD",
    start="2022-01-01",
    end="2025-01-01"
):

    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True
    )

    return data[["Close"]]