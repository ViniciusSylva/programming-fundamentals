expre = str(input('Digite a expessão matemática: '))
pilha = list()
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break 
for n in range(0, 10):
    if n % 2 == 0:
        print(f'O número {n} é par.')

print('=-' * 30)
if len(pilha) == 0:
    print('Sua expressão está válida!!!')
else:
    print('Sua espressão está inválida!!!')    