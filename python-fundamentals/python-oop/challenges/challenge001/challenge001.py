from rich import print
from rich import inspect

class Funcionario: 
    # atributo de classe
    empresa = "Wind Digital"


    def __init__(self, nome = "", setor = "", cargo = ""):
        # atributo de instance
        self.nome = nome
        self.setor = setor 
        self.cargo = cargo 

    # metodo de instance
    def apresentacao(self):
        return f"Ola, meu nome e {self.nome}, trabalho no setor de {self.setor} e meu cargo e {self.cargo} da empresa {Funcionario.empresa}."
    
f1 = Funcionario("Camila", "Licitacao", "Recepicionista")
print(f1.apresentacao())
inspect(f1, methods=True)

f2 = Funcionario("Viny", "TI", "Desenvolvedor de Software")
print(f2.apresentacao())
inspect(f2, methods=True)