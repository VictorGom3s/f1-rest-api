from flask import Blueprint, abort, jsonify
from lib.Drivers import Drivers
from data_provider import dataset as data


bp = Blueprint("drivers", __name__, url_prefix="/drivers")


@bp.route("/<string:nationality>")
def driversNationality(nationality):
    """
    GET
    Retorna todos os pilotos de uma determinada nacionalidade
    """
    try:
        nationality = nationality.capitalize()

        result = Drivers.fetchByNationality(data["drivers"], nationality)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/name/<string:forename>/<string:surname>")
def driversByName(forename, surname):
    """
    GET
    Retorna piloto por nome e sobrenome
    """
    try:
        forename = forename.capitalize()
        surname = surname.capitalize()

        result = Drivers.fetchByForenameAndSurname(data["drivers"], forename, surname)

        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)
