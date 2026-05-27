# Strategy Allocation — Probabilistic DeFi Portfolio Engineering

## Overview

This project studies DeFi portfolio construction as a probabilistic allocation problem under:

* stochastic market regimes,
* endogenous fragility,
* liquidity constraints,
* leverage dynamics,
* and regime-dependent payoff structures.

The framework moves away from:

* protocol-centric analysis,
* static APY optimization,
* and purely deterministic modeling.

Instead, the project develops:

* a regime-aware allocation framework,
* stochastic payoff modeling,
* probabilistic portfolio engineering,
* dynamic positioning logic,
* and fragility-aware capital allocation for DeFi markets.

The long-term objective is to construct a computational research framework capable of:

* simulating market regimes,
* modeling conditional strategy payoffs,
* evaluating robustness under stress,
* calibrating stochastic environments using empirical data,
* and designing adaptive allocation policies under systemic fragility.

The project also includes a practical experimental component:
a small-scale live allocation laboratory (“mini-LBA”) using approximately €10k–15k of capital.

---

# Research Direction

The framework studies DeFi strategies as:

* stochastic payoff engines,

rather than:

* static yield opportunities.

The central object of the framework is:

[
R_i \mid X_t
]

where:

* (R_i) represents the payoff process of strategy (i),
* (X_t) represents the market regime state vector.

This implies that:

* strategy quality is regime dependent,
* fragility evolves dynamically,
* allocation decisions must adapt probabilistically to changing market conditions,
* and long-run survivability becomes as important as raw yield generation.

The project increasingly focuses on:

* optimal capital allocation under systemic instability,
* fragility-constrained growth,
* and probabilistic portfolio engineering for reflexive crypto-financial systems.

---

# Core Conceptual Shift

## Traditional DeFi Perspective

* Protocol-centric analysis,
* APY comparison,
* deterministic yield assumptions,
* isolated liquidation analysis.

---

## Framework Perspective

* Strategy families as stochastic systems,
* conditional payoff distributions,
* regime-aware positioning,
* probabilistic portfolio construction,
* robustness-adjusted allocation,
* dynamic stochastic allocation policies,
* and fragility-aware optimization.

---

# State-Space Framework

The market environment is represented through the state vector:

[
X_t =
(\sigma_t, L_t, U_t, F_t, T_t)
]

where:

| Variable     | Interpretation                  |
| ------------ | ------------------------------- |
| ( \sigma_t ) | Volatility regime               |
| ( L_t )      | Liquidity conditions            |
| ( U_t )      | Utilization and leverage stress |
| ( F_t )      | Funding and basis conditions    |
| ( T_t )      | Trend and directional structure |

The framework studies how these variables influence:

* payoff distributions,
* leverage admissibility,
* liquidity stability,
* portfolio robustness,
* and systemic fragility propagation.

---

# Regime System

The current implementation models market evolution using a probabilistic Markov regime framework.

Current regimes include:

* carry
* stable_range
* stress
* panic

Each regime defines conditional distributions for:

* volatility,
* liquidity,
* funding conditions,
* leverage stress,
* and trend structure.

The framework supports:

* stochastic regime evolution,
* regime persistence,
* panic escalation experiments,
* and empirical transition calibration.

---

# Strategy Universe

The framework abstracts DeFi into strategy families rather than individual protocols.

Current strategy families include:

| Strategy Family         | Core Yield Source                           |
| ----------------------- | ------------------------------------------- |
| Passive Lending         | Borrow demand and utilization               |
| Leveraged Carry         | Recursive leverage and spread amplification |
| AMM Liquidity Provision | Trading fees and volatility harvesting      |
| Basis / Relative Value  | Funding and spread convergence              |
| Volatility Selling      | Variance risk premia                        |
| Reflexive Yield Systems | Recursive collateral expansion              |

Each strategy is modeled through:

* conditional payoff distributions,
* regime sensitivity,
* liquidity dependence,
* nonlinear fragility,
* and crisis exposure.

The current implementation increasingly incorporates:

* convexity effects,
* tail-risk amplification,
* liquidity stress,
* and panic-sensitive payoff dynamics.

---

# Regime-Aware Allocation

