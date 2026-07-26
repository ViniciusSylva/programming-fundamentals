class ContaBancaria: 
    '''
    Cria uma conta bancária com um número de conta e um saldo inicial.
    '''
    def __init__(self, id, name, saldo = 0):
        self.id = id
        self.name = name
        self.saldo = saldo
        print(f"Conta {self.id} criada para {self.name} com saldo inicial de R$ {self.saldo:.2f}")

    def __str__(self):
        return f"A conta {self.id} pertence a {self.name} e tem um saldo atual de R${self.saldo:.2f}."
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de valor R$ {valor:.2f} autorizado com sucesso. Na conta {self.id}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"\033[32mSaque de valor R$ {valor:.2f} autorizado com sucesso. Na conta {self.id}\033[0m")
        else:
            print(f"\033[31mSaque no valor de R$ {valor:.2f} nao autorizado. Saldo insuficiente na conta {self.id}\033[0m")

c1 = ContaBancaria(123, "Ana", 2180.00)
c1.depositar(1200.00)
c1.sacar(1175.00)
print(c1)