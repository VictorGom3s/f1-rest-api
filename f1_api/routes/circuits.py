from flask import Blueprint, abort, jsonify
from lib.Circuits import Circuits
from data_provider import dataset as data

bp = Blueprint("circuits", __name__, url_prefix="/circuits")


@bp.route("/location/<string:location>")
def circuitsLocation(location):
    """
    GET
    Retorna todos os circuitos por ano localização
    """
    try:
        location = location.capitalize()

        result = Circuits.fetchByLocation(data["circuits"], location)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/name/<string:name>")
def circuitsRefName(name):
    """
    GET
    Retorna todos os circuitos por reference name
    """
    try:
        name = name.lower()

        result = Circuits.fetchByRefName(data["circuits"], name)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/country/<string:country>")
def circuitsCountry(country):
    """
    GET
    Retorna todos os circuitos do pais escolhido
    """
    try:
        country = country.capitalize()

        result = Circuits.fetchByCountry(data["circuits"], country)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found: </h1> <br> {}".format(e)
