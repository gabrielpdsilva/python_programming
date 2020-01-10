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


change_colors(arquivo_aberto, FOREGROUND_VERDE)
"""
