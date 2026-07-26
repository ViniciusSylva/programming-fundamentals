print("===ANÁLISE DE DADOS DO GRUPO===")

maior_18 = homem = mulher_20 = 0

print(15*"-=")
print("  CADASTRE UMA PESSOA  ")
print(15*"-=")

while True:
    idade = int(input("Idade: "))
    if idade > 18:
        maior_18 += 1
    mf = str(input("Sexo [M-F]")).strip().upper()[0]
    if mf == "M":
        homem += 1
    elif mf == "F":
        if idade < 20:
            mulher_20 += 1    
    print(30*"-")
    flag = " "
    while flag not in "SN":
        flag = str(input("Quer continuar: [S-N]")).strip().upper()[0] 
    if flag == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior_18}")
print(f"Ao todo temos {homem} homens cadastrados")
print(f"E temos {mulher_20} mulher com menos de 20 anos")