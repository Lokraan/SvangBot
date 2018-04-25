

from enum import Enum

class RsiConfig(Enum):
	TIMEFRAME = "1m"
	DATA_POINTS = 14
	PERIOD = 14
	SELL = 70
	BUY = 30 
