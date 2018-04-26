

from timeframe import Timeframe
from datetime import timedelta
import one_hour

class FourHours(Timeframe):
	"""
	Timeframe class for four hours.
	"""

	TIMEFRAME = "4h"
	MINUTES = 240
	BASE = one_hour.OneHour

	@staticmethod
	def get_timedelta(length):
		return timedelta(hours=length * 4)

	def __eq__(self, other):
		return other == TIMEFRAME

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__
