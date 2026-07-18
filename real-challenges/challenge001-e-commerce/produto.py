class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome 
        self.preco = preco
        self.estoque = estoque


class Carrinho():
    def __init__(self):
        self.itens_carrinho = {}
        self.valor_carrinho = 0

    def adicionar_produto(self, produto, quantidade):
        if quantidade > produto.estoque:
            print(f'O estoque não tem toda essa quantidade de {produto.nome}. (Disponível: {produto.estoque})')
            return
        
        if produto in self.itens_carrinho:
            self.itens_carrinho[produto] += quantidade
        else:
            self.itens_carrinho[produto] = quantidade
            
        produto.estoque -= quantidade
        self.valor_carrinho += (produto.preco * quantidade)  
        print(f'{quantidade}x {produto.nome} (R${produto.preco:.2f} cada) adicionado ao carrinho.')

    def remover_produto(self, produto, quantidade):
        if produto not in self.itens_carrinho:
            print(f'O produto {produto.nome} não está no carrinho.')
            return

        quantidade_no_carrinho = self.itens_carrinho[produto]
        if quantidade > quantidade_no_carrinho:
            print(f'Quantidade que você está tentando remover ({quantidade}) é maior do que você tem no carrinho ({quantidade_no_carrinho})')
            return
        
        self.itens_carrinho[produto] -= quantidade
        if self.itens_carrinho[produto] == 0:
            del self.itens_carrinho[produto]
            
        produto.estoque += quantidade
        self.valor_carrinho -= (produto.preco * quantidade)
        print(f'{quantidade}x {produto.nome} removido do carrinho.')

    def calcular_total(self):
        if not self.itens_carrinho:
            print('O carrinho está vazio')
        else: 
            print(f'O valor total é de: R${self.valor_carrinho:.2f}')

