from diario import Diario

def main():
    meudiario = Diario()
    meudiario.escrever("Essa é a minha primeira vez escrevendo no diário")
    meudiario.escrever("Dia 27/07/2026")
    try:
        meudiario.ler("Teste")
    except Exception as e:
        (f"[red][ERROR]: {e}")

if __name__ == "__main__":
    main()