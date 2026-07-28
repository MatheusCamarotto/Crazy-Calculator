#Calculadora 1
from flask import request as FlaskRequest
from typing import Dict

class Calculator1:
    """Função da calculadora 1
    1. Um número é divido em 3 partes iguais.
    2.1. A primeira parte é dividida por 4 e seu resultado somado a 7.
    2.2. Após isso, o resultado é elevado ao quadrado e multiplicado
    por um valor de 0.257.
    3.1. A segunda parte é elevada a potência de 2.121, dividida 
    por 5 e somado a 1.
    3.2. A terceira parte se mantem no mesmo valor.
    """

    def calculate(self, request:FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body mal formatado!")

        input_data = body["number"]
        return input_data

    def __first_process(self, first_number: float) -> float:
        first_part = (first_number/4) + 7
        second_part = (first_part**2) * 0.257
        return second_part