

class Timeframe:
	""" 
	Abstract Timeframe class. 
	This class is used in order to make timeshift calculations easier because
	it has a get_timedelta method which automatically fills in the parameters
	eg. timedelta(minutes=), timedelta(days=), etc

	Makes coding more understandable as you're using classes instead of strings
	as well.
	"""

	@staticmethod
	def get_timedelta(length: int):
		raise NotImplementedError("Please implement this method u.u")

	def __eq__(self, other):
		raise NotImplementedError("Please implement this method u.u")

	def __str__(self, other):
		raise NotImplementedError("Please implement this method u.u")

	__repr__ = __str__
	