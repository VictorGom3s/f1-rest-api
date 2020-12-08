from flask import Flask
from pandas import pandas as pd
from routes import drivers, constructors, circuits, races
import data_provider

app = Flask(__name__)

data_provider.load_dataset()

app.register_blueprint(drivers.bp)
app.register_blueprint(constructors.bp)
app.register_blueprint(circuits.bp)
app.register_blueprint(races.bp)


@app.route("/")
def home():
    return "<h1>Welcome to the F1 REST API</h1>"


app.run(debug=True)