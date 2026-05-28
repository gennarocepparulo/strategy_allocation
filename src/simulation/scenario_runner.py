"""
scenario_runner.py

Runs comparative allocation experiments.
"""

from src.parameters import N_STEPS


class ScenarioRunner:

    def __init__(self, monte_carlo_engine):

        self.monte_carlo_engine = monte_carlo_engine

    def compare_policies(
        self,
        policies,
        initial_state,
        n_paths=100,
        n_steps=250
    ):

        results = {}

        for policy_name, environment in policies.items():

            engine = self.monte_carlo_engine.__class__(
                path_generator=
                    self.monte_carlo_engine.path_generator.__class__(
                        environment
                    )
            )

            simulations = engine.run(
                initial_state=initial_state,
                n_paths=n_paths,
                horizon=N_STEPS
            )

            results[policy_name] = simulations

        return results