1. Overview
2. Conditional Payoff Representation
3. Distributional Properties
4. Strategy-Specific Conditional Structures
5. Regime Dependence
6. Path Dependence
7. Robustness vs Yield
8. Implications for Allocation

# Conditional Payoffs

## Overview

Traditional DeFi analysis often evaluates strategies through static metrics such as:
- APY,
- historical return,
- or nominal yield.

This framework instead models DeFi strategies as stochastic payoff systems whose behavior depends on evolving market regimes.

The relevant object is therefore not:

\[
\mathbb{E}[R_i]
\]

alone, but the conditional payoff distribution:

\[
R_i \mid X_t = x
\]

where:
- \(R_i\) is the payoff process of strategy \(i\),
- \(X_t\) is the market state vector,
- \(x\) represents a specific market regime.

This shift transforms the analysis from:
- deterministic yield estimation

toward:
- probabilistic regime-dependent portfolio engineering.

---

# Conditional Payoff Representation

Each strategy is modeled as a stochastic payoff engine conditional on the market state.

Formally:

\[
R_i \mid X_t = x
\sim
\mathcal{D}_{i,x}
\]

where:
- \(\mathcal{D}_{i,x}\) denotes the payoff distribution associated with strategy \(i\) under regime \(x\).

The distribution itself changes dynamically as:
- volatility evolves,
- liquidity conditions change,
- leverage accumulates,
- funding conditions shift,
- and market structure transitions across regimes.

This implies that:
- expected returns,
- tail behavior,
- drawdown geometry,
- and payoff asymmetry

are all state-dependent quantities.

---

# Distributional Properties

The framework studies the entire conditional distribution rather than only its mean.

Relevant properties include:

| Property | Interpretation |
|---|---|
| Mean | Expected return |
| Variance | Dispersion of returns |
| Skewness | Asymmetry of payoff distribution |
| Kurtosis | Tail heaviness |
| Tail loss probability | Extreme downside exposure |
| Drawdown geometry | Pathwise capital deterioration |
| Liquidity sensitivity | Dependence on market depth |
| Convexity exposure | Nonlinear response to volatility |

The objective is to understand how these properties evolve under different market states.

---

# Strategy-Specific Conditional Structures

# 1. Passive Lending

## Conditional Structure

\[
R_{\text{lend}} \mid X_t
\]

depends primarily on:
- utilization conditions,
- stablecoin stability,
- collateral market quality,
- liquidity stress.

---

## Distributional Characteristics

Typical structure:
- relatively stable median payoff,
- negatively skewed tail events,
- rare but severe stress losses.

---

## Dominant Conditional Risks

- utilization collapse,
- liquidity withdrawal,
- collateral insolvency,
- stablecoin depeg events.

---

# 2. Leveraged Carry

## Conditional Structure

\[
R_{\text{carry}} \mid X_t
\]

depends on:
- volatility regime,
- leverage intensity,
- collateral dynamics,
- funding conditions.

---

## Distributional Characteristics

Typical structure:
- smooth carry under calm regimes,
- strong negative convexity during stress,
- liquidation boundary effects.

---

## Dominant Conditional Risks

- first-passage liquidation,
- volatility expansion,
- collateral depeg,
- liquidity compression.

---

# 3. AMM Liquidity Provision

## Conditional Structure

\[
R_{\text{LP}} \mid X_t
\]

depends on:
- realized volatility,
- directional persistence,
- trading volume,
- liquidity conditions.

---

## Distributional Characteristics

Typical structure:
- fee accumulation under stable regimes,
- inventory drift under trends,
- nonlinear downside under directional escape.

---

## Dominant Conditional Risks

- impermanent loss,
- inventory concentration,
- jump volatility,
- short convexity exposure.

---

# 4. Basis / Relative Value Strategies

## Conditional Structure

\[
R_{\text{basis}} \mid X_t
\]

depends on:
- funding persistence,
- spread convergence,
- exchange liquidity,
- leverage conditions.

---

## Distributional Characteristics

Typical structure:
- compressed variance under stable conditions,
- occasional spread dislocations,
- liquidity-sensitive tail events.

---

## Dominant Conditional Risks

- basis inversion,
- funding instability,
- liquidity fragmentation,
- counterparty exposure.

---

# 5. Volatility Selling

## Conditional Structure

\[
R_{\text{vol}} \mid X_t
\]

depends on:
- realized volatility,
- volatility clustering,
- jump intensity,
- liquidity depth.

---

## Distributional Characteristics

Typical structure:
- high frequency small gains,
- negatively skewed tails,
- nonlinear drawdown acceleration.

---

## Dominant Conditional Risks

- volatility spikes,
- jump risk,
- gamma exposure,
- liquidity evaporation.

---

# 6. Reflexive Yield Systems

## Conditional Structure

\[
R_{\text{reflexive}} \mid X_t
\]

depends on:
- collateral confidence,
- recursive leverage expansion,
- liquidity availability,
- market reflexivity.

---

## Distributional Characteristics

Typical structure:
- strong returns during expansionary regimes,
- unstable behavior under stress,
- endogenous collapse dynamics.

---

## Dominant Conditional Risks

- confidence collapse,
- recursive deleveraging,
- liquidity spirals,
- endogenous instability.

---

# Regime Dependence

The same strategy may exhibit radically different payoff behavior across market regimes.

For example:

| Regime | LP Strategy Behavior |
|---|---|
| Low volatility + high volume | Stable fee harvesting |
| Strong directional trend | Inventory drift |
| Liquidity stress | Convexity losses |
| Panic regime | Severe nonlinear drawdowns |

This implies that:
- no strategy is universally optimal,
- payoff quality is regime dependent,
- allocation decisions must be state conditioned.

---

# Path Dependence

Many DeFi strategies are path dependent rather than memoryless.

The realized trajectory of the market matters, not only terminal outcomes.

Examples:

| Strategy | Source of Path Dependence |
|---|---|
| Leveraged carry | Liquidation boundaries |
| LPing | Inventory drift |
| Funding carry | Funding persistence |
| Reflexive leverage | Recursive deleveraging |

This motivates:
- Monte Carlo simulation,
- regime path generation,
- stopping-time analysis,
- and stochastic process modeling.

---

# Robustness vs Yield

High nominal yield does not necessarily imply attractive allocation quality.

Two strategies with identical expected returns may exhibit:
- radically different drawdown structures,
- liquidity sensitivity,
- skewness,
- and tail behavior.

The framework therefore prioritizes:
- robustness,
- regime consistency,
- pathwise stability,
- and conditional payoff quality

rather than static yield comparisons alone.

---

# Implications for Portfolio Construction

The portfolio problem is therefore not:

\[
\max \mathbb{E}[R]
\]

alone.

Instead, allocation depends on:
- conditional payoff distributions,
- regime transitions,
- liquidity conditions,
- leverage admissibility,
- and drawdown geometry.

The relevant allocation object becomes:

\[
w_t = \pi(X_t)
\]

where:
- \(X_t\) is the market state,
- \(\pi\) is a regime-aware allocation policy.

This transforms portfolio construction into:
- a probabilistic,
- state-dependent,
- dynamically adaptive process.

---

# Research Direction

The conditional payoff framework serves as the probabilistic foundation for:

1. Strategy-regime mapping,
2. Monte Carlo simulation,
3. Dynamic allocation,
4. Regime-aware optimization,
5. Fragility-adjusted portfolio construction,
6. Experimental live deployment.

Future extensions may include:
- stochastic volatility models,
- hidden-state estimation,
- jump diffusion processes,
- endogenous liquidation feedback,
- and reinforcement learning allocation policies.