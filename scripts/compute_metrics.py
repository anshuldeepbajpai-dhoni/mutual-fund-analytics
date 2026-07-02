import numpy as np
import pandas as pd


TRADING_DAYS = 252


def calculate_cagr(nav_series):
    years = len(nav_series) / TRADING_DAYS

    if years <= 0:
        return np.nan

    return ((nav_series.iloc[-1] / nav_series.iloc[0]) ** (1 / years) - 1) * 100


def calculate_sharpe_ratio(returns, risk_free_rate=0.06):
    excess_returns = returns - (risk_free_rate / TRADING_DAYS)

    return (
        excess_returns.mean()
        / excess_returns.std()
    ) * np.sqrt(TRADING_DAYS)


def calculate_sortino_ratio(returns, risk_free_rate=0.06):
    excess_returns = returns - (risk_free_rate / TRADING_DAYS)

    downside_returns = excess_returns[excess_returns < 0]

    downside_std = downside_returns.std()

    return (
        excess_returns.mean()
        / downside_std
    ) * np.sqrt(TRADING_DAYS)


def calculate_beta(fund_returns, benchmark_returns):
    covariance = np.cov(
        fund_returns,
        benchmark_returns
    )[0, 1]

    variance = np.var(benchmark_returns)

    return covariance / variance


def calculate_alpha(
    fund_return,
    benchmark_return,
    beta,
    risk_free_rate=0.06
):
    return (
        fund_return
        - (
            risk_free_rate
            + beta * (benchmark_return - risk_free_rate)
        )
    )


def calculate_max_drawdown(nav_series):
    rolling_max = nav_series.cummax()

    drawdown = (
        nav_series - rolling_max
    ) / rolling_max

    return drawdown.min() * 100


def calculate_var(returns, confidence=0.95):
    percentile = (1 - confidence) * 100

    return np.percentile(returns, percentile) * 100


def calculate_cvar(returns, confidence=0.95):
    var = np.percentile(
        returns,
        (1 - confidence) * 100
    )

    return returns[returns <= var].mean() * 100


if __name__ == "__main__":
    print("Performance metrics module loaded successfully.")