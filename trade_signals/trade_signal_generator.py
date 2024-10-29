import pandas as pd
import numpy as np

def generate_trade_signal(data, short_window=40, long_window=100):
    """
    Generates trade signals based on a simple moving average crossover strategy.
    Buy signal when short moving average crosses above long moving average,
    sell signal when short moving average crosses below long moving average.
    """
    # Calculate short and long moving averages
    data['SMA_short'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['SMA_long'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Generate signals using np.where for clear element-wise comparison
    data['Signal'] = np.where(data['SMA_short'] > data['SMA_long'], 1,
                              np.where(data['SMA_short'] < data['SMA_long'], -1, 0))

    return data
