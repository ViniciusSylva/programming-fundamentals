print("==DESCONTO DO PRODUTO==")
produto = float(input("Qual o preço do seu produto?"))
desconto = (produto / 100) * 5
preçofinal = produto - desconto
print("Seu produto com nossa taxa de desconto de 5% ficará: ", preçofinal)