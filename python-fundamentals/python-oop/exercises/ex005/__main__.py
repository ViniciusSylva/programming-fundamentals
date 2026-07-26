from rich import inspect
from classesex005 import Aluno, Professor, Funcionario

a1 = Aluno("João", 20, "Engenharia", "A")
p1 = Professor("Maria", 35, "Matemática", "Doutorado")
f1 = Funcionario("Carlos", 40, "Analista", "TI")

inspect(a1, methods=True)
a1.fazer_aniversario()
inspect(a1)
inspect(p1)
p1.dar_aula()
inspect(p1)
inspect(f1)
f1.bater_ponto()