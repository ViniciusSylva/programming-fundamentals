class Funcionario():
    def __init__(self, nome, salario = 1621.00): # Salário mínimo no momento
        self.nome = nome
        self.salario = salario

    def meu_salario(self):
        print(f"Meu salário é de {self.salario}")


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

        self.salario_novo = self.salario + (self.salario / 5)

    def meu_salario(self):
        print(f"Meu salário é {self.salario}, mas por eu ser gerente tenho bônus de 20% adicional que um salário de {self.salario_novo}")


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

        self.salario_novo = self.salario + (self.salario / 10)

    def meu_salario(self):   
        print(f"Meu salário é {self.salario}, mas por eu ser desenvolvedor tenho bônus de 10% adicional que um salário de {self.salario_novo}")
