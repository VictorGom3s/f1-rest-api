from pandas import pandas as pd

dataset = {
    "drivers": None,
    "races": None,
    "circuits": None,
    "constructors": None,
}


def load_dataset():
    dataset["drivers"] = pd.read_csv("data/drivers.csv")
    dataset["races"] = pd.read_csv("data/races.csv")
    dataset["circuits"] = pd.read_csv("data/circuits.csv")
    dataset["constructors"] = pd.read_csv("data/constructors.csv")
