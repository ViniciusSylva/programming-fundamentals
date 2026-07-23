from conta import *

def main(): 
    c1 = ContaCorrente(saldo=1750.00)
    c1.depositar(250.00)
    c1.sacar(1200)

    c2 = ContaPoupanca(saldo=1000)
    c2.sacar(250)
    c2.render_juros(0.01)

if __name__ == "__main__":
    main()