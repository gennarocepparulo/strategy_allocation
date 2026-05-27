"""
environment.py

Central DeFi simulation environment.
"""

from src.core.simulation_result import (
    SimulationResult
)


class DeFiEnvironment:

    def __init__(
        self,
        state_simulator,
        strategies,
        allocation_policy,
        portfolio_engine,
        risk_engine,
    ):

        self.state_simulator = state_simulator

        self.strategies = strategies

        self.allocation_policy = allocation_policy

        self.portfolio_engine = portfolio_engine

        self.risk_engine = risk_engine


    def step(self, state, portfolio):

        # ----------------------------------------------------
        # 1. Regime / state transition
        # ----------------------------------------------------

        next_state = self.state_simulator.step(
            state
        )


        # ----------------------------------------------------
        # 2. Generate strategy returns
        # ----------------------------------------------------

        strategy_returns = {

            name: strategy.generate_return(
                next_state
            )

            for name, strategy
            in self.strategies.items()
        }


        # ----------------------------------------------------
        # 3. Compute allocation weights
        # ----------------------------------------------------

        weights = (
            self.allocation_policy.compute_weights(
                next_state,
                portfolio
            )
        )


        # ----------------------------------------------------
        # 4. Update portfolio
        # ----------------------------------------------------

        new_portfolio = (
            self.portfolio_engine.update(
                portfolio,
                strategy_returns,
                weights
            )
        )


        # ----------------------------------------------------
        # 5. Compute risk metrics
        # ----------------------------------------------------

        risk_metrics = (
            self.risk_engine.evaluate(
                new_portfolio,
                next_state
            )
        )


        # ----------------------------------------------------
        # 6. Return simulation step
        # ----------------------------------------------------

        return SimulationResult(

            state=next_state,

            portfolio=new_portfolio,

            returns=strategy_returns,

            weights=weights,

            risk_metrics=risk_metrics,
        )