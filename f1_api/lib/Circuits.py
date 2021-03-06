from pandas import pandas as pd


class Circuits:
    @staticmethod
    def fetchByLocation(dataset, location):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["location"] == location]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByRefName(dataset, refName):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["circuitRef"] == refName]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByCountry(dataset, country):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["country"] == country]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchById(dataset, circuitId):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["circuitId"] == circuitId]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchAllUniqueCircuits(dataset):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset.groupby(dataset["name"]).max().reset_index()
        result = result.to_dict("records")

        return result