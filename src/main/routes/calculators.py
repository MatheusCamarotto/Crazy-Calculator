#Rotas para as calculadoras

from flask import Blueprint, jsonify, request

calc_routes_bp = Blueprint("calc_routes", __name__) #isso nomeia as rotas das calculadoras e categoriza elas de fato como as rotas especificas da calculadora