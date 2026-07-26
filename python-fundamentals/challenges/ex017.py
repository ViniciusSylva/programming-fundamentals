print("==CALCULANDO A HIPOTENUSA==")

catetooposto = float(input("Qual o comprimento do cateto oposto? "))
catetoadjascente = float(input("Qual o comprimento do cateto adjascente? "))
hipotenusa = ((catetooposto ** 2) + (catetoadjascente ** 2)) ** 0.5
print("Baseado nos valores de cateto oposto {} e cateto adjascente {} o comprimento da hipotenusa é {:.2f}".format(catetooposto, catetoadjascente, hipotenusa))