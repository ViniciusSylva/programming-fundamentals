def msg(text1, text2, text3):
    print('-' * len(text3))
    print(text3)
    print('-' * len(text3))

    print('-' * len(text2))
    print(text2)
    print('-' * len(text2))

    print('-' * len(text1))
    print(text1)
    print('-' * len(text1))



texto1 = str(input('Digite a primeira mensagem: '))
texto2 = str(input('Digite a segunda mensagem: '))
texto3 = str(input('Digite a terceira mensagem: '))
msg(texto1, texto2, texto3)