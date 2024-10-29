import pandas as pd

def generate_trade_signal(data, short_window=3, long_window=5):
    """
    Generates trade signals based on a simple moving average crossover strategy.
    Buy signal when short moving average crosses above long moving average,
    sell signal when short moving average crosses below long moving average.
    """
    # Calculate short and long moving averages
    data['SMA_short'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['SMA_long'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Generate signals: Use `.loc` to avoid chained assignment issues
    data['Signal'] = 0
    data.loc[short_window:, 'Signal'] = [
        1 if data['SMA_short'].iloc[i] > data['SMA_long'].iloc[i] else -1
        for i in range(short_window, len(data))
    ]

    return data

if __name__ == "__main__":
    # Test with sample data (you could also fetch data using market_data_agent)
    test_data = pd.DataFrame({
        'Close': [3200, 3220, 3215, 3230, 3245, 3250, 3260, 3280, 3270, 3300]
    })

    # Generate trade signals
    data_with_signals = generate_trade_signal(test_data)
    print(data_with_signals[['Close', 'SMA_short', 'SMA_long', 'Signal']])
