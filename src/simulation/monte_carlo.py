"""
monte_carlo.py

Full Monte Carlo simulation engine.
"""

from src.core.portfolio import Portfolio


class MonteCarloEngine:

    def __init__(self, environment):

        self.environment = environment


    def run_single_path(

        self,

        initial_state,

        horizon=356,

        initial_capital=10_000
    ):

        portfolio = Portfolio(

            capital=initial_capital,

            weights={},

            history=[initial_capital]
        )

        current_state = initial_state

        wealth_history = [initial_capital]

        state_history = [initial_state]

        risk_history = []


        for _ in range(horizon):

            result = self.environment.step(

                current_state,

                portfolio
            )

            next_state = result.state

            portfolio = result.portfolio

            risk_metrics = result.risk_metrics


            wealth_history.append(
                portfolio.capital
            )

            state_history.append(
                next_state
            )

            risk_history.append(
                risk_metrics
            )

            current_state = next_state


        return {

            "wealth_history": wealth_history,

            "state_history": state_history,

            "risk_history": risk_history,
        }


    def run_many_paths(

        self,

        initial_state,

        n_paths=100,

        horizon=356,

        initial_capital=10_000
    ):

        all_paths = []

        for _ in range(n_paths):

            path = self.run_single_path(

                initial_state=initial_state,

                horizon=horizon,

                initial_capital=initial_capital
            )

            all_paths.append(path)

        return all_paths