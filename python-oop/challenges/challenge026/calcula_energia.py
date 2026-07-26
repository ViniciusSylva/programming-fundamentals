class Aparelho():
    def __init__(self, nome, consumo_kwh, horas_dia):
        self.nome = nome
        self.consumo_kwh = consumo_kwh
        self.horas_dia = horas_dia

    def calcular_consumo_total(self):
        return self.consumo_kwh * self.horas_dia

    def calcular_co2(self):
        return (self.consumo_kwh * self.horas_dia) * 0.10
       

class CalculadoraEnergia():
    def __init__(self):
        self.aparelhos = []

    def adicionar_aparelho(self, aparelho):
        self.aparelhos.append(aparelho)

    def calcular_consumo_total(self):
        consumo_total = 0

        for aparelho in self.aparelhos:
            consumo_total += aparelho.calcular_consumo_total()

        return consumo_total
    
    def calcular_co2_total(self):
        return sum(aparelho.calcular_co2() for aparelho in self.aparelhos)