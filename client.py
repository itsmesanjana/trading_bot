import random
from logger import setup_logger

logger = setup_logger()

class BinanceClient:
    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Mock Request: {symbol} {side} {order_type} {quantity} {price}")

            # Simulated response
            response = {
                "orderId": random.randint(100000, 999999),
                "status": "FILLED" if order_type == "MARKET" else "NEW",
                "executedQty": quantity if order_type == "MARKET" else 0,
                "avgPrice": price if price else "market_price"
            }

            logger.info(f"Mock Response: {response}")
            return response

        except Exception as e:
            logger.error(f"Error: {str(e)}")
            raise Exception(f"Mock API Error: {str(e)}")
        
        

# NOTE:
# This is a mock implementation due to Binance Testnet access limitations.
# Replace this with real Binance API call using python-binance or requests.