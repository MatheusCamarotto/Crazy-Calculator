from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body):
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standart_derivation(self, numbers: list[float]) -> float:
        return 3

#Integração entre NumpyHandler e  Calculator2
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.3, 5.33, 1.32]})

    driver = NumpyHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)
  
    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.07}}

#isolando teste
def test_calculate():
    mock_request = MockRequest({"numbers": [2.3, 5.33, 1.32]})

    driver = MockDriverHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock_request)
  
    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.33}}