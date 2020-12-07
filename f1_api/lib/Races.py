from pandas import pandas as pd


class Races:
    @staticmethod
    def fetchById(dataset, raceId):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["raceId"] == raceId]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByYear(dataset, year):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["year"] == year]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByName(dataset, name):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["name"] == name]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByDate(dataset, date):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["date"] == date]
        result = result.to_dict("records")

        return result
