from calcula_energia import *

def main(): 
    calc = CalculadoraEnergia()

    calc.adicionar_aparelho(Aparelho("Geladeira", 0.15, 24))  
    calc.adicionar_aparelho(Aparelho("Ar Condicionado", 1.2, 8)) 

    total_kwh = calc.calcular_consumo_total()
    total_co2 = calc.calcular_co2_total()

    print(f"Consumo Total Diário: {total_kwh:.2f} kWh")
    print(f"Emissão Total de CO2: {total_co2:.2f} kg")

if __name__ == "__main__": 
    main()