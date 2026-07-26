class gamer: 
    def __init__(self, nome, nick):
        self.name = nome
        self.nick = nick
        self.favoritos = list()

    def add_jogo(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        return f"Nick: {self.nick}\nNome: {self.name}\nJogos Favoritos: {', '.join(self.favoritos)}"
    
    
j1 = gamer("Joao", "joaogamer")
j1.add_jogo("GTA V")
j1.add_jogo("Minecraft")
print(j1.ficha())

j2 = gamer("Maria", "mariagamer")
j2.add_jogo("Valorant")
print(j2.ficha())