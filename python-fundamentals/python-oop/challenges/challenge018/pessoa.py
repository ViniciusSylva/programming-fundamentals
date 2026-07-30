from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None
        self._nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar idade. Mude o ano de nascimento")


class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "INF", "ENG"]
    def __init__(self):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = self.curso

    @property
    def curso(self):
        return self._curso


    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não está na lista de cursos práticos!")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()

        if 3 <= len(curso) <= 5:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"Curso {curso} está fora do padrão de cursos")        