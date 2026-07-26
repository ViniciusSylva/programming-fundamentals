palavras = ('Efervescente', 'Resiliencia', 'Crepusculo', 'Efemero', 
            'Serenidade', 'Peculiar', 'Eloquencia', 'Alento', 'Inefavel', 
            'Perspicacia', 'Melancolia', 'Pragmatico', 'Deleite', 'Aureola', 
            'Fugaz', 'Plenitude', 'Harmonia', 'Vertigem', 'Essencia', 'Gratidao')

for pos in palavras:
    print(f'\nNa palavra {pos.upper()} temos: ', end = '')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end = ' ')