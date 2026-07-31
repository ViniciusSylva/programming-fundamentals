from sistema_funcionarios import * 

def main():
    ger = Gerente("João", 5000, "123456")
    ger.calcular_bonus()

    dev = Desenvolvedor("Maria", 4000, "teste")
    dev.calcular_bonus()

if __name__ == "__main__":
    main()