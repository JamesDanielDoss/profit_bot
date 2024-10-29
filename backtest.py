import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_collection.market_data_agent import fetch_data
from trade_signals.trade_signal_generator import generate_trade_signal
from risk_management.confidence_score_manager import calculate_confidence_score
from utils.logger_setup import setup_logger

# Set up logging for backtesting
logger = setup_logger('backtest_logger', 'backtest.log')

def calculate_returns(data):
    """Calculates daily returns and cumulative returns based on generated signals."""
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']
    data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod() - 1
    return data

def plot_performance(data):
    """Plots the cumulative strategy return, coloring green for positive and red for negative."""
    plt.figure(figsize=(10, 6))
    
    # Determine where the cumulative return is positive or negative
    positive_returns = data['Cumulative_Strategy_Return'] >= 0
    plt.plot(data.index, data['Cumulative_Strategy_Return'].where(positive_returns),
             label="Strategy Cumulative Return", color='green')
    plt.plot(data.index, data['Cumulative_Strategy_Return'].where(~positive_returns),
             label="Strategy Cumulative Return", color='red')

    plt.title("Cumulative Strategy Return Over Time")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid()
    plt.savefig("backtest_performance.png")
    logger.info("Performance chart saved as backtest_performance.png")

def main():
    try:
        # Step 1: Fetch historical data
        logger.info("Fetching historical market data for backtesting...")
        data = fetch_data()
        logger.info("Data fetched successfully.")

        # Step 2: Generate trade signals
        logger.info("Generating trade signals for backtesting...")
        data_with_signals = generate_trade_signal(data)
        logger.info("Trade signals generated.")

        # Step 3: Calculate confidence scores
        logger.info("Calculating confidence scores for backtesting...")
        data_with_confidence = calculate_confidence_score(data_with_signals)
        logger.info("Confidence scores calculated.")

        # Step 4: Calculate strategy returns
        logger.info("Calculating strategy returns...")
        data_with_returns = calculate_returns(data_with_confidence)

        # Step 5: Plot performance
        plot_performance(data_with_returns)

        # Log summary statistics
        final_cumulative_return = data_with_returns['Cumulative_Strategy_Return'].iloc[-1]
        avg_daily_return = data_with_returns['Strategy_Return'].mean()
        logger.info(f"Final Cumulative Return: {final_cumulative_return:.2%}")
        logger.info(f"Average Daily Return: {avg_daily_return:.4%}")

        logger.info("Backtesting completed.")

    except Exception as e:
        logger.error(f"An error occurred during backtesting: {e}")

if __name__ == "__main__":
    main()
