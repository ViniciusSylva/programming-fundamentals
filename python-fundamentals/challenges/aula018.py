galera = list()
dados = list() 
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome? ' )))
    dados.append(int(input('Idade? ')))
    galera.append(dados[:]) #galera recebe uma cópia de dados
    dados.clear() #limpa a lista dados para receber os próximos dados
    print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'P{[0]} é maior de idade.')
        totmai += 1
    else: 
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')




#For = para cada
#p = pessoa
#in = em
#galera = [['João', 19], ['Maria', 22], ['Pedro', 20]]