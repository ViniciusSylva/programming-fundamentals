from veiculo import *

def main():
    v1 = Veiculo("Astra", 100)
    v1.acelerar()

    print("==--" * 20)

    v2 = Carro("Chevete", 100)
    v2.acelerar()

    print("==--" * 20)

    v3 = Moto("Fan 160", 100)
    v3.acelerar()

    print("==--" * 20)

    v4 = Caminhao("Montertruck", 100)
    v4.acelerar()

if __name__ == "__main__":
    main()