def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n   
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return n
    
n1 = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n1}')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {n2:.2f}')