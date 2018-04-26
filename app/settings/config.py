

import ccxt.async as ccxt
import logging
import sys

from ichi_conf import IchiConfig
from ema_conf import EmaConfig
from rsi_conf import RsiConfig

import timeframes

import utils
import ichimoku
import rsi

class Config:
	def __init__(self, API_KEY=None, SECRET=None, TIMEFRAME=None):
		self.DEBUG = False
		self.TEST = False

		# Trading config
		self.MULTIPLIER = 1.25 # something to do with the buy function
		self.LEVERAGE = 25 # leverage to trade with
		self.INTERVAL = 60 # how often it connects to the exchange and calculates whatever

		self.TIMEFRAME = TIMEFRAME # timeframe to calculate indicators with
		self.SYMBOL = "BTC/USD"
		self.API_KEY = API_KEY
		self.SECRET = SECRET

		# if self.SECRET is None or self.KEY is None:
		# 	raise TypeError("Please specify a secret and key for bitmex api")

		self.CLIENT = None #ccxt.bitmex({
			# "apiKey": self.API_KEY,
			# "secret": self.SECRET
			# })

		## TRADING CONFIG
		self.EMA_CFG = EmaConfig
		self.ICHI_CFG = IchiConfig
		self.RSI_CFG = RsiConfig
		# Choosing Indicator
		self.INDICATOR = "RSI"

		## set up logging
		logger = logging.getLogger()

		level = logging.INFO

		f_handler = logging.FileHandler(filename="../../svangbot.log", encoding="utf-8", mode="w")
		cl_handler = logging.StreamHandler()

		dt_fmt = "%Y-%m-%d %H:%M:%S"
		fmt = logging.Formatter("[{asctime}] [{levelname:<6}] {name}: {message}", 
			dt_fmt, style="{")

		cl_handler.setFormatter(fmt)
		f_handler.setFormatter(fmt)

		logger.addHandler(cl_handler)
		logger.addHandler(f_handler)
		logger.setLevel(level)

		self.LOGGER = logger

		self.UTILS = utils.Utils(self.CLIENT, self.LOGGER)

		# Strategy config
		self.INDICATOR = rsi.RSI(self.UTILS, self.RSI_CFG, self.LOGGER, self.TIMEFRAME)
		self.TIMEFRAME = timeframes.timeframes[self.TIMEFRAME]


class DevConfig(Config):
	def __init__(self, API_KEY=None, SECRET=None, TIMEFRAME=None):
		Config.__init__(self, API_KEY=None, SECRET=None, TIMEFRAME=None)
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

		self.LOGGER.setLevel(logging.DEBUG)

cfg = Config()
