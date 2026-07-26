from rich import print
import time

class Livro:
    def __init__(self, titulo = "", paginas = 0):
        self.titulo = titulo 
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f"[blue]Voce acabou de abrir o livro [red]'{self.titulo}'[/red] que tem {self.total_paginas} paginas no total. Voce esta na pagina [yellow]{self.pagina_atual}[/yellow][/blue]")

    
    def Avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"pag{self.pagina_atual} :arrow_forward: ", end="")
                time.sleep(0.3)
                cont += 1
        print(f"\nVoce avancou {cont} paginas e esta na pagina {self.pagina_atual}")
        if self.fim_do_livro():
            print(f"[red]Voce chegou ao fim do livro {self.titulo}[/red]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False


l1 = Livro("Algoritimos de programacao", 20)
print(l1)
l1.Avancar_paginas(5)
l1.Avancar_paginas(10)
l1.Avancar_paginas(50)