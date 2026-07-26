from rich import print
from rich import inspect   

class Produto:

    def __init__(self, nome = "", preco = 0.0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return print(f"Produto: {self.nome} - Preco R$ {self.preco:.2f}")
        
    
p1 = Produto("Thinkpad", 2700.00)
p2 = Produto("TV 43 Polegadis", 1500.00)

p1.etiqueta()
p2.etiqueta()