from flask import Blueprint

bp = Blueprint("constructors", __name__, url_prefix="/constructors")


@bp.route("/<string:nationality>")
def constructorsNationality(nationality):
    """
    GET
    Retorna todos os construtores(equipes) de uma determinada nacionalidade
    """


@bp.route("/<int:year>")
def constructorsYear(year):
    """
    GET
    Retorna todos os construtores(equipes) de um determinado ano/temporada
    """
