

from datetime import datetime, timedelta

import ccxt.async as ccxt
import tenacity


class Utils:
	"""
	Provides utils for methods used across a majority of classes in order to
	make coding easier and more understandable.
	"""
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
		"""
		Gets available free balance in BTC and returns it.
		"""
		bal = await self.client.fetch_balance()
		bal = bal["BTC"]["free"]

		self.logger.debug("Balance {0}".format(bal))

		return bal
		

	async def get_current_price(self, symbol: str) -> float:
		"""
		Gets the current price of *symbol* by fetching it's current ticker
		and returning the close price.
		"""
		ticker = await self._aretry.call(self.client.fetch_ticker, symbol)
		self.logger.debug(ticker)

		return ticker["close"]


	async def curr_timestamp(self, symbol: str):
		"""
		Gets the current timestamp that the exchange is operating on
		by fetching its most recent ticker and getting its timestamp.
		"""
		ticker = await self._aretry.call(self.client.fetch_ticker, symbol)

		return ticker["timestamp"]


	async def get_historical_data(self, symbol: str, length: int, timeframe):
		"""
		Gets historical data from exchange for *symbol* with *length* datapoints
		on the specified *timeframe*. 
		Returns historical data with the oldest at index 0, and the newest at
		the end.

		Supported timeframes = 1 minute, 5 minutes, 30 minutes, 1 hour, 4 hour, 1 day
		"""
		base = await self.curr_timestamp(symbol)
		base /= 1000
		
		since = datetime.fromtimestamp(base) - timeframe.get_timedelta(length)
		since = since.timestamp() * 1000

		# need to do ohlcv testing
		ohlcv = await self._aretry.call(self.client.fetch_ohlcv, 
			symbol, timeframe.BASE.TIMEFRAME, since=since, limit=length+1)

		ohlcv = timeframe.splice_data(ohlcv, timeframe.BASE, timeframe)

		close_prices = [p[4] for p in ohlcv]

		self._logger.debug(close_prices)

		return close_prices
