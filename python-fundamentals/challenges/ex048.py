("===SOMA ÍMPARES MÚLTIPLOS DE TRÊS===")

cont = 0 
totnum = 0

for i in range(1, 501, 1):
    if i % 3 == 0:
        cont += i
        totnum += 1
print("A soma dos {} valores é: {}".format(totnum, cont))        