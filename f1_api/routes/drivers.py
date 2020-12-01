from flask import Blueprint, abort
from lib.Drivers import Drivers
from data_provider import dataset as data


bp = Blueprint("drivers", __name__, url_prefix="/drivers")


@bp.route("/<int:year>")
def driversYear(year):
    """
    GET
    Retorna todos os pilotos de um determinado ano/temporada
    """
    try:
        result = Drivers.getByYear(data["drivers"], year)
        return {"result": result}
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/<string:nationality>")
def driversNationality(nationality):
    """
    GET
    Retorna todos os pilotos de uma determinada nacionalidade
    """