def dobro(*nums):
    print('-=' * 15)
    for n in nums:
        print(f'O dobro de {n} é {n * 2}', end=' ')
        print()
    print('-=' * 15)

totnum = int(input('Quantos números deseja dobrar? '))
list = []
for c in range(0 , totnum):
    list.append(int(input(f'Número {c + 1}: ')))

dobro(*list)