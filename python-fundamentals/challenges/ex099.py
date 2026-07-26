import time

def maior(*nums):
    cont = maior = menor = 0
    print('-=' * 20)
    print('Analisando os valores passados...')  
    for n in nums:
        print(f'{n} ', end='', flush=True)
        time.sleep(0.5)
        cont += 1
        if cont == 0:
            maior = n
        elif n > maior:
            maior = n
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')  


    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2, 0, 0, 4)   
maior(6, 3)
maior(0)