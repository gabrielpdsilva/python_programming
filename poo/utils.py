###############################################################
# LINK SOBRE MUDAR CORES DO TERMINAL DE UM PROGRAMA EM PYTHON #
###############################################################
#https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python?noredirect=1

import ctypes

# Constants from the Windows API
STD_OUTPUT_HANDLE = -11
FOREGROUND_VERMELHO    = 0x0004 # text color contains red.
FOREGROUND_AZUL_MARINHO    = 0x0003 # text color contains blue,
FOREGROUND_VERDE    = 0x0002 # text color contains green,
FOREGROUND_AZUL_ESCURO    = 0x0001 # text color contains dark blue,
FOREGROUND_ROXO    = 0x0005 # text color contains roxo,
FOREGROUND_AMARELO    = 0x0006 # text color contains yellow,

def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_ROXO)
print("Cherry on top")
ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_AMARELO)
print("Cherry on top")
ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
