"""
compare_policies.py

Comparative policy evaluation framework.
"""

import pandas as pd

from .evaluate_policy import (
    evaluate_policy
)


def compare_policies(

    policies,

    transition_matrix,

    n_paths=500,

    horizon=356,

    initial_capital=10_000,

    initial_regime="stable_range"
):

    results = []


    # --------------------------------------------------
    # Evaluate each policy
    # --------------------------------------------------

    for policy_name, policy in policies.items():

        metrics = evaluate_policy(

            policy=policy,

            transition_matrix=transition_matrix,

            n_paths=n_paths,

            horizon=horizon,

            initial_capital=initial_capital,

            initial_regime=initial_regime
        )


        metrics["policy"] = policy_name

        results.append(metrics)


    # --------------------------------------------------
    # Convert to DataFrame
    # --------------------------------------------------

    df = pd.DataFrame(results)

    df = df.set_index("policy")

    return df