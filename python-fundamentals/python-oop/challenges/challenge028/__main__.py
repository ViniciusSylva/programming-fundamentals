from system_users import *

def main():
    u1 = Admin("Vinicius", "Vinydev@gmail.com")
    print(u1.validar_senha("senhacorreta"))

    u2 = Cliente("Vinizada", "Flaviodopneu@gmail.com")
    print(u2.validar_senha("senhaincorreta"))

    print(u1)
    print(u2)

if __name__ == "__main__":
    main()