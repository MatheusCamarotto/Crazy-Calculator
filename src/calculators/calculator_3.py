from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator3:
    def __init__(self, driver_handle: DriverHandlerInterface):
        self.__driver_handler = driver_handle

    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        pass