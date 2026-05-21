from personagens import *

def main():
    p1 = Guerreiro("Rimuru", 10000)
    p2 = Mago("Shuna", 5000)

    p1.atacar(p2, 500)
    p2.curar(200)

    p2.atacar(p1, 5000)
    p1.curar(1000)

if __name__ == "__main__":
    main()