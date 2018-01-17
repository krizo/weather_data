import pandas as pd


class Measurements:
    """
    Supported weather conditions measurements.
    This class defines what kind of measurements will be extracted for the analysis.
    """
    MAIN_MEASURES = {
        "Ciśnienie atmosferyczne obserwowane-synop": "Air Pressure",
        "Temperatura powietrza chwilowa-synop": "Temperature",
        "Wilgotność względna chwilowa-synop": "Humidity",
        "Kierunek wiatru średni za ostatnie 10 min.-synop": "Wind direction avg",
        "Prędkość wiatru średnia za ostatnie 10 min.-synop": "Wind speed avg",
        "Suma opadu za ostatnią godzinę-synop": "Rainfall 1h",
        "Czas trwania usłonecznienia za ostatnią godzinę-synop": "Sunshine 1h",
        'Suma opadu śniegu za ostatnią godzinę-synop': "Snowfall",
        "Widzialność pozioma-synop": "Visibility"
    }
    MEASURES_CSV = "input_data/imgw/listaDanychSystem.csv"
    measures_definitions = pd.read_csv(MEASURES_CSV, delimiter=';')

    @classmethod
    def build_main_measurements(cls):
        """
        Define main weather conditions measurements 
        :return: measurements with defined: name (Polish and English), code and unit 
        :rtype dict
        """
        measurements = []
        for measurement_pl, measurement_eng in cls.MAIN_MEASURES.items():
            measurement = Measurement(name=measurement_pl)
            measurement_def = {
                "measurement_pl": measurement.name,
                "measurement_en": measurement_eng,
                "measurement_code": measurement.code,
                "measurement_unit": measurement.unit
            }
            measurements.append(measurement_def)
        return measurements


class Measurement:
    def __init__(self, code=None, name=None):
        self._code = code
        self._name = name
        self._unit = None
        self.name_en = None

    @property
    def code(self):
        if self._code is None:
            return Measurements.measures_definitions.set_index("Opis pola").loc[self._name, 'Symbol']
        else:
            return self._code

    @property
    def name(self):
        if self._name is None:
            Measurements.measures_definitions.set_index("Symbol").loc[self._code, 'Opis pola']
        else:
            return self._name

    @property
    def unit(self):
        if self._unit is None:
            if self.code is not None:
                return Measurements.measures_definitions.set_index("Symbol").loc[self.code, 'Jednostka']
            else:
                return Measurements.measures_definitions.set_index("Opis pola").loc[self.name, 'Jednostka']
        else:
            return self._unit

