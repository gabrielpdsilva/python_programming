from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade):
        Pessoa.__init__(self, nome, idade)
