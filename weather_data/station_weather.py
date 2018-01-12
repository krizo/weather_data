import datetime
from urllib.request import urlretrieve
from weather_data.stations import get_station
import os


class Station:
    def __init__(self, station_name):
        self.name = station_name

    @property
    def id(self):
        return list(get_station(self.name)['station_id'])[0]

    def fetch_weather_conditions(self, year, month):
        date = datetime.date(year, month, 1)
        year, month= str(date).split('-')[0:2]
        url_prefix = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/"
        sub_dir = "{}/{}/".format(year, month)
        filename = "dane_{}_{}_{}.csv.gz".format(year, month, self.id)
        local_dir = "./input_data/imgw/data/{}/".format(year)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        url = url_prefix + sub_dir + filename
        urlretrieve(url, local_dir + filename)

