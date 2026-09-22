from abc import ABC, abstractclassmethod

class Arquivo(ABC):
    def __init__(self, nome:str, ext:str, tam:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext

    @abstractclassmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise ValueError("O arquivo está em um formato não suportado!")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1_000_000}MB)"

class PDF(Arquivo):

    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'pdf', tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

        
class DOC(Arquivo):

    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'docx', tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")


def abrir_arquivo(arquivo):
    arquivo.abrir()