print("===CONVERSOR DE BASES NUMÉRICAS===")

num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para a conversão: \n" 
"[ 1 ] Converter para BINÁRIO\n" 
"[ 2 ] Converter para OCTAL\n" 
"[ 3 ] Converter para HEXADECIMAL")
opção = int(input("Sua opção: "))

if opção == 1:
    print("{} convertido para binário é igual a {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para hexadecimla é {}".format(num, hex(num)[2:])) 
else:
    print("Opção inválida!!")           