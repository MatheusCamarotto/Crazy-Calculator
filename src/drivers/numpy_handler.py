import numpy as np
from .interfaces.driver_handler_interface import DriverHandlerInterface
# from Typing import List -> não é mais necessario por conta da versão do python
"""
Classe que vai utilizar o numpy(lib externa), esse arquivo serve para padronização
do projeto. Quem quiser utilizar o desvio padrão vai consultar esse arquivo.
Funciona como uma Fachada, isso é um padrão de projeto estrutural que fornece uma
interface simplificada para uma biblioteca, um framework, ou quakquer conjunto 
complexo de classes.
https://refactoring.guru/design-patterns/facade
"""

class NumpyHandler(DriverHandlerInterface):
    def __init__(self):
        self.__np = np

    # Desvio padrão(.std())
    def standart_derivation(self, numbers:list[float]) -> float:
        return self.__np.std(numbers)

    def standart_derivation_with_param(self, numbers:list[float]) -> float:
        return self.__np.std(numbers, axis=[])

    def variance(self, numbers:list[float]) -> float:
        return self.__np.var(numbers)
    