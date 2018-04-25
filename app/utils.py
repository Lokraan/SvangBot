
from datetime import datetime, timedelta

import ccxt.async as ccxt
import tenacity


class Utils:
	def __init__(self, client, logger): 
		self.client = client
		self.logger = logger

		self._aretry = tenacity.AsyncRetrying(
			wait=tenacity.wait_random(0, 2),
			retry=(
				tenacity.retry_if_exception(ccxt.DDoSProtection) | 
				tenacity.retry_if_exception(ccxt.RequestTimeout)
				)
			)	


	async def get_available_balance(self):
		bal = await self.client.fetch_balance()
		bal = bal["BTC"]["free"]

		self.logger.debug("Balance {0}".format(bal))

		return bal
		

	async def get_current_price(self, symbol: str) -> float:
		ticker = await self._aretry.call(self.client.fetch_ticker, symbol)
		self.logger.debug(ticker)

		return ticker["close"]


	async def curr_timestamp(self, symbol: str):
		ticker = await self._aretry.call(self.client.fetch_ticker, symbol)

		return ticker["timestamp"]


	async def get_historical_data(self, symbol: str, length: int, timeframe: str):
		base = await self.curr_timestamp(symbol)
		base /= 1000
		
		since = datetime.fromtimestamp(base) - timedelta(minutes=length)
		since = since.timestamp() * 1000

		ohlcv = await self._aretry.call(self.client.fetch_ohlcv, 
			symbol, "1m", since=since, limit=length+1)

		close_prices = [p[4] for p in ohlcv]

		self._logger.debug(close_prices)

		return close_prices

