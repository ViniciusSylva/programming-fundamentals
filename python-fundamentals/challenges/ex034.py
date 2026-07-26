print("==Aumentos múltiplos==")

salario = float(input("Qual o salário do funcionário? "))

if salario < 1250: 
    sal15 = (salario / 100 * 15) + salario
    print("Esse salário teve um aumento de 15%, agora o salário tem o valor de {:.2f}".format(sal15))
else:
    sal10 = (salario / 100 * 10) + salario
    print("Esse salário teve um aumento de 10%, agora o salário tem o valor de {:.2f}".format(sal10))    