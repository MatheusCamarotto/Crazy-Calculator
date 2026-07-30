from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler
#from typing import Dict, List -> não é mais necessario por conta da versão do python

class Calculator2:
    def calculate(self, request: FlaskRequest): # type: ignore
        body = request.json
        input_data = self.__validate_body(body=body)
        calculated_number = self.__process_data(input_data=input_data)
        formated_response = self.__format_response(calculate_number=calculated_number)
        return formated_response

    def __validate_body(self, body: dict) -> list[float]:
        if 'numbers' not in body:
            raise Exception("Body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: list[float]) -> float:
        numpy_handler = NumpyHandler()
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        print(first_process_result)
        result = numpy_handler.standart_derivation(first_process_result)
        print(result)
        return 1/result

    def __format_response(self, calculate_number: float) -> dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculate_number, 2)
            }
        }