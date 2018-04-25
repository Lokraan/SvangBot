

import asyncio
import sys

sys.path.append("app/indicators")
sys.path.append("app/settings")
sys.path.append("app")

from app.settings import *
from app.settings import config
from app import bot


def main():
	
	if len(sys.argv) == 1 or sys.argv[1] == "main" :
		cfg = config.Config(API_KEY=None, SECRET=None)

	elif sys.argv[1] == "dev":
		cfg = config.DevConfig(API_KEY=None, SECRET=None)


	# logger = config.LOGGER
	# logger.info("Starting System...")

	# bot = trading_bot.Bot(config)

	# loop = asyncio.get_event_loop()
	# loop.run_until_complete(bot.start())
	# loop.close()


if __name__ == "__main__":
	main()
	