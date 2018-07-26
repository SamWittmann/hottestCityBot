from weather import Weather, Unit
import datetime


class WeatherRequester:
    def __init__(self):
        self.weather = Weather(unit=Unit.FAHRENHEIT)

    def query_temperature(self, city_name, state_name):
        try:
            location = self.weather.lookup_by_location(city_name + ', ' + state_name)
            condition = location.condition
            return condition.temp
        except KeyError as e:
            return 0
        except AttributeError as e:
            return 0

    def find_hottest_city(self):
        hottest = (0, '')
        with open('top1000cities.txt') as f:
            for line in f:
                split_line = line.split(',')
                city = split_line[1]
                state = split_line[2]

                if "'" in city:
                    city = city.replace("\'", "\\\'")
                temperature = self.query_temperature(city, state)

                if hottest[0] < temperature:
                    hottest = (temperature, city + ', ' + state)

        return hottest


test = WeatherRequester()
b4 = datetime.datetime.now()
print test.find_hottest_city()
print datetime.datetime.now() - b4