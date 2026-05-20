from rich import inspect
from classes import Aluno, Professor, Funcionario

def main():
    aluno1 = Aluno("João", 20, "Engenharia", "A")
    professor1 = Professor("Dr. Silva", 45, "Matemática", "Doutor")
    funcionario1 = Funcionario("Maria", 30, "Secretária", "Administração")

    aluno1.fazer_matricula()
    professor1.dar_aula()
    funcionario1.bater_ponto()
    aluno1.estudar()
    professor1.estudar()
    funcionario1.estudar()

if __name__ == "__main__":
    main()