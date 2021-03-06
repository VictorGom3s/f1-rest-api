from pandas import pandas as pd

dataset = {
    "drivers": None,
    "races": None,
    "circuits": None,
    "constructors": None,
    "constructor_standings": None,
}


def load_dataset():
    try:
        dataset["drivers"] = pd.read_csv("data/drivers.csv")
        dataset["races"] = pd.read_csv("data/races.csv", parse_dates=["date"])
        dataset["circuits"] = pd.read_csv("data/circuits.csv")
        dataset["constructors"] = pd.read_csv("data/constructors.csv")
    except:
        raise Exception("Could not load data")
