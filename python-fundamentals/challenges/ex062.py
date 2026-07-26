print("===SUPER PROGRESSÃO ARITIMÉTICA V3.0===")

p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
t = p
c = 1
while c <= 10:
    print("{} -> ".format(t), end="")
    t += r
    c += 1
