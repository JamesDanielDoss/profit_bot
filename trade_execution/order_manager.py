# trade_execution/order_manager.py

import logging

# Initialize logger
logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self):
        self.orders = []

    def place_order(self, signal, price, volume):
        """
        Places a buy or sell order based on the signal.
        
        Parameters:
        - signal (str): The trade signal, either 'buy' or 'sell'.
        - price (float): The price at which to place the order.
        - volume (int): The number of units to trade.
        """
        if signal not in ['buy', 'sell']:
            logger.error("Invalid signal: Must be 'buy' or 'sell'")
            return

        order = {
            'signal': signal,
            'price': price,
            'volume': volume
        }
        self.orders.append(order)
        logger.info(f"Order placed: {order}")

    def get_orders(self):
        """Returns all orders placed."""
        return self.orders

# Test functionality if run as a standalone script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    manager = OrderManager()
    manager.place_order('buy', price=100.5, volume=10)
    manager.place_order('sell', price=102.3, volume=5)
    print(manager.get_orders())
