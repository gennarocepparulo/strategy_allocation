"""
portfolio_engine.py

Portfolio capital evolution.
"""

from src.core.portfolio import Portfolio


class PortfolioEngine:

    def update(
        self,
        portfolio,
        strategy_returns,
        weights
    ):

        portfolio_return = 0.0

        for strategy_name, weight in weights.items():

            strategy_return = strategy_returns[strategy_name]

            portfolio_return += (
                weight * strategy_return
            )

        new_capital = (
            portfolio.capital
            * (1 + portfolio_return)
        )

        new_capital = max(
            new_capital,
            1e-8
)

        updated_history = (
            portfolio.history
            + [new_capital]
        )

        return Portfolio(
            capital=new_capital,
            weights=weights,
            history=updated_history
        )