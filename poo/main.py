from pessoa import Pessoa
from aluno import Aluno

#mensagens de sucesso/erro
arquivo_aberto = "===>>> O arquivo foi aberto com sucesso. <<<==="
mensagem_de_erro = "Ocorrereram um ou mais erros durante a execução => "

lista_de_pessoas = []

###############################################################
# LINK SOBRE MUDAR CORES DO TERMINAL DE UM PROGRAMA EM PYTHON #
###############################################################
#https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python?noredirect=1
"""
import ctypes

STD_OUTPUT_HANDLE = -11
FOREGROUND_VERMELHO    = 0x0004 # texto vermelho
FOREGROUND_AZUL_MARINHO    = 0x0003 # texto azul marinho
FOREGROUND_VERDE    = 0x0002 # texto verde
FOREGROUND_AZUL_ESCURO    = 0x0001 # texto azul escuro
FOREGROUND_ROXO    = 0x0005 # texto roxo
FOREGROUND_AMARELO    = 0x0006 # texto amarelo

def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr

def change_colors(text, color):
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    #print(text)
    #ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

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
        lista = open('pessoas.txt')

        #printa mensagem de sucesso em abrir o arquivo
        #change_colors(arquivo_aberto, FOREGROUND_VERDE)
        print(arquivo_aberto)

    except Exception as erro:
        #printa mensagem de erro com cor vermelha
        #change_colors((mensagem_de_erro, erro), FOREGROUND_VERMELHO)
        print(mensagem_de_erro, erro)

    for nome in lista:
        lista_de_pessoas.append(Aluno(nome))
        print("O seguinte objeto foi adicionado: ", nome.rstrip('\n'))

except Exception as erro:
    #change_colors((mensagem_de_erro, erro), FOREGROUND_VERMELHO)
    print(mensagem_de_erro, erro)

for pessoa in lista_de_pessoas:
    print("Lista de pessoas -> ", pessoa.nome.rstrip('\n'))        #rstrip('\n') serve pra pular apenas uma linha a cada print, e não duas

input("\nAperte ENTER pra sair")
