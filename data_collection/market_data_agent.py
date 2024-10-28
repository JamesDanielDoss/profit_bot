import yfinance as yf
import pandas as pd

def fetch_data(symbol='^GSPC', start_date='2020-01-01', end_date='2023-01-01'):
    """Fetches historical data for the specified symbol."""
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    # Test fetching data
    data = fetch_data()
    print(data.head())
