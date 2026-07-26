from rich import print, inspect
from poligono import Quadrado, Circulo

def main():
    p1 = Quadrado(12)
    p2 = Circulo(5)

    print(f"Área = {p1.area()}")
    print(f"Perímetro = {p1.perimetro()}")
    print(f"Área = {p2.area():.2f}")
    print(f"Perímetro = {p2.perimetro():.2f}")

if __name__ == "__main__":
    main()