'''
def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f += c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
print(f'O fatorial de 5 é {f1}')
'''

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))

if par(num):
    print('O número é par.')
else:
    print('O número é ímpar.')