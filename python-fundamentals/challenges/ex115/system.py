from lib.interface import *
from lib.arquivos import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
        resposta = menu(['Listar pessoas', 'Cadastrar pessoa', 'Sair do sistema'])
        if resposta == 1:
            lerArquivo(arq)
        elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = input('Nome: ')
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        elif resposta == 3:
            print('Saindo do sistema... Até logo!')
            break
        else:
            print('\033[0;31mERRO: Digite uma opção válida.\033[m')
        sleep(2)