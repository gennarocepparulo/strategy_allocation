"""
evaluate_policy.py

Unified policy evaluation engine.
"""

import numpy as np

from src.simulation.environment import (
    DeFiEnvironment
)

from src.simulation.monte_carlo import (
    MonteCarloEngine
)

from src.states.state_simulator import (
    StateSimulator
)

from src.strategies import strategies

from src.portfolio.portfolio_engine import (
    PortfolioEngine
)

from src.risk.risk_engine import (
    RiskEngine
)

from src.risk.path_evaluator import (
    evaluate_many_paths
)


def evaluate_policy(

    policy,

    transition_matrix,

    n_paths=500,

    horizon=356,

    initial_capital=10_000,

    initial_regime="stable_range"
):

    simulator = StateSimulator(

        transition_matrix=transition_matrix
    )

    env = DeFiEnvironment(

        state_simulator=simulator,

        strategies=strategies,

        allocation_policy=policy,

        portfolio_engine=PortfolioEngine(),

        risk_engine=RiskEngine(),
    )

    mc = MonteCarloEngine(
        environment=env
    )

    initial_state = simulator.generate_state(

        regime=initial_regime,

        timestamp=0
    )

    wealth_paths = []

    state_paths = []

    for _ in range(n_paths):

        result = mc.run_single_path(

            initial_state=initial_state,

            horizon=horizon,

            initial_capital=initial_capital
        )

        wealth_paths.append(
            result["wealth_history"]
        )

        state_paths.append(
            result["state_history"]
        )

    metrics = evaluate_many_paths(
        wealth_paths
    )

    total_days = 0

    panic_days = 0

    for path in state_paths:

        for state in path:

            total_days += 1

            if state.regime == "panic":

                panic_days += 1

    metrics["mean_panic_fraction"] = (

        panic_days / total_days
    )

    return metrics