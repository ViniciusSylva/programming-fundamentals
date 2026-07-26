from rich import print

class Churrasco:
    def __init__(self, nome = "", quant = 0):
        self.nome = nome
        self.quant = quant

    def Calculos(self):
        print('-=' * 50)
        print(f"Analisando [green]{self.nome}[/green] com [blue]{self.quant} convidados[/blue]")
        print(f"Cada participante comera em media 0.400Kg de carne e cada Kg custa em media R$82.40")
        print(f"Recomendo [blue]comprar {self.quant * 0.400:.2f}Kg de carne[/blue]")
        print(f"O custo total sera de [green]R${self.quant * 0.400 * 82.40:.2f}[/green]")
        print(f"Cada pessoa pagara cerca de [yellow]R${self.quant * 0.400 * 82.40 / self.quant:.2f}[/yellow]")
    
c1 = Churrasco("Churas das lendas", 15)
c1.Calculos()
        
    