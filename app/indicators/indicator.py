

class Indicator:
	def __init__(self, utils, config, logger):
		self.logger = logger
		self.utils = utils
		self.cfg = config

	async def analyze(self):
		raise NotImplementedError("Please implement this method u.u")
