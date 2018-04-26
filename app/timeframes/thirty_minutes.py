

from timeframe import Timeframe
from datetime import timedelta
import one_minute

class ThirtyMinutes(Timeframe):
	"""
	Timeframe class for thirty minutes.
	"""

	TIMEFRAME = "30m"
	MINUTES = 30
	BASE = one_minute.OneMinute

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length * 30)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
