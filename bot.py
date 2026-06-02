from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging

print("Bot started")
API_KEY = ""
API_SECRET = ""

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

client = Client(API_KEY, API_SECRET, testnet=True)

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Order Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

        else:
            print("Invalid order type")
            return

        logging.info(f"Order Response: {order}")

        print("Order placed successfully")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))

    except BinanceAPIException as e:
        logging.error(f"Binance API Error: {e}")
        print("Binance API Error:", e)

    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error:", e)


# Test market order
place_order(
    symbol="BTCUSDT",
    side="BUY",
    order_type="LIMIT",
    quantity=0.001,
    price=50000
)
