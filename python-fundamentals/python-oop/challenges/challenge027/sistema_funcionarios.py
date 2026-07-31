from abc import ABC, abstractmethod
from hashlib import sha256

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float, senha:str):
        self.nome = nome
        self.salario = salario
        self.__senha = None

        self.__senha = senha

        @property
        def senha(self):
            return self.__senha

        @senha.setter
        def senha(self, novasenha):
            self.__senha = sha256(novasenha.encode()).hexdigest()
            return self.__senha

        def autenticar_senha(self, testesenha):
            if self.__senha == sha256(testesenha.encode()).hexdigest():
                print("Senha confere!")
            else: 
                print("Senha não confere")

        @abstractmethod
        def calcular_bonus():
            pass


class Gerente(Funcionario):
    def __init__(self, nome:str, salario:float, senha:str):
        super().__init__(self, nome, salario)
        self.nome = nome
        self.salario = salario

        def calcular_bonus():
            pass


class Desenvolvedor(Funcionario): 
    def __init__(self, nome:str, salario:float, senha:str):
        super().__init__(self, nome, salario)
        self.nome = nome
        self.salario = salario

        def calcular_bonus():
            pass