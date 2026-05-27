"""
path_generator.py

Generates full stochastic simulation paths.
"""

from src.core.portfolio import Portfolio


class PathGenerator:

    def __init__(self, environment):

        self.environment = environment

    def generate_path(
        self,
        initial_state,
        n_steps=250,
        initial_capital=10_000
    ):

        portfolio = Portfolio(
            capital=initial_capital,
            weights={},
            history=[initial_capital]
        )

        current_state = initial_state

        simulation_history = []

        for _ in range(n_steps):

            step_result = self.environment.step(
                current_state,
                portfolio
            )

            simulation_history.append(step_result)

            current_state = step_result.state

            portfolio = step_result.portfolio

        return simulation_history