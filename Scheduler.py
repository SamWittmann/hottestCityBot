import schedule
from Controller import Controller
import time

controller = Controller()
schedule.every().day.at("14:00").do(lambda: controller.get_hottest_city_and_tweet_result())

while 1:
    schedule.run_pending()
    time.sleep(1)

