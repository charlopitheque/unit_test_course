from functions import Functions
from functools import reduce


class Exercice4:
    heater_state_str = 'Heater stopped'

    def __init__(self, functions: Functions):
        super().__init__()
        self.functions = functions

    def start_heater(self):
        moy_last_temps = self.calc_moy_list(self.functions.get_last_days_temps())
        actual_temp = self.functions.get_actual_temp()
        if moy_last_temps > 20 and actual_temp > 25:
            self.functions.set_heater(True)
            self.heater_state_str = 'Heater started'
        else:
            self.functions.set_heater(False)
            self.heater_state_str = 'Heater stopped'

    # je me permet de ne pas la retest vu que je l'ai fait dans l'ex1, juste j'arrivais pas à importer la fct
    def calc_moy_list(self, list):
        return (reduce((lambda x, y: x + y), list)) / len(list)
