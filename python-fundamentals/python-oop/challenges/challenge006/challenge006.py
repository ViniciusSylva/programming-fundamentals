from rich import print

class Caneta: 
    def __init__(self, cor = "azul", ):
            cor_lower = cor.lower().strip()
            if cor_lower == "azul":
                escolha = "[blue]"
            elif cor_lower == "verde":
                escolha = "[green]"
            elif cor_lower == "vermelha":
                escolha = "[red]"
            else:
                escolha = "[white]"
        
            self.cor = escolha
            self.tampada = True
        

    def escrever(self, texto):
        if self.tampada:
            print("[red]prohibited: A caneta esta tampada![/red]")
            return
        
        print(f"{self.cor}[/]", end="")
        print(f"{self.cor}{texto}[/]", end="")

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd)

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta("azul")
c2 = Caneta("verde")
c3 = Caneta("vermelha")

c1.destampar()
c2.destampar()



c1.escrever("Ola, tudo bem? \n")
c2.escrever("Funcionando \n")        
c3.escrever("Estou escrevendo com a caneta vermelha. \n")

c2.quebrar_linha(4)

c1.tampar()
c1.escrever("Nao consigo escrever, a caneta esta tampada. \n ")
c2.escrever("A caneta 1 foi tampada. \n")   