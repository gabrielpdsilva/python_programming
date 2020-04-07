#video: https://www.youtube.com/watch?v=6E169kShoNU

from node import Node

class Arvore:
    def __init__(self, dado = None):
        if dado:                       #se o dado não for None
            node = Node(dado)
            self.raiz = node
        else:
            self.raiz = None

    def percurso_simetrico(self, node = None):
        if node is None:
            node = self.raiz
        
        if node.esquerda:
            print('(', end='')                  #end = '' serve pra não quebrar linha ao finalizar o print
            self.percurso_simetrico(node.esquerda)
        print(node.dado, end = '')

        if node.direita:
            self.percurso_simetrico(node.direita)
            print(')', end='')

#============================================
#modelo 1:

#     '1'
#    /   \
#   '5'  '2'

"""
arvore = Arvore(1)
arvore.raiz.esquerda = Node(5)
arvore.raiz.direita = Node(2)

print(arvore.raiz.dado)
print(arvore.raiz.esquerda.dado)
print(arvore.raiz.direita.dado)
input()
"""

#============================================
#modelo 2:

#     '+'
#    /   \
#  'a'   '*'
#        /  \
#      'b'   '-'
#            /  \
#          '/'  'e'
#         /  \
#       'c'  'd'

# (a+(b*((c/d)-e)))

"""
arvore = Arvore()
n1 = Node('a')
n2 = Node('+')
n3 = Node('*')
n4 = Node('b')
n5 = Node('-')
n6 = Node('/')
n7 = Node('c')
n8 = Node('d')
n9 = Node('e')

n6.esquerda = n7
n6.direita = n8
n5.esquerda = n6
n5.direita = n9
n3.esquerda = n4
n3.direita = n5
n2.esquerda = n1
n2.direita = n3
arvore.raiz = n2

arvore.percurso_simetrico()
input()
"""