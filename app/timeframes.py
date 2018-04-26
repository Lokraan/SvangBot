
from datetime import timedelta


class Timeframe:
	""" 
	Abstract Timeframe class. 
	This class is used in order to make timeshift calculations easier because
	it has a get_timedelta method which automatically fills in the parameters
	eg. timedelta(minutes=), timedelta(days=), etc

	Makes coding more understandable as you're using classes instead of strings
	as well.
	"""

	ERR = "Please implement this method u.u"
	TIMEFRAME = "NONE"

	@staticmethod
	def get_timedelta(length: int):
		raise NotImplementedError(ERR)

	@staticmethod
	def splice_data(data: list, timeframe, desired):
		if timeframe.MINUTES > desire.MINUTES:
			raise TypeError("Cannot scale timeframes DOWN")
			
		elif timeframe.MINUTES == desired.TIMEFRAME:
			return data

		ratio = desired.MINUTES / timeframe.MINUTES
		return data[::ratio]


class OneMinute(Timeframe):
	"""
	Timeframe class for one minute.
	"""

	TIMEFRAME = "1m"
	MINUTES = 1
	BASE = OneMinute

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length)


class FiveMinutes(Timeframe):
	"""
	Timeframe class for five minutes.
	"""

	TIMEFRAME = "5m"
	MINUTES = 5
	BASE = OneMinute

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length * 5)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__


class ThirtyMinutes(Timeframe):
	"""
	Timeframe class for thirty minutes.
	"""

	TIMEFRAME = "30m"
	MINUTES = 30

	@staticmethod
	def get_timedelta(length):
		return timedelta(minutes=length * 30)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__


class OneHour(Timeframe):
	"""
	Timeframe class for one hour.
	"""

	TIMEFRAME = "1h"
	MINUTES = 60
	BASE = OneHour

	@staticmethod
	def get_timedelta(length):
		return timedelta(hours=length)

	def __eq__(self, other):
		return other == TIMEFRAME	

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__


class FourHours(Timeframe):
	"""
	Timeframe class for four hours.
	"""

	TIMEFRAME = "4h"
	MINUTES = 240
	BASE = OneHour

	@staticmethod
	def get_timedelta(length):
		return timedelta(hours=length * 4)

	def __eq__(self, other):
		return other == TIMEFRAME

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__


class OneDay(Timeframe):
	"""
	Timeframe class for four hours.
	"""

	TIMEFRAME = "1d"
	MINUTES = 1440
	BASE = OneDay

	@staticmethod
	def get_timedelta(length):
		return timedelta(days=length)

	def __eq__(self, other):
		return other == TIMEFRAME

	def __str__(self):
		return TIMEFRAME

	__repr__ = __str__


timeframes = {
	ThirtyMinutes.TIMEFRAME: ThirtyMinutes,
	FiveMinutes.TIMEFRAME: FiveMinutes,
	OneMinute.TIMEFRAME: OneMinute,
	FourHours.TIMEFRAME: FourHours,
	OneHour.TIMEFRAME: OneHour,
	OneDay.TIMEFRAME: OneDay	
}


if __name__ == '__main__':
	t = Timeframe
	print(str(t))
	t = OneMinute
	print(str(t))