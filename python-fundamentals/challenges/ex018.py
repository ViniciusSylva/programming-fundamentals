from math import radians, sin, cos, tan

print("==CALCULO DO SENO E DO COSSENO==")

angulo = float(input("Digite um ângulo para que eu possa calcular seu seno e seu cosseno: "))
seno = sin(radians(angulo)) 
print("O ãngulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))