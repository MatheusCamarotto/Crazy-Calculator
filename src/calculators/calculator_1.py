#Calculadora 1
from flask import request as FlaskRequest
from typing import Dict

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

    def calculate(self, request:FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(first_number=splited_number)

        second_process_result = self.__second_process(second_number=splited_number)

        third_process_result = self.__third_process(third_number=splited_number)

        final_process_result = self.__final_process(firts_result=first_process_result, second_result=second_process_result, third_result=third_process_result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body mal formatado!")

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

    def __third_process(self, third_number: float) -> float:
        return third_number

    def __final_process(self, first_result: float, second_result: float, third_result: float) -> float:
        first_part = first_result + second_result + third_result
        return first_part