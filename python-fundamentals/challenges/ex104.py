def leiaint(num):
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
            num = input('Digite um número: ')

n = leiaint(input('Digite um número: '))
print(f'Você digitou o número {n}.')