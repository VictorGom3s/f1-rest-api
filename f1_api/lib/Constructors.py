from pandas import pandas as pd


class Constructors:
    @staticmethod
    def fetchById(dataset, constructorId):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["constructorId"] == constructorId]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByNationality(dataset, nationality):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["nationality"] == nationality]
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
    def fetchByRefName(dataset, constructorRef):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["constructorRef"] == constructorRef]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchAllUniqueConstructors(dataset):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset.groupby(dataset["name"]).max().reset_index()
        result = result.to_dict("records")

        return result