Portfolio allocation is modeled dynamically as:

[
w_t = \pi(X_t)
]

where:

* (X_t) is the market state,
* (\pi) is the allocation policy.

This transforms portfolio construction into:

* a probabilistic,
* state-dependent,
* dynamically adaptive process.

Implemented allocation policies currently include:

| Policy         | Description                          |
| -------------- | ------------------------------------ |
| CarryMaximizer | Aggressive carry-seeking allocation  |
| RegimeAdaptive | Dynamic regime-sensitive positioning |
| RobustGrowth   | Survivability-oriented allocation    |

Policies are evaluated comparatively using Monte Carlo simulation under:

* stochastic regime transitions,
* crisis escalation,
* and panic persistence perturbations.

---

# Efficiency–Fragility Framework

A central concept of the project is the trade-off between:

* capital efficiency,
* and structural fragility.

Many DeFi strategies generate elevated yield by implicitly absorbing:

* liquidity risk,
* leverage instability,
* convexity exposure,
* and tail fragility.

The framework therefore studies:

* long-run compounded growth,
* robustness,
* drawdown geometry,
* ruin probability,
* regime mismatch risk,
* and crisis survivability.

The project is progressively evolving toward:

* efficient fragility frontiers,
* and fragility-constrained portfolio optimization.

---

# Current Computational Framework

The current system includes:

## Monte Carlo Simulation Engine

* multi-path stochastic simulation,
* regime-dependent state evolution,
* dynamic portfolio evolution,
* daily crypto-native time convention (365-day framework).

## Comparative Policy Evaluation

* multi-policy comparison,
* panic sensitivity experiments,
* regime-conditioned performance analysis,
* stochastic robustness testing.

## Risk and Fragility Metrics

Implemented metrics include:

### Growth Metrics

* CAGR
* log-growth
* terminal wealth

### Risk Metrics

* volatility
* maximum drawdown
* downside semivariance
* Value-at-Risk (VaR)
* Conditional VaR (CVaR)

### Fragility Metrics

* ruin probability
* time under water
* panic exposure fraction
* worst drawdown
* regime-conditioned performance

---

# Hybrid Calibration

The framework has begun transitioning from partially synthetic simulation toward hybrid empirical calibration.

Current calibration work includes:

* empirical BTC volatility estimation,
* regime persistence estimation,
* transition matrix calibration,
* panic episode analysis,
* regime-conditioned return analysis.

Planned calibration extensions include:

* funding-rate distributions,
* liquidation stress proxies,
* dynamic correlation regimes,
* crisis-period calibration,
* and volatility clustering estimation.

---

# Long-Term Research Direction

The project is evolving toward a generalized framework for:

> optimal capital allocation under systemic fragility.

Key future directions include:

* fragility-constrained optimization,
* endogenous panic dynamics,
* liquidation cascades,
* reflexive leverage systems,
* dynamic correlation structures,
* and efficient fragility frontiers.

The framework ultimately aims to study:

* growth,
* survivability,
* and robustness
  within stochastic crypto-financial systems.

---

# Repository Structure

```text
strategy_allocation/
│
├── notebooks/
│
├── src/
│   ├── calibration/
│   ├── core/
│   ├── optimization/
│   ├── portfolio/
│   ├── research/
│   ├── risk/
│   ├── simulation/
│   ├── states/
│   └── strategies/
│
├── figures/
│
├── research_notes/
│   ├── 01_state_space.md
│   ├── 02_research_questions.md
│   ├── 03_strategy_universe.md
│   ├── 04_conditional_payoffs.md
│   ├── 05_regime_dynamics.md
│   ├── 06_strategy_regime_mapping.md
│   └── 07_efficiency_fragility_frontier.md
│
└── README.md
```

---

# Current Status

Current project status:

* stochastic simulation architecture operational,
* comparative policy evaluation implemented,
* fragility metrics integrated,
* panic sensitivity framework operational,
* hybrid calibration in progress,
* optimization layer under development.

The framework has evolved from isolated DeFi strategy analysis into a broader probabilistic research engine for studying:

* systemic fragility,
* nonlinear payoff structures,
* and adaptive capital allocation under uncertainty.
