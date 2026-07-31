from src.drivers.numpy_handler import NumpyHandler
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body):
        self.json = body

class MockDriverHandlerError: #aqui não utilizo o DriverHandlerInterface pois não necessito de outros metódos além da variancia
    def average(self, numbers: list[float]) -> float:
        return 3

class MockDriverHandler:
    def average(self, numbers: list[float]) -> float:
        return 5

def test_calculate():
    mock_request = MockRequest({"numbers": [5, 5, 5, 5, 5]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {
            "data": {                
                "Calculator": 4,
                "value": 5,
                "Success": True
                }
            }