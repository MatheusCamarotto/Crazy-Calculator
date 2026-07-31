#Calculadora 1
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

# from typing import Dict -> não é mais necessario por conta da versão do python

class Calculator1:
    """Função da calculadora 1
    1. Um número é divido em 3 partes iguais.
    __first_process()
    2.1. A primeira parte é dividida por 4 e seu resultado somado a 7.
    2.2. Após isso, o resultado é elevado ao quadrado e multiplicado
    por um valor de 0.257.
    __second_process()
    3.1. A segunda parte é elevada a potência de 2.121, dividida 
    por 5 e somado a 1.
    3.2. A terceira parte se mantem no mesmo valor.

    4. Por fim é somado os 3 valores e entregue o resultado.
    """

    def calculate(self, request: FlaskRequest) -> dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(first_number=splited_number)

        second_process_result = self.__second_process(second_number=splited_number)

        final_calc_result = first_process_result + second_process_result + splited_number

        response = self.__format_response(calc_result=final_calc_result)

        return response

    def __validate_body(self, body: dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["number"]
        return input_data

    def __first_process(self, first_number: float) -> float:
        first_part = (first_number/4) + 7
        second_part = (first_part**2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        first_part = (second_number**2.121) 
        second_part = (first_part / 5) + 1
        return second_part

    def __format_response(self, calc_result: float) -> dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2) #deixa com duas casas decimais
            }
        }