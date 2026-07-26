from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():

    a1 = Aluno("João", 20, "Engenharia", "A")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Maria", 35, "Matemática", "Doutorado")
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Carlos", 40, "Analista", "TI")
    f1.fazer_aniversario()
    f1.bater_ponto()

if __name__ == "__main__":
    main()