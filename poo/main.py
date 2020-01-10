from pessoa import Pessoa
from aluno import Aluno

print("""
=======================================
====CRIANDO OBJETOS AUTOMATICAMENTE====
=======================================
""")

#mensagens de sucesso/erro
arquivo_aberto = "===>>> Os arquivos foram abertos com sucesso. <<<===\n"
mensagem_de_erro = "Ocorrereram um ou mais erros durante a execução => "

lista_de_alunos = []

"""
#funcao pra abrir o arquivo
def abrir_arquivo():
    try:
        lista = open('pessoas.txt')
        print("O arquivo foi aberto com sucesso.")
        return lista
    except Exception as erro:
        print("Ocorreu o seguinte erro: ", erro)
"""

try:

    try:
        #abrindo arquivos
        lista_de_nomes = open('pessoas.txt')
        lista_de_idades = open('idades.txt')
        print(arquivo_aberto)

    except Exception as erro:
        print(mensagem_de_erro, erro)

    for (nome, idade) in zip(lista_de_nomes, lista_de_idades):
        #criando e adicionando os objetos na lista de alunos
        lista_de_alunos.append(Aluno(nome, idade))

except Exception as erro:
    #change_colors((mensagem_de_erro, erro), FOREGROUND_VERMELHO)
    print(mensagem_de_erro, erro)

if not lista_de_alunos:
    print("Nenhum objeto do tipo Aluno foi criado/inserido na lista.")
else:
    print("LISTA COMPLETA DE ALUNOS ATÉ O MOMENTO:\n")
    for aluno in lista_de_alunos:
        aluno.infoAluno()

input("\nAperte ENTER para sair")
