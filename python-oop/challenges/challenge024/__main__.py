from rh_empresa import * 

def main():
    f1 = Funcionario(nome = "Carlos")
    f1.meu_salario()

    f2 = Gerente("Camila", 5200)
    f2.meu_salario()

    f3 = Desenvolvedor("Vinicius", 8600)
    f3.meu_salario()


if __name__ == "__main__":
    main()