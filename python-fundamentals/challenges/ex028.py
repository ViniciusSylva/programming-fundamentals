import random

print("==Jogo da adivinhação==")

print("O computador irá pensar em um número entre 0 e 5 e você terá que adivinhar qual número ele pensou.")
numcomp = random.randint(0, 5)
print("O computador já pensou em um número.")
numuser = int(input("Qual número e você acha q é? "))

if numuser == numcomp:
    print("Parabénssss!! Você acertou")
if numuser > 5:
    print("ERRO! Você não digitou um número dentro do pedido")    
else:
    print("Você errou, tente de novo!")
    print("O número era {}".format(numcomp))