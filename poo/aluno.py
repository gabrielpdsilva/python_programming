from pessoa import Pessoa
"""
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome, idade)

        self.nome = nome
        self.idade = idade
        self.matricula = matricula
"""
class Aluno(Pessoa):
    def __init__(self, nome):
        Pessoa.__init__(self, nome)

        self.nome = nome
