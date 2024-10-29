# File: utils/logger_setup.py

import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Set up a logger for a specific module."""
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    # Create logger with the given name and level
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Add the handler only if it's not already added
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

if __name__ == "__main__":
    # Test the logger
    test_logger = setup_logger('test_logger', 'test.log')
    test_logger.info("This is an informational message.")
    test_logger.error("This is an error message.")
