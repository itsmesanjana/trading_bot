import argparse
from client import BinanceClient
from utils import validate_input

def main():
    parser = argparse.ArgumentParser(description="Mock Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol, side, order_type, quantity, price = validate_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n📌 Order Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}\n")

        client = BinanceClient()
        response = client.place_order(
            symbol, side, order_type, quantity, price
        )

        print("✅ Order Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print(f"❌ {str(e)}")

if __name__ == "__main__":
    main()