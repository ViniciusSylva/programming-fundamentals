#declaracao de classe
class Gafanhoto:
    '''
        Classe que representa um gafanhoto, com atributos de nome e idade, e métodos para incrementar a idade e retornar uma mensagem sobre o gafanhoto.
    '''
    def __init__(self, nome = "", idade = 0): #metodo construtor
        #atributo de instance
        self.nome = nome
        self.idade = idade

    #metodos de instance 
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} e gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __str__(self):
        return f"{self.nome} e gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"estado: nome: {self.nome}, idade: {self.idade}"

#declaracao de objeto
g1 = Gafanhoto('Maria', 20)
#definiu o objeto "g1" como uma instancia da classe "Gafanhoto"

g1.aniversario() #chamando o metodo "aniversario" para incrementar a idade do objeto "g1"
print(g1) #chamando o metodo "mensagem" para retornar a mensagem sobre o objeto "g1"

print(g1.__dict__) # Sem "()", atributo
print(g1.__getstate__()) # Com "()", método

g2 = Gafanhoto('Ana', 15)
print(g2.mensagem())
print(g2.__class__)