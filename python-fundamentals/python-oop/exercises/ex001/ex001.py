#declaracao de classe
class Gafanhoto:
    def __init__(self): #metodo construtor
        #atributo de instance
        self.nome = ""
        self.idade = 0

    #metodos de instance 
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} e gafanhoto(a) e tem {self.idade} anos de idade."


#declaracao de objeto
g1 = Gafanhoto()
#definiu o objeto "g1" como uma instancia da classe "Gafanhoto"

g1.nome = "Maria"
g1.idade = 20   
g1.aniversario() #chamando o metodo "aniversario" para incrementar a idade do objeto "g1"
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Ana"
g2.idade = 15
print(g2.mensagem())