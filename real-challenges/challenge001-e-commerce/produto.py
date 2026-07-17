class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome 
        self.preco = preco
        self.estoque = estoque 
        if estoque < 0:
            print(f'Estoque n aceita valor negativo, valor inserido de {self.estoque}')


class Carinho(produto):
    def __init__(self, carrinho = 0, valor_total = 0):
        self.carrinho = carrinho
        self.valor_total = valor_total

    def adicionar_produto(self):
        self.carrinho += self.preco
        print(f'Adicionando produto de valor {self.valor } no carrinho, atualmente o carinho tem o valor de {self.carrinho}')

    def remover_produto(self):
        self.carrinho -= self.precp
        print(f'Removendo produto de valor {self.valor} do carrinho, atualmente o carrinho tem o valor de {self.carrinho}')

    def calcular_total(self):
        print(f'O valor total do seu carrinho é de {self.carrinho}')