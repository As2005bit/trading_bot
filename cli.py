import argparse
from orders import place_order
from validators import validate_side, validate_order_type, validate_quantity

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "LIMIT" and not args.price:
        raise ValueError("Price required for LIMIT order")

    place_order(args.symbol, args.side, args.type, args.quantity, args.price)

except Exception as e:
    print("Validation Error:", str(e))
