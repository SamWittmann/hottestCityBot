from weather import Weather, Unit


class WeatherRequester:
    def __init__(self):
        self.weather = Weather(unit=Unit.FAHRENHEIT)

    def _query_temperature(self, city_and_state):
        try:
            location = self.weather.lookup_by_location(city_and_state)
            condition = location.condition
            return condition.temp
        except KeyError:
            return 0
        except AttributeError:
            return 0

    def find_hottest_city_and_temp(self):
        hottest = ('', 0)
        with open('resources/top1000cities.txt') as f:
            for city_and_state in f:
                temperature = self._query_temperature(city_and_state)

                if hottest[1] < temperature:
                    hottest = (city_and_state, temperature)

        return hottest
