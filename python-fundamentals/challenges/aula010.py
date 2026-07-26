n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
print("A sua média foi {:.1f}".format(media))
if media >= 6:
    print("Parabéns, você está na média!!")
else:
    print("Você está abaixo da média, tem que estudar mais!!")    