

from timeframe import Timeframe
from datetime import timedelta
import one_hour

class OneDay(Timeframe):
	"""
	Timeframe class for four hours.
	"""

	TIMEFRAME = "1d"
	MINUTES = 1440
	BASE = one_hour.OneHour

	@staticmethod
	def get_timedelta(length):
		return timedelta(days=length)

	def __eq__(self, other):
		return other == TIMEFRAME

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
