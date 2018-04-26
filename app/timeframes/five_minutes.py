

from timeframe import Timeframe
from datetime import timedelta
import one_minute

class FiveMinutes(Timeframe):
	"""
	Timeframe class for five minutes.
	"""

	TIMEFRAME = "5m"
	MINUTES = 5
	BASE = one_minute.OneMinute

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length * 5)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
