

import ccxt.async as ccxt

class Config:
	def __init__(self, API_KEY=None, SECRET=None):
		self.DEBUG = False
		self.TEST = False

		self.SYMBOL = "BTC/USD"
		self.API_KEY = API_KEY
		self.SECRET = SECRET

		if self.SECRET is None or self.KEY is None:
			raise TypeError("Please specify a secret and key for bitmex api")

		self.CLIENT = ccxt.bitmex({
			"apiKey": self.API_KEY,
			"secret": self.SECRET
			})

		## TRADING CONFIG
		self.EMAS = [13, 21, 34]
		self.EMA1 = self.EMAS[0]
		self.EMA2 = self.EMAS[1]
		self.EMA3 = self.EMAS[2]
		
		self.MULTIPLIER = 1.25
		self.LEVERAGE = 25
		self.INTERVAL = 60


class DevConfig(Config):
	def __init__(self):
		Config.__init__(self, API_KEY=None, SECRET=None)
		self.DEBUG = True
		self.TEST = True

		self.CLIENT = ccxt.bitmex({
			"urls": {
				"api": "https://testnet.bitmex.com",
				"test": "https://www.bitmex.com"
			},
			"apiKey": self.API_KEY,
			"secret": self.SECRET
			})
