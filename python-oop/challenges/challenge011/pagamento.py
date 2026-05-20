from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC): 

    sal_minimo = 1612
    desconto_inss = 7.5

    def __init__(self, nome = None, sal_bruto = 0, salario = 0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario


    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        mensagem = f"O salário de {self.nome} é de R${self.salario:.2f} e corresponde a {self.salario / Funcionario.sal_minimo:.2f} salários mínimos."

        painel = Panel(mensagem, title="Análise do salário", width=50, height=5, border_style="red")
        print(painel)
        


class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trab = 228):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desconto_inss / 100)


class Mensalista(Funcionario):
    
    def __init__(self, nome, sal_bruto = Funcionario.sal_minimo):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desconto_inss / 100)