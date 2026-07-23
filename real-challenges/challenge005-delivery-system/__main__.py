from logistica import *

def main():
    p1 = Pedido("1", 120.00, "Preparando")
    print(p1)
    p1.atualizar_status()
    p1.calcular_frete()
    p1.atualizar_status()

    print("=-" * 20)

    p2 = EntregaNormal("2", 510.00, "Finalizado")
    print(p2)
    p2.atualizar_status()
    p2.calcular_frete()

    print("=-" * 20)

    p3 = EntregaExpressa("3", 1200.00, "Preparando")
    print(p3)
    p3.atualizar_status()
    p3.calcular_frete()

if __name__ == "__main__":
    main()