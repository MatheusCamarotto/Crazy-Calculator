import numpy
from typing import List

"""
Classe que vai utilizar o numpy(lib externa), esse arquivo serve para padronização
do projeto. Quem quiser utilizar o desvio padrão vai consultar esse arquivo.
Funciona como uma Fachada, isso é um padrão de projeto estrutural que fornece uma
interface simplificada para uma biblioteca, um framework, ou quakquer conjunto 
complexo de classes.
https://refactoring.guru/design-patterns/facade
"""

class NumpyHandler:
    def __init__(self):
        self.__np = numpy
    #Desvio padrão(.std)
    def standart_derivation(self, numbers:List[float]) -> float:
        return self.__np.std(numbers)

    def standart_derivation_with_param(self, numbers:List[float]) -> float:
        return self.__np.std(numbers, axis=[])
    