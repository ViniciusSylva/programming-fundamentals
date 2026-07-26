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

def linha(tam=42):
        return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'{i+1} - {item}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc