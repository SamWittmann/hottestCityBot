import schedule
from Controller import Controller
import time
import logging

# Setup logging
logger = logging.getLogger('HottestCityBot')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('HottestCityBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("Bot started running")
controller = Controller()
schedule.every().day.at("20:00").do(lambda: controller.get_hottest_city_and_tweet_result())

while 1:
    schedule.run_pending()
    time.sleep(1)

