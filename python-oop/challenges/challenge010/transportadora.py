from abc import ABC, abstractmethod

class Transporte(ABC):

    #atributos
    def __init__(self, distancia, frete = 0):
        self.distancia = distancia
        self.frete = 0 

    @abstractmethod
    def calcular_frete(self):
        pass


class Caminhao(Transporte):
    #atributo de classe
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return("Distância mínima para caminhão é de 50km")
        else: 
            self.frete = self.distancia * Caminhao.fator
            return (f"Valor do frete é de R${self.frete:.2f}")


class Drone(Transporte):
    fator = 9.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            return("Distância máxima para drone é de 10km")
        else: 
            self.frete = self.distancia * Drone.fator
            return (f"Valor do frete é de R${self.frete:.2f}")


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return (f"Valor do frete é de R${self.frete:.2f}")