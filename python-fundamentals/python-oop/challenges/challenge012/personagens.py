from abc import ABC, abstractmethod
import random

class Personagens(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        print(f"{self.nome}({self.vida}) ataca {alvo.nome}({alvo.vida}) com um {self.golpes[random.randint(0, len(self.golpes) - 1)]} de força {forca}!")
        forca = random.randint(0, forca)
        print(f"{alvo.nome} recebeu {forca} de dano!")
        alvo.vida -= forca
        print(f"{alvo.nome} agora tem {alvo.vida} de vida!")

    @abstractmethod
    def curar(self, curar):
        pass


class Guerreiro(Personagens):
    def __init__(self, nome, vida):
        super().__init__(nome, vida, ["Dark punch", "Corte embuido em trevas"])

    def curar(self, curar):
        curar = random.randint(0, curar)
        self.vida += curar
        print(f"{self.nome} usou ataduras e recuperou {curar} de vida!")
        print(f"{self.nome} agora tem {self.vida} de vida!")


class Mago(Personagens):
    def __init__(self, nome, vida):
        super().__init__(nome, vida, ["Golpe de Fogo", "Kyokusen"])

    def curar(self, curar):
        curar = random.randint(0, curar)
        self.vida += curar
        print(f"{self.nome} usou uma magia de cura e recuperou {curar} de vida!")
        print(f"{self.nome} agora tem {self.vida} de vida!")