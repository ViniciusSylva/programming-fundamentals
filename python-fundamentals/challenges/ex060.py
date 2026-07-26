print("===CÁLCULO DO FATORIAL===")

n = int(input("Digite um número para\nCalcular o seu fatorial: "))
c = n
f = 1
print("Calculando {}! ".format(n), end="")
while c > 0:
    cont = n - 1
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))    