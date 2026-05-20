from rich import print, inspect
from rich.table import Table
from transportadora import *

def main():
    dist = 54

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    # entrega_moto = Moto(dist)
    # print(f"Frete de {type(entrega_moto).__name__} em {dist}km: {entrega_moto.calcular_frete()}")

    # entrega_caminhao = Caminhao(dist)
    # print(f"Frete de {type(entrega_caminhao).__name__} em {dist}km: {entrega_caminhao.calcular_frete()}")

    # entrega_drone = Drone(dist)
    # print(f"Frete de {type(entrega_drone).__name__} em {dist}km: {entrega_drone.calcular_frete()}")

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância (km)", justify="center", style="cyan", no_wrap=True)
    tabela.add_column("Tipo de Transporte", justify="center", style="magenta")
    tabela.add_column("Valor do Frete (R$)", justify="center", style="green")

    for item in viagem:
        tabela.add_row(f"{dist}km", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)

if __name__ == "__main__": 
    main()