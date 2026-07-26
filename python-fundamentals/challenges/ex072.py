numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input("Digite um número: "))  
    if 0 <= num <= 20:
        break    
    print("Tente novamente! Número inválido.")
    
print(f'o número digitado é o : {numeros[num]}')