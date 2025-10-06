"""
This contains the logic for future implementation of a trading bot.
We should also add a smart way to log its activity. Measure its performance.

I/O functions
Buy, Sell, Hold, Buy amount, Sell amount, Stop loss, Take profit

Libraries to consider:
-Alpaca
-yfinance
-PyTorch
-NumPy
-Backtrader

Lets start implementing a mean reversion strategy as our first strategy.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


# Load environment variables from .env file
PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")

if not API_KEY or not API_SECRET:
    raise RuntimeError(
        "Missing Alpaca credentials. Set ALPACA_API_KEY and ALPACA_API_SECRET in the OS "
        "environment or create Stonks/trade_bot/.env with those keys."
    )

print("API_KEY:", API_KEY)
print("API_SECRET:", API_SECRET)

# The trading client is how we can interact with the API and submit orders
# Initialize the trading client
trading_client = TradingClient(
    API_KEY, API_SECRET, paper=True
)  # paper=True for paper trading


