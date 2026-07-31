#Rotas para as calculadoras

from flask import Blueprint, jsonify, request
from src.main.factories.calculator3_factory import calculator3_factory 
from src.main.factories.calculator2_factory import calculator2_factory 
from src.main.factories.calculator1_factory import calculator1_factory

calc_routes_bp = Blueprint("calc_routes", __name__) #isso nomeia as rotas das calculadoras e categoriza elas de fato como as rotas especificas da calculadora

@calc_routes_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calc = calculator1_factory()
    response = calc.calculate(request=request)

    return jsonify(response), 200

@calc_routes_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    calc = calculator2_factory()
    response = calc.calculate(request=request)

    return jsonify(response), 200

@calc_routes_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    calc = calculator3_factory()
    response = calc.calculate(request=request)

    return jsonify(response), 200