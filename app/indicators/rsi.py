

from indicator import Indicator
import states

class RSI(Indicator):
	def __init__(self, utils, config, logger, timeframe):
		Indicator.__init__(self, utils, config, logger)

		self.timeframe = timeframe
		self.distance = self.cfg.DATA_POINTS
		self.period = self.cfg.PERIOD
		self.sell = self.cfg.SELL
		self.buy = self.cfg.BUY


	def calc_rsi(self, prices: list) -> float:
		period = self.period
		max_len = period if period < len(prices) else len(prices)

		losses = gains = 0
		for i in range(1, max_len):
			try:
				change = prices[i] - prices[i-1]
				if change < 0:
					losses += abs(change)
				elif change > 0:
					gains += abs(gains)

			except TypeError as e:
				print(e, prices)

		avg_loss = losses / period
		avg_gain = gains / period

		for i in range(period, len(prices)):
			change = prices[i] - prices[i - 1]

			loss = gain = 0
			if change < 0: 
				loss = abs(change)
			else:
				gain = change

			avg_gain = (avg_gain * (period - 1) + gain) / period
			avg_loss = (avg_loss * (period - 1) + loss) / period

		if avg_loss == 0:
			return 100

		elif avg_gain == 0:
			return 0

		rsi = 100
		rs = avg_gain / avg_loss
		rsi -= 100 / (1+ rs)

		return round(rsi, 2)


	async def acalc_rsi(self, symbol: str):
		data = await self.utils.get_historical_data(symbol, 
			length=self.distance * self.timeframe)

		rsi = self.calc_rsi(data)
		self.logger.debug(rsi)

		return rsi


	async def analyze(self, symbol: str) -> str:
		rsi = await self.acalc_rsi(symbol)

		if rsi >= self.sell:
			return symbol, rsi, states.SELL
		elif rsi <= self.buy:
			return symbol, rsi, states.BUY

		return symbol, rsi, states.HOLD


	def __str__(self):
		return "RSI"

	__repr__ = __str__
