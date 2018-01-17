import pandas as pd

STATIONS_FILE = "input_data/imgw/wykaz_stacji.csv"


def get_stations():
    stations = pd.read_csv(STATIONS_FILE,
                           encoding='iso8859_2',
                           names=['station_id', 'station_name', 'no_idea'],
                           )
    stations.station_id = stations.station_id.fillna(0).astype(int)
    return stations


def get_city_stations(city):
    stations = get_stations()
    return stations[stations.station_name.str.startswith(city.upper())]


def get_station(station_name):
    stations = get_stations()
    return stations[stations.station_name == (station_name.upper())]
