class Pedido():
    def __init__(self, id, valor, status):
        self.id = id
        self.valor = valor
        self.status = status

    def __str__(self):
         return f"Pedido {self.id} - Valor: {self.valor} - Status: {self.status}"

    def atualizar_status(self):
        if self.status == "Preparando":
            self.status = "Em andamento"
        elif self.status == "Em andamento":
            self.status = "Finalizado"
        else:
            self.status = "Finalizado"

    def calcular_frete(self):
        self.valor_total = self.valor + 10
        print(f"Seu pedido no valor de {self.valor} tem uma adição de taxa de entrega de entrega de 10,00 R$! Valor total do pedido: {self.valor_total:.2f}")


class EntregaNormal(Pedido):
        def __init__(self, id, valor, status):
            super().__init__(id, valor, status)

        def atualizar_status(self):
            if self.status == "Preparando":
                self.status = "Em andamento"
            elif self.status == "Em andamento":
                self.status = "Finalizado"
            else:
                self.status = "Finalizado"

        def calcular_frete(self):
            self.valor_total = self.valor
            print(f"Seu pedido no valor de {self.valor:.2f} com a taxa de entrega normal o frete é grátis! Valor total do pedido: {self.valor_total:.2f}")


class EntregaExpressa(Pedido):
        def __init__(self, id, valor, status):
            super().__init__(id, valor, status)

        def atualizar_status(self):
            if self.status == "Preparando":
                self.status = "Em andamento"
            elif self.status == "Em andamento":
                self.status = "Finalizado"
            else:
                self.status = "Finalizado"

        def calcular_frete(self):
            self.valor_total = self.valor + 20
            print(f"Seu pedido no valor de {self.valor:.2f} tem uma adição de taxa de entrega de entrega de 20,00 R$ por ser entrega expressa! Valor total do pedido:  {self.valor_total:.2f}")