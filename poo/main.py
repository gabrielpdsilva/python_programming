from pessoa import Pessoa
from aluno import Aluno

#nome = input("Digite o nome da pessoa: ")
#idade = int(input("Digite a idade da pessoa: "))
#matricula = input("Digite a matricula da pessoa: ")
#pessoa1 = Aluno(nome, idade, matricula)

#for nome in lista:

#    pessoa = Aluno(nome)
#    print("Pessoa criada: " + pessoa.nome)

lista_de_pessoas = []

def abrir_arquivo():
    try:
        lista = open('pessoas.txt')
        print("O arquivo foi encontrado com sucesso.")
        return lista
    except Exception as erro:
        print("Ocorreu o seguinte erro: ", erro)

for nome in abrir_arquivo(): #necessario corrigir, pois se tiver um except no abrir_arquivo(), vai dar pau no loop
    try:
        lista_de_pessoas.append(Aluno(nome))
        print("O seguinte objeto foi adicionado: ", nome.rstrip('\n'))
    except Exception as erro:
        print("Houve o seguinte erro enquanto inseria objetos: ", erro)
        break

for pessoa in lista_de_pessoas:
    print("Lista de pessoas -> ", pessoa.nome.rstrip('\n'))        #rstrip('\n') serve pra pular apenas uma linha a cada print, e não duas

#===========

input("\nAperte ENTER pra sair")
