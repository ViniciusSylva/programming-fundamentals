from termostatus import *


def main():
    t = Termostato()
    t.temperatura = 25

    print(f"A temperatura atual é de {t.ftemperatura}")


if __name__ == "__main__":
    main()
