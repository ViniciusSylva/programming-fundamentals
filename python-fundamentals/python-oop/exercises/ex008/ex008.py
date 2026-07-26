class ContaBancaria: 
    '''
    Cria uma conta bancária com um número de conta e um saldo inicial.
    '''
    def __init__(self, id, name, saldo = 0):
        self.id = id
        self._name = name
        self.__saldo = saldo
        print(f"Conta {self.id} criada para {self._name} com saldo inicial de R$ {self.__saldo:.2f}")

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"
        #return f"A conta {self.id} pertence a {self.name} e tem um saldo atual de R${self.saldo:.2f}."
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de valor R$ {valor:.2f} autorizado com sucesso. Na conta {self.id}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"\033[31mSaque no valor de R$ {valor:.2f} nao autorizado. Saldo insuficiente na conta {self.id}\033[0m")
        else:
            self.__saldo -= valor
            print(f"\033[32mSaque de valor R$ {valor:.2f} autorizado com sucesso. Na conta {self.id}\033[0m")