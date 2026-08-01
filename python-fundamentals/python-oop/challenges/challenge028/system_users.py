from abc import ABC, abstractmethod
from hashlib import sha256

class Usuario(ABC):
    def __init__(self, nome:str, email:str, senha:str = None):
        self.nome = nome
        self.email= email
        if senha is None:
            senha = self.pede_senha()
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}, email: {self.email}, senha: {self.__senha}"

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
    def senha(self, senha):
        self.__senha = sha256(senha.encode()).hexdigest()
        return self.__senha

    def validar_senha(self, senha):
        if self.__senha == sha256(senha.encode()).hexdigest():
            return ("Senha confere!")
        else: 
            return ("Senha não confere")

    @abstractmethod
    def mostrar_dados(self):
        pass

class Admin(Usuario):
    def __init__(self, nome:str, email:str, senha:str = None):
        super().__init__(nome, email, senha)

    def __str__(self):
        return f"Nome: {self.nome}, email: {self.email}, senha: {self.senha}"

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nPermissão: Acesso total ao sistema")


class Cliente(Usuario):
    def __init__(self, nome:str, email:str, senha:str = None):
        super().__init__(nome, email, senha)

    def __str__(self):
        return f"Nome: {self.nome}, email: {self.email}, senha: {self.senha}"
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nPermissão: Acesso limitado ao sistema")