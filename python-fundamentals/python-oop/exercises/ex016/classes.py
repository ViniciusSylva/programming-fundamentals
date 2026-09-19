
class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e puxar/empurrar a maçaneta")


class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")


class Ovo:
    def abrir(self):
        print(f"Quebre a casca com um garfo e separe as partes sobre uma frigideira")


class Pedra:
    pass


# METODO PYTHONICO POLIMORFICO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei poblemas ao tentar abrir um objeto do tipo {objeto.__class__.__name__}")

