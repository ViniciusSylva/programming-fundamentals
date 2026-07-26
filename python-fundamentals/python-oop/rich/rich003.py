from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome", justify="right", style="red")
tabela.add_column("Preço", justify="right", style="green")
tabela.add_row("Livro", "R$ 50,00")
tabela.add_row("Caneta", "R$ 5,00")
print(tabela)