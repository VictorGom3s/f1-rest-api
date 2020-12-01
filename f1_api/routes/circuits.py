from flask import Blueprint

bp = Blueprint("circuits", __name__, url_prefix="/circuits")


@bp.route("/<int:year>")
def circuitsYear(year):
    """
    GET
    Retorna todos os circuitos por ano escolhido
    """


@bp.route("/<string:country>")
def circuitsCountry(country):
    """
    GET
    Retorna todos os circuitos do pais escolhido
    """


@bp.route("/<int:year>/<string:country>")
def circuitsYearCountry(year, country):
    """
    GET
    Retorna todos os circuitos do pais escolhido
    """