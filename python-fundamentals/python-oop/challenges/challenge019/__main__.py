from produto import Produto, Carrinho

def main():
    p1 = Produto("camisa", 50.00, 10)

    meu_carrinho = Carrinho()
    meu_carrinho.adicionar_produto(p1, 2)
    meu_carrinho.calcular_total()
    
    meu_carrinho.remover_produto(p1, 2)
    meu_carrinho.calcular_total()

if __name__ == "__main__":
    main()