from exercises.ex012.classes import Cachorro, Gato, Pato, Galinha, Spitz, PitBull

def main():
    a = Cachorro("Bandit")
    b = Gato("Frajola")
    c = Pato("Donald")
    d = Galinha("Pintada")
    e = Spitz("Luluzinha")
    f = PitBull("Guereiro")
    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()
    e.emitir_som()
    f.emitir_som()


if __name__ == "__main__":
    main()