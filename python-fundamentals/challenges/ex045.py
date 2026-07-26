from random import randint
from time import sleep

print("===GAME: PEDRA PAPEL E TESOURA===")

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("Suas opções: \n" \
"[ 0 ] PEDRA \n" \
"[ 1 ] PAPEL \n" \
"[ 2 ] TESOURA \n")

jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POOO!!!")
sleep(1)

print("-=" * 11)
print("O computador jogou {}".format(itens[computador]))
print("o jogador jogou {}".format(itens[jogador]))
print("-=" * 11)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador ==2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!!")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:    
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!!")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!!")