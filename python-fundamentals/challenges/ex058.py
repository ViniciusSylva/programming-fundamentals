import random

print("===JOGO DA ADIVINHAÇÃO===")

cont = 1
num_pc = random.randint(1, 10)

print("Sou seu computador... \nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?")
palpite = int(input("Qual é o seu palpite: "))

while palpite != num_pc:
    palpite = int(input("Não foi dessa vez, qual seu novo palpite? "))
    cont += 1 
print("Parabéns!! Você acertou, com apenas {} tentativas".format(cont))    