def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return fat

n = int(input('Digite um número para calcular seu fatorial: '))
print(fatorial(n, show=False))