from flask import Blueprint, abort, jsonify
from lib.Races import Races
from data_provider import dataset as data


bp = Blueprint("races", __name__, url_prefix="/races")


@bp.route("/<int:id>")
def racesId(id):
    """
    GET
    Retorna a corrida por id
    """
    try:
        result = Races.fetchById(data["races"], id)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/year/<int:year>")
def racesYear(year):
    """
    GET
    Retorna todas as corridas de um determinado ano
    """
    try:
        result = Races.fetchByYear(data["races"], year)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/name/<string:name>")
def raceName(name):
    """
    GET
    Retorna as corridas por nome
    """
    try:
        result = Races.fetchByName(data["races"], name)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/date/<string:date>")
def raceDate(date):
    """
    GET
    Retorna as corridas por data
    """
    try:
        result = Races.fetchByDate(data["races"], date)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)
