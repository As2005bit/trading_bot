# Trading Bot (Binance Futures Testnet)

## Setup
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Add your Binance Testnet API key and secret in client.py

## How to run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000

## Assumptions
- This project uses Binance Futures Testnet (not real money)
- Only MARKET and LIMIT orders are implemented
- User provides correct symbol and inputs
- Internet connection is required to place orders
