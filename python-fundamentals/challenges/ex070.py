print("===ESTATÍSTICAS EM PRODUTOS===")

maisbaratostr = ""
maisbaratofloat = contproduto = total = 0

print(15*"-=")
print("  LOJA SUPER BARATÃO  ")
print(15*"-=")

while True:
    c = 0 
    produto = str(input("Nome do Produto: "))
    preço = float(input("Preço: R$"))
    if preço > 1000:
        contproduto += 1
    total += preço    
    if c == 0:
        maisbaratostr = produto
        maisbaratofloat = preço
        c += 1
    elif preço > maisbaratofloat:  
        maisbaratofloat = preço
        maisbaratostr = produto   
    tipo = " "
    while tipo not in "SN":
        tipo = str(input("Quer continuar: [S-N] ")).strip().upper()[0]
    if tipo == "N":
        break
print("-=-=-=-=FIM DAS COMPRAS-=-=-=-=")
print(f"O total da compra foi {total:.2f}")
print(f"Temos {contproduto} acima de R$1000 reais")
print(f"O produto mais barato foi {maisbaratostr} que custa {maisbaratofloat}")        