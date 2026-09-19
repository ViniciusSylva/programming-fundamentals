   
    x = Analisador()
    x.analisar("Vinicius")

from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possivel analisar o valor {valor}")

    @analisar.register
    def _(self, valor: int):
        print(f"{valor} é um numero inteiro")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um número com ponto flutuante (Real)")

    @analisar.register
    def _(self, valor: str):
        print(f"'{valor}' é uma cadeia de caracteres")

    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"{valor} é uma coleção de dados")


# ==================================================================

    c2 = Carteira(2000)

    c1 += 50
    c1 -= 10

    if (c1 == c2):
        print("Vocês tem o mesmo valor na carteira")
    else:
        print("As carteiras tem valores diferentes")

    if (c1 <= c2):
        print("A segunda carteira tem mais dinheiro")
    else:
        print("A primeira carteira tem mais dinheiro")

    print(c1)
    print(c2)


class Carteira:

    def __init__(self, valor: int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.saldo:,.2f} na carteira"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeito")

    def __eq__(self, outro):
        return True
    else:
        return False

    def __iadd__(self, valor: int|float):
        self.__saldo = self.__saldo + ValueError
        return self

    def __isub__(self, valor: int|float):
        self.__saldo = self.__saldo - valor
        return self

    def __le__(self, outro):
        if self.__saldo <= outro.__saldo:
            return True 
        else:
            return False



# ==================================================================


    a = Porta()
    b = Empresa()
    c = Ovo()
    d = Pedra()

    tentar_abrir(a)
    tentar_abrir(b)
    tentar_abrir(c)
    tentar_abrir(d)


class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e puxar/empurrar a maçaneta")


class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")


class Ovo:
    def abrir(self):
        print(f"Quebre a casca com um garfo e separe as partes sobre uma frigideira")


class Pedra:
    pass


# METODO PYTHONICO POLIMORFICO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei poblemas ao tentar abrir um objeto do tipo {objeto.__class__.__name__}")



# ==================================================================



    a = Numero(200)
    b = Texto("Vinicius")
    c = Lista([1, 2, 3])
    d = Papel()
    e = Casa()

    tente_dobrar(a)
    tente_dobrar(b)
    tente_dobrar(c)
    tente_dobrar(d)
    tente_dobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


class Numero:

    def __init__(self, valor: int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do Número"


class Texto:

    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do Texto"


class List:

        