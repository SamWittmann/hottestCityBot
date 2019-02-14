from requests import ConnectionError
from datetime import datetime
import logging

from Util import report_error
from TwitterClient import TwitterClient
from WeatherRequester import WeatherRequester


class Controller:
    def __init__(self):
        self.twitter_client = TwitterClient().get_client()
        self.weather_requester = WeatherRequester()
        self.logger = logging.getLogger('HottestCityBot')

    def get_hottest_city_and_tweet_result(self):
        try:
            location_temp_tup = self.weather_requester.find_hottest_city_and_temp()
            tweet = "Today, the hottest city in the U.S is %s with a temperature of %sF" % location_temp_tup
            self.twitter_client.post_text_tweet(tweet)
            self.logger.info("Succesfully posted tweet for " + str(datetime.today().date()))
        except ConnectionError:
            self.logger.exception("Run failed: could not establish a connection to an external API.")
            report_error()
            return -1

        return 0
