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

        print(name)
        print(dataset.head())

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
    def fetchByMostTitles(dt_constructors, dt_standings):
        """
        Needs Testing
        """

        if dt_standings is None:
            raise Exception("Dataset cannot be None")

        if dt_constructors is None:
            raise Exception("Dataset cannot be None")

        most_winners = dt_standings[dt_standings["position"] == 1]
        most_winners = (
            most_winners.groupby(most_winners["constructorId"])
            .max()
            .reset_index()
            .head(10)
        )

        result = most_winners.to_dict("records")
        print(most_winners.head())

        return result
