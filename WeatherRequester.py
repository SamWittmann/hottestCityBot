from weather import Weather, Unit
import logging


class WeatherRequester:
    def __init__(self):
        self.weather = Weather(unit=Unit.FAHRENHEIT)
        self.logger = logging.getLogger('HottestCityBot')

    def _query_temperature(self, city_and_state):
        try:
            location = self.weather.lookup_by_location(city_and_state)
            condition = location.condition
            return int(condition.temp)
        except KeyError:
            return 0
        except AttributeError:
            return 0

    def find_hottest_city_and_temp(self):
        hottest = ('', 0)
        self.logger.info("Finding today's hottest city")
        with open('resources/top1000cities.txt') as f:
            for line in f:
                city_and_state = line[:-1] if line[-1] == '\n' else line
                temperature = self._query_temperature(city_and_state)

                if hottest[1] < temperature:
                    hottest = (city_and_state, temperature)
        self.logger.info("Result of query is: " + hottest)
        return hottest
