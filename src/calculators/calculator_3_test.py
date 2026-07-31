from src.drivers.numpy_handler import NumpyHandler
from pytest import raises
from .calculator_3 import Calculator3

class MockRquest:
    def __init__(self, body):
        self.json = body

class MockDriverHandlerError: #aqui não utilizo o DriverHandlerInterface pois não necessito de outros metódos além da variancia
    def variance(self, numbers: list[float]) -> float:
        return 3

class MockDriverHandler: #aqui não utilizo o DriverHandlerInterface pois não necessito de outros metódos além da variancia
    def variance(self, numbers: list[float]) -> float:
        return 1000000


#e aqui ela vai dar variancia menor do que a multplicação dos valores gerando erro
def test_calculate_with_variance_error():
    mock_request = MockRquest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Falha no processo: Variância menor que multiplicação'

#variancia vai dar muito maior do que a multiplicação dos valores
def test_calculate():
    mock_request = MockRquest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)

    assert response == {
            "data": {                
                "Calculator": 3,
                "value": 1000000,
                "Success": True
                }
            }