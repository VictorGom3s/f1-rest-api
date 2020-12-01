from pandas import pandas as pd


class Drivers:
    @staticmethod
    def getByYear(dataset, year):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        return [
            {"name": "Lewis Hamilton"},
            {"name": "Sebastian Vettel"},
            {"name": "Lando Norris"},
        ]

    @staticmethod
    def getByNationality(dataset, nationality):
        return "drivers by nationality"