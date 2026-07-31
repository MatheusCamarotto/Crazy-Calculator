from src.drivers.numpy_handler import NumpyHandler
from pytest import raises
from .calculator_3 import Calculator3

class MockRquest:
    def __init__(self, body):
        self.json = body

def test_calculate():
    mock_request = MockRquest({"numbers": [1, 2, 3, 4, 5, 6]})
    calculator_3 = Calculator3(NumpyHandler())
    with raises(Exception) as excinfo:
        response = calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Falha processo: Variância menor que multiplicação'
    return response