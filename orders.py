from client import client
import logging

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        summary = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price
        }

        print("\nOrder Summary:", summary)
        print("Order Response:", {
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty")
        })

        logging.info(f"REQUEST: {summary}")
        logging.info(f"RESPONSE: {order}")

    except Exception as e:
        print("Error:", str(e))
        logging.error(str(e))
