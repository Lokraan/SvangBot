

from timeframe import Timeframe
from datetime import timedelta

class OneHour(Timeframe):
	"""
	Timeframe class for one hour.
	"""

	TIMEFRAME = "1h"
	MINUTES = 60

	@staticmethod
	def get_timedelta(length):
		return timedelta(hours=length)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__