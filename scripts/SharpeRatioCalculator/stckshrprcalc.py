import pandas as pd
import numpy as np
import yfinance as yf


def get_returns(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)
    returns = stock['Adj Close'].pct_change()
    returns = returns.dropna()
    return returns


def sharpe_ratio(returns, risk_free_rate):
    excess_returns = returns - risk_free_rate
    print('return data:' excess_returns)
    return excess_returns.mean() / excess_returns.std()


ticker = 'AAPL'
start_date = '2019-01-01'
end_date = '2022-03-10'
# Daily risk-free rate (e.g., 10-year Treasury rate / 252 trading days)
risk_free_rate = 0.02 / 252

daily_returns = get_returns(ticker, start_date, end_date)
# print(daily_returns)

sharpe = sharpe_ratio(daily_returns, risk_free_rate)
print(f'Sharpe Ratio of {ticker}: {sharpe:.2f}')

# Sharpe Ratio of AAPL: 0.78
