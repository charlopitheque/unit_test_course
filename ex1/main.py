from functools import reduce


class Exercice1:
    def __init__(self):
        pass

    def join_string_list(self, list, delimitor):
        return delimitor.join(list)

    def calc_moy_list(self, list):
        return (reduce((lambda x, y: x + y), list)) / len(list)
