print("==PINTAR UMA PAREDE==")
altura = float(input("Quantos metros de altura tem sua parede? "))
largura = float(input("E quantos metros de largura tem sua parede? "))
total_da_parede = altura * largura 
print("Cada balde de tinta pinta 2m quadrado")
tinta = 2
total_de_tinta = total_da_parede / tinta
print("Então para pintar sua parede que possui {} metros quadrados. \nSerão usados {:.2f} baldes de tinta!". format(total_da_parede, total_de_tinta))