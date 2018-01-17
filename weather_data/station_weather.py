import datetime
from urllib.request import urlretrieve, HTTPError
from dateutil import rrule
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

    def fetch_data_for_period(self, start_date, end_date):
        missing_periods = []
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
            first_day = dt.replace(day=1)
            month = datetime.datetime.strftime(first_day, "%m")
            year = datetime.datetime.strftime(first_day, "%Y")
            try:
                self.fetch_weather_conditions(int(year), int(month))
            except HTTPError:
                print("WARNING: Missing data for {} station in {}/{}".format(self.name, month, year))
                missing_periods.append("{}/{}".format(year, month))
        return "Missing periods for {} station: ".format(self.name) + ", ".join(missing_periods)

    def fetch_weather_conditions(self, year, month):
        """
        Download station's weather conditions from IMGW server for specific month and year.
        Save it to local directory 
        :param year: year to retrieve results for
        :type year: int
        :param month: month of provided year to retrieve results for
        :type month: int
        :param save_data: save the results in local directory?
        :type save_data: bool
        :return: relative path to local dir where the file has been saved to 
        :rtype  str
        """
        date = datetime.date(year, month, 1)
        year, month= str(date).split('-')[0:2]
        url_prefix = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/"
        sub_dir = "{}/{}/".format(year, month)
        filename = "dane_{}_{}_{}.csv.gz".format(year, month, self.id)
        local_dir = "./input_data/imgw/data/station_{}_{}/{}/".format(self.id, self.name, year)
        local_filename = "{}_{}_{}.csv.gz".format(self.id, year, month)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        url = url_prefix + sub_dir + filename
        urlretrieve(url, local_dir + local_filename)
        return local_dir + local_filename
