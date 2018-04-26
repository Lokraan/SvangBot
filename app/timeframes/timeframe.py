

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

	def __eq__(self, other):
		raise NotImplementedError(ERR)

	def __str__(self, other):
		raise NotImplementedError(ERR)

	__repr__ = __str__
	