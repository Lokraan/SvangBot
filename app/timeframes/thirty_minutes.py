

from timeframe import Timeframe
import timedelta

class ThirtyMinutes(Timeframe):
	"""
	Timeframe class for thirty minutes.
	"""

	TIMEFRAME = "5m"

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length * 30)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
