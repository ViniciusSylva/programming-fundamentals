from classes import *

def main():
    funcionarios = [
        Desenvolvedor("Viny", 22000),
        Designer("Yoru", 12500),
        Gerente("Maria", 22500)
    ]

    for f in funcionarios:
        print(f)

if __name__ == "__main__":
    main()