from login import Credencial

def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: "))
    print(c.senha)

    c.validar("Testando")


if __name__ == "__main__":
    main()