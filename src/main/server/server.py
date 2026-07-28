#Definições básicas para o servidor
from flask import Flask
from src.main.routes.calculators import calc_routes_bp

app = Flask(__name__)

#cadastrando a blueprint no app
app.register_blueprint(calc_routes_bp)