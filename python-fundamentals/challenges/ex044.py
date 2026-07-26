print("===GERENCIADOR DE PAGAMENTOS===")

valor = float(input("Qual o valor do produto? "))
forma_de_pagamento = int(input("Temos várias formas de pagamento? \n"
"[1] Para á vista dinheiro/cheque (10% de desconto)\n"
"[2] Para á vista no cartão (%5 de desconto)\n" 
"[3] Para em até 2x no cartão (preço normal)\n" 
"[4] Para 3x ou mais no cartão (20% de juros)\n"
"Escolha a forma de pagamento: "))

if forma_de_pagamento == 1:
    valor = valor - (valor * 0.10)
    print("Com 10% de desconto seu produto passou a custar {:.2f}".format(valor))
elif forma_de_pagamento == 2:
    valor = valor - (valor * 0.05)
    print("Com %5 de desconto seu produto passou a custar {:.2f}".format(valor))
elif forma_de_pagamento == 3:
    print("Pagando em 2x seu produto permanece no valor de {:.2f}".format(valor))
elif forma_de_pagamento == 4:
    valor = valor + (valor * 0.20) 
    print("Com 20% de juros seu produto fica no valor de {:.2f}".format(valor))
else:
    print("[ERRO] Você não escolheu uma opção correta!!")                 