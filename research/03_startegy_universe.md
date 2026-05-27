# Strategy Universe

## Overview

The objective of this framework is to study DeFi strategies as stochastic,
state-dependent payoff systems rather than static yield opportunities.

Instead of focusing on individual protocols, the framework abstracts the
DeFi ecosystem into families of capital allocation mechanisms characterized by:

- payoff structure,
- dominant risk exposures,
- liquidity dependence,
- leverage sensitivity,
- and endogenous fragility channels.

Each strategy is modeled conditionally on the market state:

\[
R_i \mid X_t = x \sim \mathcal{D}_{i,x}
\]

where:

- \(R_i\) represents the payoff process of strategy \(i\),
- \(X_t\) is the regime state vector,
- \(\mathcal{D}_{i,x}\) is the conditional payoff distribution.

The goal is not to identify universally optimal strategies, but to determine:

- which strategies are robust under specific regimes,
- how payoff distributions evolve under stress,
- and how capital should be dynamically allocated across strategy families.

---

# Core Strategy Families

## 1. Passive Lending

### Description

Capital is supplied to lending protocols in exchange for utilization-driven yield.

Examples include:
- stablecoin lending,
- ETH lending,
- isolated collateral markets.

### Yield Source

- borrower demand,
- utilization spread,
- liquidity scarcity premium.

### Dominant Risk Modes

- smart contract risk,
- utilization collapse,
- stablecoin depeg,
- liquidity withdrawal stress,
- protocol insolvency.

### Fragility Channels

- recursive leverage unwinds,
- collateral market illiquidity,
- endogenous liquidation cascades.

### Regime Sensitivity

Performs best under:
- moderate volatility,
- stable liquidity conditions,
- sustained borrow demand.

---

## 2. Leveraged Carry

### Description

Strategies based on recursive borrowing and leverage amplification.

Examples:
- looping,
- leveraged LST carry,
- recursive stablecoin leverage.

### Yield Source

- spread amplification,
- leveraged carry extraction,
- staking yield enhancement.

### Dominant Risk Modes

- liquidation,
- funding spikes,
- collateral depeg,
- volatility expansion.

### Fragility Channels

- first-passage liquidation dynamics,
- leverage convexity,
- liquidity exhaustion.

### Regime Sensitivity

Performs best under:
- low volatility,
- stable funding conditions,
- persistent directional trends.

---

## 3. AMM Liquidity Provision

### Description

Capital is allocated to automated market maker pools to harvest trading fees.

Examples:
- Uniswap LP,
- concentrated liquidity,
- stablecoin pools.

### Yield Source

- trading fees,
- volatility harvesting,
- liquidity provision premium.

### Dominant Risk Modes

- impermanent loss,
- inventory drift,
- directional escape,
- jump volatility.

### Fragility Channels

- short convexity exposure,
- liquidity asymmetry,
- inventory concentration risk.

### Regime Sensitivity

Performs best under:
- range-bound markets,
- high volume with moderate volatility,
- stable liquidity depth.

---

## 4. Basis / Relative Value Strategies

### Description

Market-neutral or relative-value positioning across venues and instruments.

Examples:
- funding arbitrage,
- cash-and-carry,
- stablecoin spread trades,
- cross-exchange basis.

### Yield Source

- basis convergence,
- funding spreads,
- structural market inefficiencies.

### Dominant Risk Modes

- basis inversion,
- exchange fragmentation,
- liquidity dislocation,
- execution risk.

### Fragility Channels

- funding regime transitions,
- counterparty concentration,
- liquidity withdrawal events.

### Regime Sensitivity

Performs best under:
- stable basis structures,
- persistent directional positioning,
- moderate leverage environments.

---

## 5. Volatility Selling

### Description

Strategies that harvest volatility risk premia through implicit or explicit
short-convexity exposure.

Examples:
- concentrated LPs,
- options vaults,
- covered call systems.

### Yield Source

- variance risk premium,
- option decay,
- fee extraction.

### Dominant Risk Modes

- tail convexity,
- jump risk,
- volatility clustering,
- directional breakout.

### Fragility Channels

- nonlinear loss acceleration,
- gamma exposure,
- liquidity evaporation during stress.

### Regime Sensitivity

Performs best under:
- compressed volatility,
- mean-reverting markets,
- orderly liquidity conditions.

---

## 6. Reflexive Yield Systems

### Description

Strategies dependent on recursive collateral confidence and endogenous expansion dynamics.

Examples:
- restaking systems,
- recursive collateral protocols,
- synthetic leverage ecosystems.

### Yield Source

- reflexive collateral expansion,
- confidence-driven leverage,
- recursive yield stacking.

### Dominant Risk Modes

- confidence collapse,
- reflexive deleveraging,
- collateral instability,
- liquidity spirals.

### Fragility Channels

- endogenous feedback loops,
- recursive balance-sheet contraction,
- systemic liquidity compression.

### Regime Sensitivity

Performs best under:
- expansionary market phases,
- strong collateral confidence,
- abundant liquidity conditions.

---

# Strategy Abstraction

The framework treats each strategy as a probabilistic payoff engine rather than a deterministic yield source.

The relevant object is therefore not:

\[
\mathbb{E}[R_i]
\]

alone, but the full conditional distribution:

\[
R_i \mid X_t
\]

including:
- variance,
- skewness,
- kurtosis,
- drawdown geometry,
- liquidity sensitivity,
- and stress behavior.

This implies that two strategies with similar expected yields may exhibit radically different robustness properties under changing market regimes.

---

# Hidden Factor Exposures

Each strategy family can be interpreted as a bundle of implicit factor exposures.

| Strategy | Dominant Hidden Exposure |
|---|---|
| Passive Lending | Short liquidity stress |
| Leveraged Carry | Short volatility + leverage convexity |
| AMM LP | Short gamma / inventory drift |
| Basis Trades | Short basis instability |
| Volatility Selling | Short tail convexity |
| Reflexive Yield | Short confidence / reflexivity |

This factor decomposition becomes central for:
- regime-aware allocation,
- stress testing,
- and dynamic portfolio construction.

---

# Research Direction

The strategy universe serves as the foundational layer for:

1. Regime classification,
2. Strategy-regime mapping,
3. Monte Carlo allocation simulation,
4. Robust portfolio optimization,
5. Experimental live allocation design.

Future stages will extend this framework toward:
- conditional payoff estimation,
- dynamic allocation policies,
- fragility-adjusted efficiency frontiers,
- and stochastic portfolio control. 