

from timeframe import Timeframe
import timedelta

class OneMinute(Timeframe):
	"""
	Timeframe class for one minute.
	"""

	TIMEFRAME = "1m"

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
