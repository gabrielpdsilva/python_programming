from node import Node 

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def inserir(self, elemento):
        node = Node(elemento)

        if self.primeiro is None:
            self.primeiro = node

        if self.ultimo is None:
            self.ultimo = node
        else:
            self.ultimo.proximo = node 
            self.ultimo = node

        self.tamanho += 1

    def remover(self):

        if self.tamanho > 0:
            elemento = self.primeiro.dado
            self.primeiro = self.primeiro.proximo
            print("Elemento removido: " + str(elemento))
            self.tamanho -=1
        else:
            print("A fila está vazia.")

    def gettamanho(self):
        return print("Tamanho da fila: " + str(self.tamanho))

    def getprimeiro(self):
        if self.tamanho > 0:
            elemento = self.primeiro.dado
            print("Primeiro da fila: " + str(elemento))
        else:
            print("A fila está vazia.")

    def listar(self):
        if self.tamanho > 0:
            ponteiro = self.primeiro
            while(ponteiro is not None):
                print(ponteiro.dado)
                ponteiro = ponteiro.proximo
        else:
            print("A fila está vazia")

#exemplo de uso:
"""
f = Fila()
f.inserir(True)
f.inserir(5)
f.inserir("123")
f.listar()
f.gettamanho()  # 3
f.getprimeiro() # True
input()
"""