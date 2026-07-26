from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print("--- Iniciando o preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida pronta ---")

    def ferver_agua(self): 
        print("1. Fervendo água a 100°C") 

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass 


class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando água quente pelo pó de café")
    
    def servir(self):
        print("3. Servindo em xícara pequena")


class Cha(BebidaQuente):
    def misturar(self):
        print("2. Passando água quente pela erva seca")

    def servir(self):
        print("3. Servindo em caneca de porcelana")


class Leite(BebidaQuente):
    def misturar(self):
        print("2. Aquecendo o leite")


    def servir(self):
        print("3. Servindo em copo de vidro")