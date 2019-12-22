#https://www.youtube.com/watch?v=RBYbuL-eFbQ&list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h&index=17

from tkinter import *

tela_inicial = Tk()
tela_inicial.title("Fórmula de Bháskara")

largura = 500
altura = 250

largura_tela = tela_inicial.winfo_screenwidth()
altura_tela = tela_inicial.winfo_screenheight()

posicao_x = (largura_tela / 2) - (largura / 2)
posicao_y = (altura_tela / 2 ) - (altura / 2)

tela_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posicao_x, posicao_y))

def calcular():

    if (not var_a.get()) or (not var_b.get()) or (not var_c.get()):     #se o campo A ou B ou C está vazio
        label_info['text'] = "É necessário preencher todos os campos para continuar!"
        return

    a = int(var_a.get())
    b = int(var_b.get())
    c = int(var_c.get())

    delta = (b * b) - (4 * a * c)

    if(delta < 0):
        label_delta_res['text'] = str(delta)
        label_info['text'] = "Delta < 0, não é possível definir as raízes."

    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)

        #print(btn_calcular.keys())
        label_delta_res['text'] = str(delta)
        label_x1_res['text'] = str(x1)
        label_x2_res['text'] = str(x2)

    label_info['text'] = "Cálculo realizado com sucesso.\nAperte o botão \"Resetar\" para iniciar outro cálculo."

    btn_calcular['state'] = DISABLED
    btn_reset['state'] = NORMAL

def reset():
    label_delta_res['text'] = "-"
    label_x1_res['text'] = "-"
    label_x2_res['text'] = "-"

    btn_calcular['state'] = NORMAL
    btn_reset['state'] = DISABLED
    #label_info.widget.grid_remove()



"""
label_titulo = Label(tela_inicial,
                     text = "Software desenvolvido para calcular Bháskara.",
                     bg = "#363636",
                     fg = "#ffffff",
                     relief = "raised",
                     bd = 5,
                     font = "Arial 15 bold italic",
                     padx = 30,
                     ).grid(row = 0, column = 0)
"""

label_titulo = Label(tela_inicial,
                     text = "Software desenvolvido para calcular Bháskara.",
                     bg = "#363636",
                     fg = "#ffffff",
                     #relief = "raised",
                     #bd = 5
                     ).grid(row = 0, column = 0)

#=============================================================================

label_a = Label(tela_inicial,
                text = "Valor de A:",
                bg = "#363636",
                fg = "#ffffff")
label_a.grid(row = 1, column = 0, sticky = W)

var_a = StringVar()
txt_a = Entry(tela_inicial, textvariable = var_a).grid(row = 1, column = 0)

#=============================================================================

label_delta = Label(tela_inicial,
                text = "Valor de delta : ",
                bg = "#363636",
                fg = "#ffffff")

label_delta.grid(row = 1, column = 1)

#=============================================================================

label_delta_res = Label(tela_inicial,
                text = "-",
                bg = "#363636",
                fg = "#ffffff")

label_delta_res.grid(row = 1, column = 2)

#=============================================================================

label_x1 = Label(tela_inicial,
                text = "Valor de X¹ : ",
                bg = "#363636",
                fg = "#ffffff")

label_x1.grid(row = 2, column = 1)

#=============================================================================

label_x1_res = Label(tela_inicial,
                text = "-",
                bg = "#363636",
                fg = "#ffffff")

label_x1_res.grid(row = 2, column = 2)

#=============================================================================

label_x2 = Label(tela_inicial,
                text = "Valor de X² : ",
                bg = "#363636",
                fg = "#ffffff")

label_x2.grid(row = 3, column = 1)

#=============================================================================

label_x2_res = Label(tela_inicial,
                text = "-",
                bg = "#363636",
                fg = "#ffffff")

label_x2_res.grid(row = 3, column = 2)

#=============================================================================

label_b = Label(tela_inicial,
                text = "Valor de B:",
                bg = "#363636",
                fg = "#ffffff")

label_b.grid(row = 2, sticky = W)

var_b = StringVar()
txt_b = Entry(tela_inicial, textvariable = var_b).grid(row = 2, column = 0)

#=============================================================================

label_c = Label(tela_inicial,
                text = "Valor de C:",
                bg = "#363636",
                fg = "#ffffff")

label_c.grid(row = 3, sticky = W)

var_c = StringVar()
txt_c = Entry(tela_inicial, textvariable = var_c).grid(row = 3, column = 0)

#=============================================================================

#tela_inicial.geometry("500x250+500+500")

tela_inicial.resizable(0, 0) #indica que tanto largura quanto altura nao poderam ser redimensionadas
#tela_inicial.minsize(500, 250) #indica o minimo pra redimensionar a tela
#tela_inicial.maxsize(1000, 500) #indica o maximo pra redimensionar a tela
#tela_inicial.state("zoomed") #faz com que a tela seja automaticamente maximizada ao executar o programa

#=============================================================================
btn_calcular = Button(tela_inicial, text = "Calcular", command = calcular, state = NORMAL)
btn_calcular.grid(row = 4, column = 0)

tela_inicial['bg'] = "#363636"

#=============================================================================
btn_reset = Button(tela_inicial, text = "Resetar", command = reset, state = DISABLED)
btn_reset.grid(row = 4, column = 1)
#=============================================================================
label_info = Label(tela_inicial, text = "Digite os valores que deseja calcular...", fg = "red", bg = "#363636", font = "Arial 10 bold") #.grid(row = 5, column = center)
label_info.place(relx=0.5, rely=0.5, anchor=CENTER)
tela_inicial.mainloop()
