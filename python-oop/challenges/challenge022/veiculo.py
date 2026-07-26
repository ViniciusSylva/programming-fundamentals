class Veiculo():
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        print(f"O {self.modelo} está acelerando a {self.velocidade} km/h.")
        

class Carro(Veiculo):
    def __init__(self, modelo, velocidade):
        super().__init__(modelo, velocidade)

    def acelerar(self):
        print(f"O {self.modelo} está acelerando a {self.velocidade} km/h. Parecendo de foguete")
        

class Moto(Veiculo):
    def __init__(self, modelo, velocidade):
        super().__init__(modelo, velocidade)

    def acelerar(self):
        print(f"A {self.modelo} está acelerando a {self.velocidade} km/h. Quase se desmanchando")

        
class Caminhao(Veiculo):
    def __init__(self, modelo, velocidade):
        super().__init__(modelo, velocidade)

    def acelerar(self):
        print(f"O {self.modelo} está acelerando a {self.velocidade} km/h. bem na lenta")