class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        #self.idade = idade

    def info(self):
        print("\nDados de usuário:")
        print("Nome: "+ self.nome)
        #print("Idade: " + str(self.idade))
