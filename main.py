# File: main.py

from data_collection.market_data_agent import fetch_data
from trade_signals.trade_signal_generator import generate_trade_signal
from risk_management.confidence_score_manager import calculate_confidence_score
from utils.logger_setup import setup_logger

# Set up logging for the entire bot
logger = setup_logger('profit_bot', 'profit_bot.log')

def main():
    try:
        logger.info("Starting the main script.")
        
        # Step 1: Fetch data
        logger.info("Fetching market data...")
        data = fetch_data()  # Default symbol is S&P 500; adjust as needed
        logger.info("Data fetched successfully.")

        # Step 2: Generate trade signals
        logger.info("Generating trade signals...")
        data_with_signals = generate_trade_signal(data)
        logger.info("Trade signals generated.")

        # Step 3: Calculate confidence scores
        logger.info("Calculating confidence scores...")
        data_with_confidence = calculate_confidence_score(data_with_signals)
        logger.info("Confidence scores calculated.")

        # Step 4: Log final output (limited rows for readability)
        logger.info("Final data with trade signals and confidence scores:")
        logger.info(data_with_confidence[['Close', 'SMA_short', 'SMA_long', 'Signal', 'Confidence']].head())

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
