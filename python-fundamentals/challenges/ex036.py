print("===APROVANDO EMPRÉSTIMO===")

valor_casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
anos = int(input("Em quantos anos você quer pagar? "))

mensalidades = anos * 12
valor_mensal = valor_casa / mensalidades
porcen_sala = salario * (30/100) 

print("Sua mensalidade, levando em conta seu salário de {:.2f} e em {} anos que você deseja pagar, ficará em um valor de {:.2f}".format(salario, anos, valor_mensal))
print("Para nossos serviços o mínimo é que sua parcela não alcance 30% do seu salário, e 30% do seu sálario é {:.2f}".format(porcen_sala))
if (valor_mensal > porcen_sala): 
    print("Sua parcelas ficarão muito alta, portanto o empréstimo não foi aprovado.")
else:
    print("PArabénsss!! Seu financiamento foi aprovado!!\n")
    print("Suas parcelas ficarão no valor de {:.2f}".format(valor_mensal))    