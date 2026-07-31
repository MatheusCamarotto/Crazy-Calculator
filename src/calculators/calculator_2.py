from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

#from typing import Dict, List -> não é mais necessario por conta da versão do python
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

"""Tipagem driver_handler: DriverHandlerInterface
A classe DriverHandlerInterface como tipagem da var 'driver_handler', 
ajuda na procura dos metodos da classe, na qual ajudamos o VScode a 
compreender isso e sugerir mais facilmente.
"""
class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest): # type: ignore
        body = request.json
        input_data = self.__validate_body(body=body)
        calculated_number = self.__process_data(input_data=input_data)
        formated_response = self.__format_response(calculate_number=calculated_number)
        return formated_response

    def __validate_body(self, body: dict) -> list[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError("body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: list[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        print(first_process_result)
        result = self.__driver_handler.standart_derivation(first_process_result)
        print(result)
        return 1/result

    def __format_response(self, calculate_number: float) -> dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculate_number, 2)
            }
        }