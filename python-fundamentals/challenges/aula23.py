try: 
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except (ZeroDivisionError, ValueError) as erro:
    print(f'Infelizmente tivemos um problema: {erro.__class__}')
except (KeyboardInterrupt, EOFError):
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'Infelizmente tivemos um problema: {erro.__class__}')
else: 
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')