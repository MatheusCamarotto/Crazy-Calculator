#Rotas para as calculadoras

from flask import Blueprint, jsonify, request

calc_routes_bp = Blueprint("calc_routes", __name__) #isso nomeia as rotas das calculadoras e categoriza elas de fato como as rotas especificas da calculadora

@calc_routes_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    print(request)
    print(request.json)# pega o boddy da requisição
    return jsonify({"Sucess": True}), 200