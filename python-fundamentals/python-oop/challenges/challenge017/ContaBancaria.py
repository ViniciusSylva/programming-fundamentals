from hashlib import sha256

class ContaBancaria: 
    '''
    Cria uma conta bancária com um número de conta e um saldo inicial.
    '''
    def __init__(self, id:int, name:str = None, saldo:float = 0, chave:str = None):
        self._id = id
        self._name = name
        self.__saldo = saldo

        if chave is None: 
            chave = self.pede_senha()

        self.__hash = sha256(chave.encode()).hexdigest()

        print(f"Conta {self._id} criada para {self._name} com saldo inicial de R$ {self.__saldo:.2f}")

    def pede_senha(self) -> str:

        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break

        return senha 

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        #return f"Estado atual da conta: {self.__dict__}"
        return f"A conta {self._id} pertence a {self._name} e tem um saldo atual de R${self.__saldo:.2f}."
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de valor R$ {valor:.2f} autorizado com sucesso. Na conta {self.id}")

    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)

        if chave is None: 
            chave = self.pede_senha()

        if self.validar_senha(chave):            
            if valor > self.__saldo:
                print(f"\033[31mSaque no valor de R$ {valor:.2f} nao autorizado. Saldo insuficiente na conta {self._id}\033[0m")
            else:
                self.__saldo -= valor
                print(f"\033[32mSaque de valor R$ {valor:.2f} autorizado com sucesso. Na conta {self._id}\033[0m")
        else:
            print("Senha não confere, saque não autorizado!")

    @property
    def nome(self):
        return self.name

    @nome.setter
    def nome(self, novonome:str):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self.name = novonome
        else:
            print("Senha não confere. Não posso alterar o nome!")