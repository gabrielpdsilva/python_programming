from node import Node

class listaEncadeada:
    def __init__(self):
        self.head = None  #primeiro elemento da lista
        self.tamanho = 0

    def inserir(self, elemento): #insere no final da lista, como o método append padrão
        node = Node(elemento)

        if self.tamanho == 0:
            self.head = node

        else:
            ponteiro = self.head

            while(ponteiro.proximo is not None):    #enquanto o proximo dado do ponteiro nao for vazio
                ponteiro = ponteiro.proximo         #pula pro proximo ponteiro

            ponteiro.proximo = node                 #quando chegar no final, o ultimo elemento terá o valor de node
        self.tamanho += 1

    def remover(self):
        self.tamanho -= 1

    def get_tamanho(self):
        return str(self.tamanho)

    def set_item(self, index, elemento):

        #lista[2] = 5
        #lista.set_item(2, 5)

        ponteiro = self.head
        for i in range(index):
            if ponteiro is not None:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("Índice estourou o tamanho da lista.")

        if ponteiro is not None:    #se chegou até o ponteiro, e ele não é nulo
            ponteiro.dado = elemento 
        else:
            raise IndexError("Índice estourou o tamanho da lista.")

    def get_item(self, index):

        #var = lista[5]
        #var = lista.get_item(5)

        ponteiro = self.head
        for i in range(index):
            if ponteiro is not None:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("Índice estourou o tamanho da lista.")

        if ponteiro is not None:    #se chegou até o ponteiro, e ele não é nulo
            return ponteiro.dado
        else:
            raise IndexError("Índice estourou o tamanho da lista.")

#exemplo de uso
"""
lista = listaEncadeada()

lista.inserir(3)
lista.inserir(4)

print(lista.get_tamanho()) #2
print(lista.get_item(1)) #4

lista.set_item(0, True)

print(lista.get_item(0)) #True

lista.remover()

print(lista.get_tamanho()) #1

print(lista.set_item(6, 2)) # "Índice estourou o tamanho da lista."

input()
"""