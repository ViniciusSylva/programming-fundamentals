from time import sleep

print("===CRIANDO MENU DE OPÇÕES===")

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
menu = 0

    
while menu != 5:
    
    print("\n===MENU DE OPÇÕES===")
    print("[ 1 ]  SOMAR")
    print("[ 2 ]  MULTIPLICAR")
    print("[ 3 ]  SABER O MAIOR")
    print("[ 4 ]  NOVOS NÚMEROS")
    print("[ 5 ]  SAIR DO PROGRAMA")
    menu = int(input("OQUE VOCÊ DESEJA FAZER COM ESSES NÚMEROS: "))
    
    if menu == 1:
        tot_soma = num1 + num2
        print("A soma dos números deu {}".format(tot_soma))
    elif menu == 2:
        tot_multi = num1 * num2
        print("A multiplicação dos dois números deu {}".format(tot_multi))
    elif menu == 3:
        if num1 > num2:
            maior = num1
            print("O maior número é o {}".format(maior))
        elif num2 > num1:
            maior = num2 
            print("O maior número é o {}".format(maior))
        else:
            print("Os números tem o mesmo valor")  
    elif menu == 4:
        print("Informe os números novamente: ")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif menu == 5:
        print("Finalizando...")
    else:  
        print("Opção inválida. Tente novamente")  
    print("==-" * 10)
    sleep(2)
print("Fim do programa! Volte sempre!")                    