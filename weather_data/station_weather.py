import datetime
from urllib.request import urlretrieve
from weather_data.stations import get_station
import os


class Station:
    """
    Meteo station to get the weather conditions results for   
    
    """
    def __init__(self, station_name):
        """
        :param station_name: name of the station. Example: "Kraków-Balice"
        :type station_name: str
        """
        self.name = station_name

    @property
    def id(self):
        """
        id of the meteo station  
        :return: 
        """
        return list(get_station(self.name)['station_id'])[0]

    def fetch_weather_conditions(self, year, month, save_data=True):
        """
        Download station's weather conditions from imgw server for specific month and year.
        Save it to local directory 
        :param year: year to retrieve results for
        :type year: int
        :param month: month of provided year to retrieve results for
        :type month: int
        :param save_data: save the results in local directory?
        :type save_data: bool
        :return: url of retrieved data
        :rtype  str
        """
        date = datetime.date(year, month, 1)
        year, month= str(date).split('-')[0:2]
        url_prefix = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/"
        sub_dir = "{}/{}/".format(year, month)
        filename = "dane_{}_{}_{}.csv.gz".format(year, month, self.id)
        local_dir = "./input_data/imgw/data/{}/".format(year)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        url = url_prefix + sub_dir + filename
        if save_data:
            urlretrieve(url, local_dir + filename)
        return url
