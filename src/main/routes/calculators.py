#Rotas para as calculadoras

from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_routes_bp = Blueprint("calc_routes", __name__) #isso nomeia as rotas das calculadoras e categoriza elas de fato como as rotas especificas da calculadora

@calc_routes_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calc = Calculator1()
    response = calc.calculate(request=request)

        
    # print(request)
    # print(request.json)# pega o boddy da requisição
    return jsonify(response), 200