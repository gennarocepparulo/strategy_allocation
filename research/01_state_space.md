1. Overview
2. State Representation
3. State Variables
4. Observable vs Latent Components
5. Economic Interpretation
6. Strategy Dependence
7. Probabilistic Interpretation
8. Future Extensions

# State Space

## Overview

The DeFi ecosystem is modeled as a stochastic market environment whose dynamics evolve through changing volatility, liquidity, leverage, funding, and trend conditions.

Rather than assuming static expected returns, strategy payoffs are modeled conditionally on the market state:

\[
R_i \mid X_t
\]

where:
- \(R_i\) represents the payoff process of strategy \(i\),
- \(X_t\) represents the regime state vector.

The objective of the state-space framework is to characterize:
- market opportunity,
- fragility conditions,
- allocation admissibility,
- and regime-dependent payoff dynamics.

The framework therefore studies how market states influence:
- expected returns,
- tail risk,
- liquidity sensitivity,
- leverage stability,
- and portfolio robustness.

---

# State Representation

The market environment is represented by the state vector:

\[
X_t =
(\sigma_t, L_t, U_t, F_t, T_t)
\]

where:

| Variable | Interpretation |
|---|---|
| \( \sigma_t \) | Volatility regime |
| \( L_t \) | Liquidity conditions |
| \( U_t \) | Utilization and leverage stress |
| \( F_t \) | Funding and basis conditions |
| \( T_t \) | Trend and directional structure |

The state vector defines the evolving opportunity and risk structure of the DeFi ecosystem.

Strategies are evaluated conditionally on:
\[
R_i \mid X_t
\]

rather than through static APY assumptions.

---

# State Variables

# 1. Volatility State \( \sigma_t \)

## Interpretation

The volatility state represents:
- realized volatility,
- jump intensity,
- volatility clustering,
- directional instability.

Volatility is a primary determinant of:
- liquidation probability,
- leverage admissibility,
- convexity exposure,
- and inventory drift.

---

## Possible Proxies

| Proxy | Meaning |
|---|---|
| Realized volatility | Short-term variance |
| Implied volatility | Forward uncertainty |
| Volatility of volatility | Variance instability |
| Liquidation frequency | Endogenous stress proxy |

---

## Economic Interpretation

High volatility:
- increases liquidation intensity,
- destabilizes leverage,
- damages short-convexity strategies.

Low volatility:
- encourages leverage expansion,
- carry accumulation,
- and yield compression.

---

# 2. Liquidity State \( L_t \)

## Interpretation

The liquidity state represents:
- market depth,
- slippage elasticity,
- withdrawal capacity,
- liquidation absorption ability.

Liquidity determines:
- whether positions can unwind efficiently,
- whether stress propagates systemically,
- and whether leverage remains stable.

---

## Possible Proxies

| Proxy | Meaning |
|---|---|
| DEX depth | Market capacity |
| TVL | Capital availability |
| Slippage | Liquidity elasticity |
| Stablecoin reserves | Systemic liquidity |

---

## Economic Interpretation

Liquidity compression:
- amplifies volatility,
- accelerates liquidation cascades,
- destabilizes carry systems,
- and increases endogenous fragility.

Abundant liquidity:
- stabilizes market functioning,
- supports leverage expansion,
- and improves execution quality.

---

# 3. Utilization / Stress State \( U_t \)

## Interpretation

The utilization state represents:
- borrow demand,
- recursive leverage intensity,
- collateral scarcity,
- system leverage pressure.

---

## Possible Proxies

| Proxy | Meaning |
|---|---|
| Aave utilization | Leverage demand |
| Borrow APR | Capital scarcity |
| Open interest | Speculative leverage |
| Stablecoin borrow rates | Stress intensity |

---

## Economic Interpretation

High utilization:
- boosts lending yield,
- increases leverage sensitivity,
- tightens liquidation geometry,
- and amplifies reflexive instability.

Low utilization:
- reduces carry opportunities,
- weakens lending profitability,
- and signals deleveraging conditions.

---

# 4. Funding / Basis State \( F_t \)

## Interpretation

The funding state represents:
- perpetual funding conditions,
- futures basis spreads,
- carry attractiveness,
- cross-market positioning imbalance.

---

## Possible Proxies

| Proxy | Meaning |
|---|---|
| Perpetual funding rates | Directional crowding |
| Futures basis | Carry premium |
| LST spread | Staking stress |
| Stablecoin premium | Liquidity imbalance |

---

## Economic Interpretation

Funding conditions govern:
- market-neutral carry profitability,
- basis convergence opportunities,
- and leverage incentives.

Funding instability may trigger:
- carry unwinds,
- spread dislocations,
- and liquidity fragmentation.

---

# 5. Trend State \( T_t \)

## Interpretation

The trend state represents:
- directional persistence,
- market structure,
- trend stability,
- momentum conditions.

---

## Possible Proxies

| Proxy | Meaning |
|---|---|
| Momentum | Directional persistence |
| Moving averages | Trend structure |
| Market breadth | Participation quality |
| Trend volatility | Regime stability |

---

## Economic Interpretation

Trend dynamics influence:
- LP inventory drift,
- leverage profitability,
- funding persistence,
- and volatility structure.

Persistent trends:
- favor directional carry strategies,
- while damaging range-dependent positioning.

---

# Observable vs Latent States

Some state variables are directly observable, while others represent latent structural conditions inferred from market behavior.

| Variable | Type |
|---|---|
| Realized volatility | Observable |
| Liquidity depth | Observable |
| Borrow utilization | Observable |
| Funding rates | Observable |
| Reflexive stress buildup | Latent |
| Market confidence | Latent |
| Fragility accumulation | Latent |

This distinction becomes important for future extensions involving:
- Hidden Markov Models,
- Bayesian filtering,
- latent regime inference,
- and probabilistic state estimation.

---

# Probabilistic Interpretation

The market state evolves stochastically through both continuous dynamics and discontinuous stress events.

A generic representation is:

\[
dX_t
=
\mu(X_t,t)dt
+
\Sigma(X_t,t)dW_t
+
J_t dN_t
\]

where:
- \( \mu(X_t,t) \) represents drift dynamics,
- \( \Sigma(X_t,t)dW_t \) represents stochastic diffusion,
- \( J_t dN_t \) represents jump dynamics and stress transitions.

Diffusion terms represent:
- ordinary market evolution,
- gradual regime adaptation.

Jump processes represent:
- liquidation cascades,
- funding dislocations,
- liquidity shocks,
- and endogenous stress propagation.

Strategy payoffs are therefore conditional on evolving state dynamics rather than static expected returns.

---

# Interpretation for Portfolio Construction

The objective of the framework is not to identify universally optimal strategies.

Instead, the framework studies:
- which strategies are admissible under specific market conditions,
- how payoff distributions evolve across regimes,
- and how capital should be dynamically allocated under uncertainty.

The relevant object is therefore:

\[
R_i \mid X_t
\]

rather than:
\[
\mathbb{E}[R_i]
\]

alone.

This implies that:
- identical expected yields may conceal radically different risk geometries,
- liquidity sensitivity,
- drawdown structures,
- and regime fragility.

---

# Future Extensions

Future iterations of the framework may extend the state-space representation through:
- hidden-state regime estimation,
- stochastic volatility models,
- endogenous liquidation feedback,
- network-based contagion dynamics,
- reinforcement learning allocation policies,
- and dynamic stochastic control.

The state-space framework serves as the foundational layer for:
1. Strategy-regime mapping,
2. Monte Carlo simulation,
3. Dynamic allocation,
4. Robust portfolio optimization,
5. Experimental live deployment.