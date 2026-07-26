print("==AREDONDAMENTO DO NÚMERO==")

from math import trunc
numreal = float(input("Digite um número real: "))
numint = trunc(numreal)
print("A porção inteira de {} é {}".format(numreal, numint))