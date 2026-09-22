from classes import *
from rich import print, inspect

def main():
    a1 = DOC("teste", 120000)
    a2 = PDF("contrato", 85000)
    inspect(a1, methods=True)
    abrir_arquivo(a1)
    abrir_arquivo(a2)

if __name__ == "__main__":
    main()