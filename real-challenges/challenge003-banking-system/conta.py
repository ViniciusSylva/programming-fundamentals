class Conta:
    def __init__(self, saldo=0.0):
        self._saldo = saldo 

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self._saldo:.2f}")
        else:
            print(f"Erro! Valor R$ {valor:.2f} inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if valor > self._saldo:
            print(f"Saldo insuficiente! Saldo disponível: R$ {self._saldo:.2f}")
            return False

        self._saldo -= valor
        return True


class ContaCorrente(Conta):
    def __init__(self, saldo=0.0, taxa_saque=2.50):
        super().__init__(saldo)
        self.taxa_saque = taxa_saque 

    def sacar(self, valor):
        valor_total = valor + self.taxa_saque
        print(f"\n[Conta Corrente] Tentando sacar R$ {valor:.2f} (Taxa: R$ {self.taxa_saque:.2f})")
        
        
        if super().sacar(valor_total):
            print(f"Saque efetuado com sucesso! Saldo atual: R$ {self._saldo:.2f}")


class ContaPoupanca(Conta):
    def __init__(self, saldo=0.0, taxa_saque=0.50):
        super().__init__(saldo)
        self.taxa_saque = taxa_saque  

    def sacar(self, valor):
        valor_total = valor + self.taxa_saque
        print(f"\n[Conta Poupança] Tentando sacar R$ {valor:.2f} (Taxa: R$ {self.taxa_saque:.2f})")
        
        if super().sacar(valor_total):
            print(f"Saque efetuado com sucesso! Saldo atual: R$ {self._saldo:.2f}")

    def render_juros(self, taxa_percentual=0.005):
        rendimento = self._saldo * taxa_percentual
        self._saldo += rendimento
        print(f"[Poupança] Rendimento de R$ {rendimento:.2f} aplicado. Novo saldo: R$ {self._saldo:.2f}")