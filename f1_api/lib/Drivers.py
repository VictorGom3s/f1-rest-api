from pandas import pandas as pd


class Drivers:
    @staticmethod
    def fetchByNationality(dataset, nationality):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[dataset["nationality"] == nationality]
        result = result.to_dict("records")

        return result

    @staticmethod
    def fetchByForenameAndSurname(dataset, forename, surname):
        if dataset is None:
            raise Exception("Dataset cannot be None")

        result = dataset[
            (dataset["forename"] == forename) & (dataset["surname"] == surname)
        ]
        result = result.to_dict("records")

        return result