from rich import print
from rich.panel import Panel

class ControleRemoto: 
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 0
    volume_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
            self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == self.canal_max:
                self.canal_atual = self.canal_min
            else:
                self.canal_atual += 1


    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1


    def volume_mais(self):  
        if self.ligado:
            if self.volume_atual < self.volume_max:
                self.volume_atual += 1  


    def volume_menos(self):
        if self.ligado:
            if self.volume_atual > self.volume_min:
                self.volume_atual -= 1


    def mostrar_tv(self):
        conteudo = ""
        if not self.ligado:
            conteudo = "A TV esta desligada"
        else:
            conteudo = f"Canal  = " 
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[green] {canal} [/]"
                else: 
                    conteudo += f" {canal} "


            conteudo += f"\nVolume = "
            for volume in range(self.volume_min, self.volume_max + 1):
                if volume == self.volume_atual:
                    conteudo += f"[green] {volume} [/]"
                else:
                    conteudo += f" {volume} "

        tv = Panel(conteudo, title="[ TV ]", subtitle="Controle Remoto", width=30, height=5, border_style="blue")
        print(tv)

c = ControleRemoto()
while True: 
    c.mostrar_tv()
    comando = str(input("\n  '@'     |ligar/desligar a TV\n  '0'     |encerrar o programa\n- VOL +   |aumentar/diminuir volume\n< CHH >   |passar/voltar canal\nDigite um comando:")).strip().upper()
    if comando == '0': 
        break
    elif "@" in comando:
        c.liga_desliga()
        print(f"TV {'ligada' if c.ligado else 'desligada'}")
    elif "<" in comando:
        if c.ligado:
            c.canal_menos()
        else:
            print("A TV esta desligada, ligue a TV para mudar de canal")
    elif ">" in comando:
        if c.ligado:
            c.canal_mais()
        else:
            print("A TV esta desligada, ligue a TV para mudar de canal")
    elif "-" in comando:
        if c.ligado:
            c.volume_menos()
        else:
            print("A TV esta desligada, ligue a TV para ajustar o volume")
    elif "+" in comando:
        if c.ligado:
            c.volume_mais()
        else:
            print("A TV esta desligada, ligue a TV para ajustar o volume")