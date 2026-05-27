# Research Questions

## Overview

This project studies DeFi portfolio construction as a probabilistic allocation problem under stochastic market regimes, endogenous fragility, and liquidity constraints.

The objective is not merely to analyze isolated protocols or maximize nominal yield, but to understand how capital should be dynamically allocated across DeFi strategy families under changing market conditions.

The framework combines:
- stochastic processes,
- regime-aware modeling,
- Monte Carlo simulation,
- dynamic allocation logic,
- and experimental portfolio deployment.

The research direction evolves from:
- protocol fragility diagnostics

toward:
- probabilistic portfolio engineering.

---

# Central Research Question

> How should capital be dynamically allocated across DeFi strategy families under stochastic regime transitions, endogenous market fragility, and changing liquidity conditions?

This question forms the conceptual center of the framework.

---

# Core Research Objectives

The framework seeks to:

1. Model DeFi strategies as stochastic payoff systems,
2. Characterize regime-dependent payoff behavior,
3. Study endogenous fragility dynamics,
4. Construct regime-aware allocation frameworks,
5. Evaluate robustness under stress conditions,
6. Design adaptive portfolio policies,
7. Develop a probabilistic experimental allocation laboratory.

---

# Foundational Questions

# 1. What Is the Appropriate Abstraction Layer for DeFi Strategies?

Traditional DeFi analysis focuses on:
- protocols,
- nominal APY,
- or isolated market opportunities.

This framework instead asks:

> Should DeFi strategies be modeled as stochastic payoff engines conditional on market regimes?

This abstraction allows strategies to be studied through:
- payoff geometry,
- liquidity sensitivity,
- leverage exposure,
- and regime dependence.

---

# 2. How Should Market States Be Represented?

The framework introduces the regime state vector:

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

jointly characterize the market environment.

The project asks:

> Which state variables most strongly determine allocation quality and strategy admissibility?

---

# 3. How Do Strategy Payoffs Change Across Regimes?

Rather than assuming static returns, the framework studies:

\[
R_i \mid X_t
\]

where strategy payoffs depend conditionally on the evolving market state.

Key questions include:

- How does volatility alter payoff geometry?
- How does liquidity compression affect drawdown structure?
- How does leverage amplify regime sensitivity?
- How do funding transitions affect carry profitability?

---

# 4. What Determines Strategy Robustness?

The framework seeks to understand why certain strategies remain structurally stable under changing market conditions while others deteriorate rapidly.

This motivates questions such as:

- Which strategies exhibit regime consistency?
- Which strategies possess hidden convexity exposure?
- Which structures amplify endogenous fragility?
- How does leverage alter pathwise robustness?

The project therefore studies:
- robustness,
- admissibility,
- and drawdown geometry

rather than static return alone.

---

# 5. How Does Endogenous Fragility Emerge?

A major objective of the framework is to study how DeFi systems generate internal instability through:
- recursive leverage,
- automated liquidation,
- liquidity feedback loops,
- and reflexive deleveraging.

Key questions include:

- How does fragility accumulate during stable regimes?
- How do liquidation dynamics propagate stress?
- How do leverage cycles alter regime transitions?
- How does liquidity deterioration amplify instability?

---

# 6. What Is the Relationship Between Efficiency and Fragility?

Many high-yield strategies implicitly sell:
- liquidity,
- convexity,
- or leverage stability.

This motivates the question:

> What is the trade-off between capital efficiency and structural fragility?

The framework therefore seeks to construct:
- efficiency-fragility frontiers,
- robustness-adjusted allocation metrics,
- and regime-aware payoff comparisons.

---

# 7. How Should Allocation Adapt Dynamically?

The framework studies portfolio construction as a dynamic allocation problem:

\[
w_t = \pi(X_t)
\]

where:
- \(X_t\) is the market state,
- \(\pi\) is the allocation policy.

Key questions include:

- How should exposures evolve across regimes?
- When should leverage be reduced?
- When should liquidity reserves increase?
- Which strategies become inadmissible under stress?

This transforms allocation into:
- a probabilistic,
- state-dependent,
- adaptive process.

---

# 8. What Role Should Probabilistic Modeling Play?

The project replaces deterministic assumptions with probabilistic state evolution.

Rather than forecasting single outcomes, the framework studies:
- distributions,
- paths,
- transition probabilities,
- and stress scenarios.

This motivates:
- Monte Carlo simulation,
- stochastic processes,
- hidden-state models,
- jump dynamics,
- and probabilistic allocation policies.

The central idea is:

> Allocation quality depends on the geometry of future distributions rather than static expected returns alone.

---

# 9. How Should Long-Horizon Compounding Be Modeled?

The framework is ultimately concerned with:
- long-horizon capital evolution,
- regime transitions,
- drawdown persistence,
- and dynamic positioning.

This raises questions such as:

- Which strategies compound efficiently across multiple regimes?
- How does path dependence alter long-run growth?
- How should capital be preserved during stress transitions?
- How should allocation adapt under uncertainty?

The relevant optimization problem therefore extends beyond nominal yield maximization.

---

# 10. Can a Practical Experimental Framework Be Constructed?

The project ultimately seeks to bridge:
- theoretical research,
- stochastic modeling,
- and practical allocation.

This motivates the construction of a small-scale experimental allocation laboratory (“mini-LBA”) using approximately €10k–15k of capital.

The objective is not purely speculative deployment, but:
- empirical validation,
- allocation experimentation,
- regime testing,
- and practical portfolio engineering.

---

# Research Philosophy

The framework does not treat DeFi as a collection of isolated protocols.

Instead, the ecosystem is viewed as:
- an evolving stochastic environment,
- populated by interacting payoff systems,
- whose attractiveness depends on changing market states.

The objective is therefore not:
- static optimization,
- nor deterministic forecasting,

but:
- probabilistic allocation,
- adaptive positioning,
- and robust exposure management under uncertainty.

---

# Long-Term Research Direction

Future extensions of the framework may include:

1. Markov regime-switching models,
2. Hidden-state estimation,
3. Monte Carlo portfolio simulation,
4. Endogenous liquidation dynamics,
5. Dynamic stochastic control,
6. Reinforcement learning allocation policies,
7. Regime-aware leverage management,
8. Fragility-adjusted optimization.

The long-term objective is to develop a coherent probabilistic framework for:
- DeFi portfolio engineering,
- adaptive capital allocation,
- and regime-aware positioning.