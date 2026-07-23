from conta import Conta

def main(): 
    s1 = Conta(1750.00)
    s1.sacar(250.00)
    s1.sacar(4000.00)
    s1.depositar(-1)
    s1.depositar(-0)
    s1.depositar(5000.00)
    s1.sacar(4000)

if __name__ == "__main__":
    main()