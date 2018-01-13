import pandas as pd


class Measures:
    """
    Supported weather conditions measurements with their English equivalents
    """
    MAIN_MEASURES = {
        "Ciśnienie atmosferyczne obserwowane-synop": "Air Pressure",
        "Temperatura powietrza chwilowa-synop": "Temperature",
        "Temperatura gruntu chwilowa-synop": "Ground Temperature",
        "Wilgotność względna chwilowa-synop": "Humidity",
        "Kierunek wiatru średni za ostatnie 10 min.-synop": "Wind direction avg",
        "Prędkość wiatru średnia za ostatnie 10 min.-synop": "Wind speed avg",
        "Suma opadu za ostatnią godzinę-synop": "Rainfall 1h",
        "Czas trwania usłonecznienia za ostatnią godzinę-synop": "Sunshine 1h",
        "Ciśnienie atmosferyczne na poziomie stacji-synop-obserwator": "Air pressure 2",
        "Temperatura powietrza-synop": "Temperature 2",
        'Średnia temperatura powietrza-dekada-synop': "Temperature avg",
        'Prędkość wiatru-synop-obserwator': "Wind speed 2",
        'Suma opadu śniegu za ostatnią godzinę-synop': "Snowfall"
    }
    MEASURES_CSV = "input_data/imgw/listaDanychSystem.csv"
    measures_definitions = pd.read_csv(MEASURES_CSV, delimiter=';').set_index('Symbol')

    @classmethod
    def get_measure_symbol(cls, measure):
        """
        Get the symbol of measure given in Polish. 
        For instance, given "Temperatura powietrza chwilowa-synop" will return B100E00200"
        :param measure: weather conditions measurement (in Polish)
        :return: weather conditions measurement symbol
        :rtype: str
        """
        measure = cls.measures_definitions[cls.measures_definitions['Opis pola'] == measure].index
        return measure[0] if len(measure) > 0 else None

    @classmethod
    def get_measure(cls, measure):
        """
        Get the measure's symbol given in English.
        For instance, given "Temperature avg" will return ('B100B016CK', 'Temperature avg')"
        :param measure: weather conditions measurement (in English)
        :return: symbol and measurement name 
        :rtype: tuple
        """
        res = [(symbol, name) for symbol, name in cls.build_main_measures().items() if name == measure or symbol == measure]
        return None if not res else res[0]

    @classmethod
    def build_main_measures(cls):
        return {
            cls.get_measure_symbol(measure_pl): measure_eng for measure_pl, measure_eng in cls.MAIN_MEASURES.items()
        }

#
# class Measure:
#     def __init__(self, symbol=None, name=None):
#         self._symbol = symbol
#         self._name = name
#
#     @property
#     def symbol(self):
#         if self._symbol is None:
#             symbol_found = [symbol for symbol, name in Measures.build_main_measures().items() if name == self._name]
#             return symbol_found[0] if symbol_found else None
#         else:
#             return self._symbol
#
#     @property
#     def name(self):
#         if self._name is None:
#             name_found = [name for symbol, name in Measures.build_main_measures().items() if symbol == self._symbol]
#             return name_found[0] if name_found else None
#         else:
#             return self._name
#
