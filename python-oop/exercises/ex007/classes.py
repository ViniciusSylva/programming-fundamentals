from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} fez matrícula no curso de {self.curso} na turma {self.turma}.")

    def estudar(self):
        print(f"{self.nome} está estudando para as provas do curso de {self.curso}.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade} com nível {self.nivel}.")

    def estudar(self):
        print(f"{self.nome} está estudando novas metodologias de ensino para a disciplina de {self.especialidade}.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu ponto no setor de {self.setor} como {self.cargo}.")

    def estudar(self):
        print(f"{self.nome} está estudando para melhorar suas habilidades no setor de {self.setor}.")