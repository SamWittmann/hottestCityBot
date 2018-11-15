from weather import Weather, Unit


class WeatherRequester:
    def __init__(self):
        self.weather = Weather(unit=Unit.FAHRENHEIT)

    def _query_temperature(self, city_name, state_name):
        try:
            location = self.weather.lookup_by_location(city_name + ', ' + state_name)
            condition = location.condition
            return condition.temp
        except KeyError:
            return 0
        except AttributeError:
            return 0

    def find_hottest_city_and_temp(self):
        hottest = ('', 0)
        with open('resources/top1000cities.txt') as f:
            for line in f:
                split_line = line.split(',')
                city = split_line[1]
                state = split_line[2]

                if "'" in city:
                    city = city.replace("\'", "\\\'")
                temperature = self._query_temperature(city, state)

                if hottest[1] < temperature:
                    hottest = (city + ', ' + state, temperature)

        return hottest
