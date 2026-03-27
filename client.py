from binance.client import Client

API_KEY = "your_api_key"
API_SECRET = "your_secret_key"

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
