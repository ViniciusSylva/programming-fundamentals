from rpa import *

def main():
    b1 = BotEmail("Cotação de bitcoin")
    b1.iniciar()
    b1.executar_tarefa()
    b1.finalizar()

    b2 = BotWebScraping("Coleta de dados")
    b2.executar_tarefa()

if __name__ == "__main__":
    main()