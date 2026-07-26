print("==Radar eletrônico==")

vel = int(input("Qual é a velocidade atual do carro? "))

if vel > 80:
    velacima = vel - 80
    multa = velacima * 7
    print("Você foi multado, está a {}km acima do permito, sua multa é de ${} reais".format(velacima, multa))
else:
    print("Muito bom!! você está dentro da velocidade permitida!!")