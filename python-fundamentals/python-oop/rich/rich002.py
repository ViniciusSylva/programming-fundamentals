from rich import print
from rich.panel import Panel 

caixa = Panel("[yellow]Painel de teste[/yellow]", title="Título do painel", subtitle="Subtítulo do painel", border_style="red")
print(caixa)