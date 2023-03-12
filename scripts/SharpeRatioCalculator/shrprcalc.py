import numpy as np


def sharpe_ratio(returns, risk_free_rate):
    """
    Calculate the Sharpe Ratio for a given set of returns and risk-free rate.
    """
    # for row in returnsdata():
    excess_returns = returns - risk_free_rate
    print(excess_returns)
    mean_excess_returns = np.mean(excess_returns)
    print(mean_excess_returns)
    std_excess_returns = np.std(excess_returns)
    print(std_excess_returns)
    sharpe_ratio = mean_excess_returns / std_excess_returns
    return sharpe_ratio


returns = np.array([0.01, 0.02, -0.01, 0.05, -0.03])
risk_free_rate = 0.005

sr = sharpe_ratio(returns, risk_free_rate)

print("Sharpe Ratio:", sr)
