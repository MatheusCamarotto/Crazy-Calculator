from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator4:
    def __init__(self, driver_handle: DriverHandlerInterface):
        self.__driver_handler = driver_handle

    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body=body)

        average = self.__calculate_average(numbers=input_data)
        formated_response = self.__format_response(average=average)
        return formated_response

    def __validate_body(self, body: dict) -> list[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError("body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __calculate_average(self, numbers: list[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average

    def __format_response(self, average: float) -> dict:
        return {
            "data": {                
                "Calculator": 4,
                "value": average,
                "Success": True
                }
            }