import random

print("===JOGO DO PAR OU ÍMPAR===")

cont = 0

print(15*"-=")
print("VAMOS JOGAR PAR OU ÍMPAR")
print(15*"-=")

while True:
    num = int(input("Digite um valor: "))
    computador = random.randint(1, 20)
    resultado = num + computador
    tipo = " "
    while tipo not in "IP":
        tipo = str(input("Par ou Ímpar [P-I]: ")).strip().upper()[0]
    print(f"Você jogou {num} e o computador {computador}. O resultado deu {resultado} ", end="")
    print("DEU PAR" if resultado % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if resultado % 2 == 0:
            print("VOCÊ VENCEU!")
            cont += 1
        else:
            print("VOCÊ PERDEU!")  
            break  
    elif tipo == "I": 
        if resultado % 2 == 1:
            print("VOCÊ VENCEU!")
            cont += 1
        else:
            print("VOCÊ PERDEU!")
            break
    print("Vamos jogar novamente...")    
print(15*"-=")
print(f"GAME OVER! Você venceu {cont} vezes.")    