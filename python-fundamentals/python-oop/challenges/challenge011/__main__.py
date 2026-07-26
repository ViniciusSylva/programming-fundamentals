from rich import print, inspect
from pagamento import Funcionario, Horista, Mensalista

def main():
    f1 = Mensalista("João da Silva", 8500)
    f2 = Horista("Maria Oliveira", 25, 250)
    f1.calc_salario()
    f1.analisar_salario()  
    f2.calc_salario()   
    f2.analisar_salario()


if __name__ == "__main__":
    main()