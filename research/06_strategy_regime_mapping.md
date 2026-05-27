# Strategy–Regime Mapping

## Overview

The objective of the framework is not to identify universally optimal DeFi strategies.

Instead, the framework studies:
- which strategies are admissible under specific market conditions,
- how payoff quality changes across regimes,
- and how capital should be dynamically allocated under uncertainty.

Strategy quality is therefore modeled conditionally on the market state:

\[
R_i \mid X_t
\]

where:
- \(R_i\) represents the payoff process of strategy \(i\),
- \(X_t\) represents the regime state vector.

This transforms portfolio construction into:
- a probabilistic,
- state-dependent,
- dynamically adaptive allocation problem.

---

# Strategy Admissibility

A strategy is considered admissible when:
- its payoff structure remains economically attractive,
- its fragility remains bounded,
- and its capital impairment risk remains acceptable under a given regime.

Admissibility is therefore conditional rather than universal.

Formally:

\[
\mathcal{A}_i(X_t)
\]

where:
- \(\mathcal{A}_i\) denotes the admissibility of strategy \(i\),
- conditioned on the current market state \(X_t\).

A strategy may be:
- highly efficient in one regime,
- structurally unstable in another.

---

# Regime Classification

The market state is represented through:

\[
X_t =
(\sigma_t, L_t, U_t, F_t, T_t)
\]

where:
- volatility,
- liquidity,
- leverage stress,
- funding conditions,
- and trend structure

jointly define the regime environment.

---

## Example Regimes

| Regime | Characteristics |
|---|---|
| Carry Expansion | Low volatility, abundant liquidity |
| Stable Range | Moderate volatility, strong volume |
| Bull Trend | Positive momentum and funding |
| Liquidity Compression | Deteriorating market depth |
| Stress Transition | Rising volatility and leverage pressure |
| Cascade Panic | Liquidation-driven instability |
| Recovery Phase | Volatility normalization and recapitalization |

These regimes represent probabilistic regions of the state space rather than deterministic labels.

---

# Expected Capital Evolution

Let:

\[
W_t
\]

denote portfolio wealth.

The portfolio evolves according to:

\[
W_{t+1}
=
W_t
\left(
1+\sum_i w_{i,t}R_{i,t+1}
\right)
\]

where:
- \(w_{i,t}\) is the portfolio allocation to strategy \(i\),
- \(R_{i,t+1}\) is the conditional stochastic payoff.

---

## Long-Run Growth Objective

The framework does not optimize static expected return alone.

Instead, the relevant objective is long-run compounded growth:

\[
\max
\mathbb{E}[\log W_T]
\]

This formulation:
- incorporates path dependence,
- penalizes catastrophic drawdowns,
- and captures geometric compounding effects.

The objective therefore becomes:
- robust long-horizon capital growth under stochastic regime transitions.

---

# Strategy–Regime Compatibility

Different strategies exhibit different payoff quality across market states.

---

## Passive Lending

| Favorable Conditions | Fragile Conditions |
|---|---|
| Stable liquidity | Stablecoin stress |
| Moderate volatility | Liquidity withdrawal |
| Strong borrow demand | Collateral insolvency |

---

## Leveraged Carry

| Favorable Conditions | Fragile Conditions |
|---|---|
| Low volatility | Volatility expansion |
| Stable funding | Liquidity compression |
| Persistent trends | Depeg events |

---

## AMM Liquidity Provision

| Favorable Conditions | Fragile Conditions |
|---|---|
| Range-bound markets | Directional breakout |
| High volume | Jump volatility |
| Stable liquidity | Inventory concentration |

---

## Basis / Relative Value

| Favorable Conditions | Fragile Conditions |
|---|---|
| Stable funding spreads | Funding inversion |
| Market stability | Liquidity fragmentation |
| Carry persistence | Exchange stress |

---

## Volatility Selling

| Favorable Conditions | Fragile Conditions |
|---|---|
| Volatility compression | Volatility spikes |
| Mean-reverting markets | Tail events |
| Stable liquidity | Liquidity evaporation |

---

## Reflexive Yield Systems

| Favorable Conditions | Fragile Conditions |
|---|---|
| Expansionary liquidity | Confidence collapse |
| Recursive growth | Reflexive deleveraging |
| Strong collateral confidence | Liquidity spirals |

---

# Robustness Dimensions

The framework defines robustness as the stability of payoff quality across changing market conditions.

Robustness is not equivalent to low volatility alone.

Instead, robustness depends on multiple dimensions:

