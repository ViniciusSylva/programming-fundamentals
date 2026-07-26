print("===SEGUÊNCIA DE FIBONACCI===")

quant_termos = int(input("Quantos termos da seguência você quer mostrar: "))
c = 0
primeiro_termo = 0
segundo_termo = 1

print((primeiro_termo), end=" -> ")
print((segundo_termo), end=" -> ")

while c <= quant_termos - 3: 
    terceiro_termo = primeiro_termo + segundo_termo 
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo   
    print((terceiro_termo), end=" -> ")
    quant_termos -= 1
print("FIM!")    