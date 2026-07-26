print("==Custo da viagem==")

dis = int(input("Quantos Km tem sua viagem? "))

if dis <= 200:
    preçoviagem = dis * 0.50
    print("O preço da passagem para essa quantidade de Km é de ${:.2f} Reais".format(preçoviagem))
if dis > 200:
    preçoviagem = dis * 0.45
    print("O preço da passagem para essa quantidade de Km é de ${:.2f} Reais". format(preçoviagem))
else:
    print("[ERRO!!] Você informou a quantidade de Km de forma incorreta!")