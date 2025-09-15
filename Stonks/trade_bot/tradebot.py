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
"""

import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")

# Initialize the trading client
trading_client = TradingClient(
    API_KEY, API_SECRET, paper=True
)  # paper=True for paper trading

# Create a market order request
order_request = MarketOrderRequest(
    symbol="AAPL",  # Ticker symbol
    qty=1,  # Number of shares
    side=OrderSide.BUY,  # Buy or sell
    time_in_force=TimeInForce.DAY,  # Order duration
)

# Submit the order
order = trading_client.submit_order(order_request)
print(order)
