from node import Node

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    #inserir na pilha
    def inserir(self, elemento):
        node = Node(elemento)
        node.proximo = self.topo
        self.topo = node
        self.tamanho += 1

    #remover da pilha
    def remover(self):
        if self.topo is not None:
            node = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return node.dado
        raise IndexError("Erro ao remover: a pilha está vazia.")

    #ver o topo da pilha
    def get_topo(self):
        if self.tamanho > 0:
            return str(self.topo.dado)
        raise IndexError("Erro ao ver topo: a pilha está vazia.") 

    #ver tamanho da pilha
    def get_tamanho(self):
        return str(self.tamanho)

    def listar(self):
        ponteiro = self.topo
        while(ponteiro is not None):
            
            print(ponteiro.dado)
            ponteiro = ponteiro.proximo

#exemplo de uso:
"""
p = Pilha()
p.inserir(5)
p.inserir("...")
p.inserir(True)
p.inserir(2.2)
print("Listando pilha:")
p.listar() #lista todos os valores da pilha
p.remover() #remove o valor 2.2

print("\nTopo da pilha: " + p.verTopo()) #mostra o valor True
print("Tamanho da pilha: " + p.tamanhoPilha()) #mostra 3
input()

"""