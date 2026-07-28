from .calculator_1 import Calculator1
from typing import Dict
"""pytest
É necessário ter o "test" no começo ou final dos arquivos, funções, métodos, tudo relacionado ao pytest
precisar ter "test" para poder ser reconhecido pela lib.

para poder ver os retornos de maneira mais detalhada
pytest -s -v
-v: verbose
"""

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={
        "number": 1
    })
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    print(response)

    #Em teste unitarios se deve testar o FORMATO DA RESPOSTA
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    #Assertividade da resposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1