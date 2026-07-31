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
    def set_senha(self, senha):
        self.__senha = sha256(senha.encode()).hexdigest()
        return self.__senha

    def verificar_senha(self, senha):
        if self.__senha == sha256(senha.encode()).hexdigest():
            print("Senha confere!")
        else:
            print("Senha não confere")

    @abstractmethod
    def mostrar_dados(self):
        pass


class Admin(Usuario):
    def __init__(self, nome:str, email:str, senha:str):
        super().__init__(self, nome, email, senha)
        self.nome = nome
        self.email = email
        self.__senha = senha

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nPermissão: Acesso total ao sistema")


class Cliente(Usuario):
    def __init__(self, nome:str, email:str, senha:str):
        super().__init__(self, nome, email, senha)
        self.nome = nome
        self.email = email  
        self.__senha = senha

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nPermissão: Acesso limitado ao sistema")