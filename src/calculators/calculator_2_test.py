from .calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body):
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [2.3, 5.33, 1.32]})

    calculator2 = Calculator2()
    calculator2.calculate(mock_request)
    formated_response = calculator2.calculate(mock_request)
    print()
    print(formated_response)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.07}}