from abc import ABC, abstractmethod
from hashlib import sha256

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float, senha:str = None):
        self.nome = nome
        self.salario = salario
        if senha is None:
            senha = self.pede_senha()
        self.senha = senha
        

    def __str__(self):
        return f"Nome: {self.nome}, salario: {self.salario}, senha: {self.senha}"

    def pede_senha(self):
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break

        return senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, novasenha):
        self.__senha = sha256(novasenha.encode()).hexdigest()
        return self.__senha

    def autenticar(self, senha):
        if self.__senha == sha256(senha.encode()).hexdigest():
            print ("Senha confere!")
        else: 
            print ("Senha não confere")

    @abstractmethod
    def calcular_bonus():
        pass


class Gerente(Funcionario):
    def __init__(self, nome:str, salario:float, senha:str = None):
        super().__init__(nome, salario, senha)

    def __str__(self):
        return f"Nome: {self.nome}, salario: {self.salario}, senha: {self.senha}"

    def calcular_bonus(self):
        self.salario = self.salario * 1.2
        print(f"Salario de Gerente com bonus de cargo de 20%: {self.salario:.2f}")
        return self.salario
        


class Desenvolvedor(Funcionario): 
    def __init__(self, nome:str, salario:float, senha:str = None):
        super().__init__(nome, salario, senha)

    def __str__(self):
        return f"Nome: {self.nome}, salario: {self.salario}, senha: {self.senha}"

    def calcular_bonus(self):
        self.salario = self.salario * 1.4
        print(f"Salario de Desenvolvedor com bonus de cargo de 40%: {self.salario:.2f}")
        return self.salario