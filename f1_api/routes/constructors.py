from flask import Blueprint, abort, jsonify
from lib.Constructors import Constructors
from data_provider import dataset as data


bp = Blueprint("constructors", __name__, url_prefix="/constructors")


@bp.route("/<int:id>")
def constructorsId(id):
    """
    GET
    Retorna construtores por id
    """
    try:
        result = Constructors.fetchById(data["constructors"], id)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/nationality/<string:nationality>")
def constructorsNationality(nationality):
    """
    GET
    Retorna todos os construtores(equipes) de uma determinada nacionalidade
    """
    try:
        nationality = nationality.capitalize()

        result = Constructors.fetchByNationality(data["constructors"], nationality)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/name/<string:name>")
def constructorsName(name):
    """
    GET
    Retorna os construtores por nome
    """
    try:
        result = Constructors.fetchByName(data["constructors"], name)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/ref/<string:ref>")
def constructorsRefName(ref):
    """
    GET
    Retorna construtores por reference name
    """
    try:
        result = Constructors.fetchByRefName(data["constructors"], ref)
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)


@bp.route("/unique")
def constructorsUnique():
    """
    GET
    Retorna todos os construtores da história da F1
    """
    try:
        result = Constructors.fetchAllUniqueConstructors(data["constructors"])
        return jsonify(result)
    except Exception as e:
        return "<h1>404 - Nothing Found </h1>: <br> {}".format(e)
