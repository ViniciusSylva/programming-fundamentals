from contabancaria import *

def main():
    cc = ContaBancaria(111, "Vini", 7800)

    print("Vou tentar sacar..")
    cc.sacar(500)

    print("Tentando alterar o nome..")
    cc.nome = ""

    print(cc)

if __name__ == "__main__":
    main()