| Dimension | Interpretation |
|---|---|
| Drawdown persistence | Duration of capital impairment |
| Tail sensitivity | Exposure to extreme losses |
| Liquidity dependence | Reliance on market depth |
| Regime sensitivity | Stability across regimes |
| Leverage admissibility | Stability under volatility expansion |
| Funding dependence | Reliance on carry persistence |
| Path dependence | Sensitivity to realized trajectories |

Robustness therefore becomes a multidimensional property of the allocation structure.

---

# Allocation Constraints

Portfolio construction is constrained by:
- liquidity,
- leverage,
- drawdown geometry,
- and regime conditions.

The framework therefore studies constrained stochastic allocation rather than unconstrained yield maximization.

---

# Liquidity Constraints

Strategies dependent on deep market liquidity may become unstable during:
- stress events,
- liquidation cascades,
- liquidity fragmentation.

Constraint representation:

\[
\mathcal{L}(w_t)
\leq
L_{\max}
\]

where:
- \(\mathcal{L}(w_t)\) measures liquidity dependence.

---

# Drawdown Constraints

Capital impairment must remain probabilistically bounded.

A generic representation is:

\[
\mathbb{P}(D_t > D^*)
\leq
\epsilon
\]

where:
- \(D_t\) represents portfolio drawdown,
- \(D^*\) is the maximum admissible drawdown,
- \(\epsilon\) is the acceptable tail probability.

---

# Leverage Constraints

Leverage admissibility depends on:
- volatility,
- liquidity,
- and funding stability.

Constraint representation:

\[
\Lambda(w_t,X_t)
\leq
\Lambda_{\max}
\]

where:
- leverage tolerance changes dynamically across regimes.

---

# Liquidity Reserve Constraints

The framework may require dynamic reserve allocation:

\[
w_{\text{cash},t}
\geq
c(X_t)
\]

where:
- reserve requirements depend on regime conditions.

This creates:
- optionality,
- deployment flexibility,
- and stress resilience.

---

# Conditional Fragility

Fragility is modeled conditionally on the regime state.

A strategy may exhibit:
- stable performance under one regime,
- nonlinear deterioration under another.

Fragility therefore depends on:
- volatility structure,
- liquidity conditions,
- leverage accumulation,
- and endogenous feedback dynamics.

---

# Regime Mismatch Risk

One of the primary sources of instability is regime mismatch.

A strategy becomes fragile when:
- its payoff geometry is inconsistent with the surrounding market state.

Examples include:
- leveraged carry during volatility expansion,
- LP positioning during directional escape,
- volatility selling during stress transitions.

Formally:

\[
\mathcal{M}(s_i,X_t)
\]

where:
- \(\mathcal{M}\) measures the mismatch between strategy structure and regime conditions.

This concept becomes central for:
- allocation adjustment,
- exposure reduction,
- and dynamic positioning.

---

# Dynamic Allocation Policies

Portfolio allocation is represented as:

\[
w_t = \pi(X_t)
\]

where:
- \(X_t\) is the market state,
- \(\pi\) is the allocation policy.

Allocation therefore adapts dynamically according to:
- volatility conditions,
- liquidity structure,
- leverage stress,
- funding dynamics,
- and trend persistence.

This transforms portfolio construction into:
- a stochastic control problem,
- rather than static optimization.

---

# Allocation Geometry

The portfolio is interpreted as a collection of interacting exposures rather than isolated yield sources.

Each strategy embeds implicit exposure to:
- liquidity,
- volatility,
- leverage,
- funding structure,
- and reflexive market dynamics.

Portfolio quality therefore depends on:
- diversification across payoff geometries,
- robustness across regimes,
- and dynamic exposure balancing.

---

# Implications for Portfolio Engineering

The framework does not seek:
- maximum nominal APY,
- nor static mean-variance efficiency.

Instead, the objective is:
- robust long-horizon compounding,
- adaptive positioning,
- and probabilistic capital allocation under uncertainty.

This transforms DeFi portfolio construction into:
- a regime-aware,
- stochastic,
- dynamically adaptive engineering problem.

---

# Future Extensions

Future research directions may include:

1. Monte Carlo regime simulation,
2. Dynamic leverage control,
3. Regime-aware rebalancing policies,
4. Hidden-state estimation,
5. Reinforcement learning allocation,
6. Fragility-adjusted optimization,
7. Stochastic control frameworks,
8. Experimental live deployment.

These extensions will progressively transform the framework into a fully probabilistic DeFi portfolio engineering system.