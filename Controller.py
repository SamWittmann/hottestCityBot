from Util import report_error
from TwitterClient import TwitterClient
from WeatherRequester import WeatherRequester
from datetime import datetime


class Controller:
    def __init__(self):
        self.twitter_client = TwitterClient().get_client()
        self.weather_requester = WeatherRequester()

    def get_hottest_city_and_tweet_result(self):
        try:
            location_temp_tup = self.weather_requester.find_hottest_city_and_temp()
        except RuntimeError as e:
            report_error(e.message)
            print "Sent error info to hottestcitytwitter@gmail.com"
            return -1

        tweet = "Today, the hottest city in the U.S is %s with a temperature of %sF" % location_temp_tup
        self.twitter_client.post_text_tweet(tweet)
        print "Succesfully posted tweet for " + str(datetime.today().date())

        return 0
