from rich import inspect

class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez matrícula no curso de {self.curso} na turma {self.turma}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade} com nível {self.nivel}.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu ponto no setor de {self.setor} como {self.cargo}.")

a1 = Aluno("João", 20, "Engenharia", "A")
p1 = Professor("Maria", 35, "Matemática", "Doutorado")
f1 = Funcionario("Carlos", 40, "Analista", "TI")

inspect(a1, methods=True)
a1.fazer_aniversario()
inspect(a1)
inspect(p1)
inspect(f1)