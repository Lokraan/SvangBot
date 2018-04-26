

class Indicator:
	def __init__(self, utils, config, logger, timeframe):
		self.logger = logger
		self.utils = utils
		self.cfg = config
		self.timeframe = timeframe

	async def analyze(self):
		raise NotImplementedError("Please implement this method u.u")
