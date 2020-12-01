from flask import Flask
from pandas import pandas as pd
from routes import drivers, constructors, circuits
import data_provider

app = Flask(__name__)

data_provider.load_dataset()

app.register_blueprint(drivers.bp)
app.register_blueprint(constructors.bp)
app.register_blueprint(circuits.bp)


@app.route("/")
def home():
    return "<h1>Welcome to the F1 REST API</h1>"


@app.route("/races/<string:date>")
def raceDate(date):
    """
    GET
    Retorna informações sobre a corrida em uma determinada data.
    """


app.run(debug=True)