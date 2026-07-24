class Bot():  
    def __init__(self, nome, status = "Parado"):
        self.nome = nome 
        self.status = status 

    def iniciar(self):
        self.status = "Rodando"

    def executar_tarefa(self):
        print("Executando tarefa...")
    
    def finalizar(self):
        self.status = "Finalizado"


class BotEmail(Bot):
    def __init__(self, nome):
        super().__init__(nome)

    def executar_tarefa(self):
        if self.status != "Rodando":
            print(f"O RPA não está em estado de execução, inicie ele primeiro!")
            return
        else: 
            print(f"Bot {self.nome} enviou e-mail automatizado com sucesso!")

    def finalizar(self):
        if self.status != "Rodando":
            print(f"O macro não está rodando para ser executado!")
            return
        else: 
            print(f"RPA de envio de e-mail foi finalizado!")


class BotWebScraping(Bot):  
    def __init__(self, nome):
        super().__init__(nome)

    def executar_tarefa(self):
        if self.status != "Rodando":
            print(f"O Script não está em estado de execução, inicie ele primeiro!")
            return
        else: 
            print(f"Script {self.nome} coletou todos os dados com sucesso!")

    def finalizar(self):
        if self.status != "Rodando":
            print(f"O Script não está rodando para ser executado!")
            return
        else: 
            print(f"O Script foi finalizado com sucesso!")

