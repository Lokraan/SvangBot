

from indicator import Indicator
import states


class Ichimoku(Indicator):
	def __init__(self, utils, config, logger, timeframe):
		Indicator.__init__(self, utils, config, logger, timeframe)

		self.senkou_span_b_period = self.cfg.SENKOU_SPAN_B_PERIOD
		self.displacement_period = self.cfg.DISPLACEMENT_PERIOD
		self.tenkan_sen_period = self.cfg.TENKAN_SAN_PERIOD
		self.kijun_sen_period = self.cfg.KIJUN_SEN_PERIOD


	def calc_ichi(prices: list) -> list:
		## TODO, MAKE SURE PRICES ARE BEING PASSED IN CORRECTLY

		#Calculate Tenkan Sen
		tenkan_sen = (
			max(prices[:self.tenkan_sen_period]) + 
			min(prices[:self.tenkan_sen_period])) / 2

		#Calculate Kijun Sen
		kijun_sen = (
			max(prices[:self.kijun_sen_period]) + 
			min(prices[:self.kijun_sen_period])) / 2

		#Calculate Current Senkou Span A
		old_tenkan_sen = (
			max(
				prices[
					self.displacement_period : 
					self.displacement_period + self.tenkan_sen_period
				]
			) + 
			min(
				prices[
					self.displacement_period:
					self.displacement_period + self.tenkan_sen_period
				]
			)) / 2
		
		old_kijun_sen = (
			max(
				prices[
					self.displacement_period :
					self.displacement_period + self.tenkan_sen_period
				]
			) + 
			min(
				prices[
					self.displacement_period :
					self.displacement_period + self.tenkan_sen_period
				]
			)) / 2

		current_senkou_span_a = (old_tenkan_sen + old_kijun_sen) / 2

		#Calculate Current Senkou Span B
		current_senkou_span_b = (
			max(
				prices[
					self.displacement_period :
					self.displacement_period + self.senkou_span_b_period
				]
			) + 
			min(
				prices[
					self.displacement_period :
					self.displacement_period + self.senkou_span_b_period
					]
			)) / 2

		#Calculate Future Senkou Span A
		future_senkou_span_a = (tenkan_sen + kijun_sen) / 2

		#Calculate Future Senkou Span B
		future_senkou_span_b = (
			max(prices[:self.senkou_span_b_period]) + 
			min(prices[:self.senkou_span_b_period])) / 2

		#Get Chikou Span == Current Closing Price
		chikou_span_and_current_closing_price = prices[0]

		#return previous_prices[0]
		return [tenkan_sen, kijun_sen, current_senkou_span_a, current_senkou_span_b, future_senkou_span_a, future_senkou_span_b, chikou_span_and_current_closing_price]


	def signal(previous_ichimokus: list):
		data = previous_ichimokus
		current_close_index = len(data) - 1
		previous_close_index = len(data) - 2

		signals = []

		#Tenkan Sen / Kijun Sen Cross
		if data[previous_close_index][1] < data[previous_close_index][2] and data[current_close_index][1] > data[current_close_index][2]:
			current_signal = []
			current_signal.append("Tenkan Sen / Kijun Sen Cross")
			current_signal.append("Bullish")
			signals.append(current_signal)
		elif data[previous_close_index][1] > data[previous_close_index][2] and data[current_close_index][1] < data[current_close_index][2]:
			current_signal = []
			current_signal.append("Tenkan Sen / Kijun Sen Cross")
			current_signal.append("Bearish")
			signals.append(current_signal)

		#Kijun Sen Cross
		if data[previous_close_index][7] < data[previous_close_index][2] and data[current_close_index][7] > data[current_close_index][2]:
			current_signal = []
			current_signal.append("Kijun Sen Cross")
			current_signal.append("Bullish")
			signals.append(current_signal)
		elif data[previous_close_index][7] > data[previous_close_index][2] and data[current_close_index][7] < data[current_close_index][2]:
			current_signal = []
			current_signal.append("Kijun Sen Cross")
			current_signal.append("Bearish")
			signals.append(current_signal)

		#Kumo Breakout
		if data[previous_close_index][7] < max(data[previous_close_index][-6:-3]) and  data[previous_close_index][7] > max(data[previous_close_index][-6:-3]):
			current_signal = []
			current_signal.append("Kumo Breakout")
			current_signal.append("Bullish")
			signals.append(current_signal)
		elif data[previous_close_index][7] > max(data[previous_close_index][-6:-3]) and  data[previous_close_index][7] > min(data[previous_close_index][-6:-3]):
			current_signal = []
			current_signal.append("Kumo Breakout")
			current_signal.append("Bearish")
			signals.append(current_signal)

		'''
		#Tenkan Sen / Kijun Sen Cross
		if (data[len(data) - 1][0] > data[len(data) - 1][1] and data[len(data) -2][0] < data[len(data) - 2][1]):
			current_signal = []
			current_signal.append("Tenkan Sen / Kijun Sen Cross")
			current_signal.append("bullish")
			signals.append(current_signal)
		elif (data[len(data) - 1][0] < data[len(data) - 1][1] and data[len(data) -2][0] > data[len(data) - 2][1]):
			current_signal = []
			current_signal.append("Tenkan Sen / Kijun Sen Cross")
			current_signal.append("bearish")
			signals.append(current_signal)

		#Kijun Sen Cross
		if (data[len(data) - 1][6] > data[len(data) - 1][1] and data[len(data) -2][5] < data[len(data) - 2][1]):
			current_signal = []
			current_signal.append("Kijun Sen Cross")
			current_signal.append("bullish")
			signals.append(current_signal)
		elif (data[len(data) - 1][6] < data[len(data) - 1][1] and data[len(data) -2][5] > data[len(data) - 2][1]):
			current_signal = []
			current_signal.append("Kijun Sen Cross")
			current_signal.append("bearish")
			signals.append(current_signal)

		#Kumo Breakout
		if data[len(data) - 1][6] > max(data[len(data) - 2][2], data[len(data) - 2][3]) and min(data[len(data) - 2][2], data[len(data) - 2][3]) < data[len(data) - 2][5] < max(data[len(data) - 2][2], data[len(data) - 2][3]):
			current_signal = []
			current_signal.append("Kumo Breakout")
			current_signal.append("bullish")
			signals.append(current_signal)
		elif data[len(data) - 1][6] < min(data[len(data) - 2][2], data[len(data) - 2][3]) and min(data[len(data) - 2][2], data[len(data) - 2][3]) < data[len(data) - 2][5] < max(data[len(data) - 2][2], data[len(data) - 2][3]):
			current_signal = []
			current_signal.append("Kumo Breakout")
			current_signal.append("bearish")
			signals.append(current_signal)

		#Senkou Span Cross
		if data[len(data) - 1][2] > data[len(data) - 1][3] and data[len(data) - 2][2] < data[len(data) - 1][3]:
			current_signal = []
			current_signal.append("Senkou Span Cross")
			current_signal.append("bullish")
			signals.append(current_signal)
		elif data[len(data) - 1][2] < data[len(data) - 1][3] and data[len(data) - 2][2] > data[len(data) - 1][3]:
			current_signal = []
			current_signal.append("Senkou Span Cross")
			current_signal.append("bearish")
			signals.append(current_signal)

		#Chikou Span Cross
		if data[len(data) - 1][4] > data[len(data) - 1][5] and data[len(data) - 1][4] < data[len(data) - 1][5]:
			current_signal = []
			current_signal.append("Chikou Span Cross")
			current_signal.append("bullish")
			signals.append(current_signal)
		elif data[len(data) - 1][4] > data[len(data) - 1][5] and data[len(data) - 1][4] < data[len(data) - 1][5]:
			current_signal = []
			current_signal.append("Chikou Span Cross")
			current_signal.append("bearish")
			signals.append(current_signal)
		'''

		#Bull or Bear Kumo Cloud
		if data[current_close_index][5] > data[current_close_index][6]:
			current_signal = []
			current_signal.append("Kumo Cloud")
			current_signal.append("Bullish")
			signals.append(current_signal)
		elif data[current_close_index][5] < data[current_close_index][6]:
			current_signal = []
			current_signal.append("Kumo Cloud")
			current_signal.append("Bearish")
			signals.append(current_signal)

		return signals


	async def acalc_ichi(symbol: str):
		
		length = self.displacement_period + max(self.tenkan_sen_period, 
			self.kijun_sen_period, self.senkou_span_b_period)

		prices = await self.utils.get_historical_data(symbol, length, self.timeframe)

		return self.calc_ichi(prices)