

from timeframe import Timeframe
import timedelta

class OneHour(Timeframe):
	"""
	Timeframe class for four hours.
	"""

	TIMEFRAME = "5m"

	@staticmethod
	def get_timedelta(length):
		return timedelta(hours=length * 4)

	def __eq__(self, other):
		return other == TIMEFRAME

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
