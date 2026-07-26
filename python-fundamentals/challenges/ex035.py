print("==Analisando triângulo==")

r1 = float(input("Primeiro Seguimento: "))
r2 = float(input("Segundo Seguimento: "))
r3 = float(input("Terceiro Seguimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos PODEM FORMAR um triângilo!") 
else:
    print("Os seguimentos NÃO PODEM formar um triângulo!")
    