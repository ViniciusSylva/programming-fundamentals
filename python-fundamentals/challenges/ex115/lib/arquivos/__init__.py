def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+') #wt+ = write text + (cria o arquivo se ele não existir)
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!') 

def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';') #separar os dados por ';'
            dado[1] = dado[1].replace('\n', '') #remover o '\n' do final do nome
            print(f'{dado[0]:<30}{dado[1]:>3} anos') #formatar a saída
    finally:
        a.close()

def cadastrar(arquivo, nome='desconecido', idade=0):
    try:
        a = open(arquivo, 'at') #at = append text (adiciona ao final do arquivo)
    except:
        print('Houve um erro ao cadastrar a pessoa!')
    else:
        try:
            a.write(f'{nome};{idade}\n') #escrever os dados no arquivo
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()