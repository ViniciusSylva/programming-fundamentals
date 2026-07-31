from abc import ABC, abstractmethod
from hashlib import sha256

class Usuario(ABC):
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email= email
        self.__senha = None

        self.__senha = senha

        @property
        def senha(self):
            return self.__senha 

        @senha.setter
        def senha(self, novasenha):
            self.__senha = sha256(novasenha.encode()).hexdigest
            return self.__senha

    def verificar_senha(self):
        pass

    @abstractmethod
    def mostrar_dados(self):
        pass


class Admin(Usuario):
    pass


class Cliente(Usuario):
    pass