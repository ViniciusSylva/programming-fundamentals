from sistema_funcionarios import * 

def main():
    ger = Gerente("João", 5000, "apenasteste")
    ger.calcular_bonus()
    ger.senha = "testando"
    ger.autenticar("deubom?")

    dev = Desenvolvedor("Maria", 4000, "teste")
    dev.calcular_bonus()

    print(ger)
    print(dev)

if __name__ == "__main__":
    main()