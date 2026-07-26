print("===TABUADA V3.0===")

while True:
    tabuada = int(input("Quer ver a tabuada de qual número: "))
    c = 0
    if tabuada < 0:
        break
    print(15*"==")
    while c <= 10:
        result = tabuada * c
        print(f"{tabuada} x {c} = {result}")
        c += 1
    print(15*"==")    
print("FIM!!")        