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
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)

        #self.nome = nome

    def infoAluno(self):
            
            print("Nome: ", self.nome.rstrip('\n'))     #rstrip('\n') serve pra pular apenas uma linha a cada print, e não duas
            print("Idade: ", self.idade)
