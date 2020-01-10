#https://www.youtube.com/watch?v=RBYbuL-eFbQ&list=PLXik_5Br-zO_m8NaaEix1pyQOsCZM7t1h&index=17

from tkinter import *
import tkinter.messagebox

root_bhaskara = Tk()
root_bhaskara.title("Fórmula de Bháskara")

largura = 500
altura = 250

largura_tela = root_bhaskara.winfo_screenwidth()
altura_tela = root_bhaskara.winfo_screenheight()

posicao_x = (largura_tela / 2) - (largura / 2)
posicao_y = (altura_tela / 2 ) - (altura / 2)

root_bhaskara.geometry("%dx%d+%d+%d" % (largura, altura, posicao_x, posicao_y))

nenhum_erro = "EXCEPT STATUS: Nenhum erro até o momento."

#funcao pra apresentar info da formula de bhaskara
def apresentaInfoBhaskara():
    tkinter.messagebox.showinfo("Sobre a fórmula",
                                "A fórmula de Bhaskara é um método resolutivo para equações do segundo grau cujo nome homenageia o grande matemático indiano que a demonstrou. Essa fórmula nada mais é do que um método para encontrar as raízes reais de uma equação do segundo grau fazendo uso apenas de seus coeficientes. Vale lembrar que coeficiente é o número que multiplica uma incógnita em uma equação.")

#funcao pra encerrar a aplicacao
def encerrarAplicacao():
    encerrar =  tkinter.messagebox.askquestion ('Encerrar aplicação','Tem certeza de que deseja encerrar a aplicação?')
    if encerrar == 'yes':
        tkinter.messagebox.showinfo('Encerrando aplicação','Clique em \"OK\" para encerrar a aplicação.')
        root_bhaskara.destroy()

    #else:
        #tkinter.messagebox.showinfo('Return','You will now return to the application screen')

#config do menu
menu_tela_bhaskara = Menu(root_bhaskara)
menu_opcoes_bhaskara = Menu(menu_tela_bhaskara, tearoff = 0)
menu_opcoes_bhaskara.add_command(label = "Sobre a fórmula", command = apresentaInfoBhaskara)
menu_opcoes_bhaskara.add_separator()
menu_opcoes_bhaskara.add_command(label = "Menu principal")
menu_opcoes_bhaskara.add_command(label = "Encerrar aplicação", command = encerrarAplicacao)
menu_tela_bhaskara.add_cascade(label = "Opções", menu = menu_opcoes_bhaskara)
root_bhaskara.config(menu = menu_tela_bhaskara)

#funcao com a formula pra calcular bhaskara
def calcularBhaskara():
    try:

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
    #    txt_a.config(state = DISABLED)
        txt_a['state'] = DISABLED
    except Exception as erro:
        print("Ocorreu o seguinte erro: ", erro)
        label_erro['text'] = ("EXCEPT STATUS: %s" % erro)

def resetarCampos():
    label_delta_res['text'] = "-"
    label_x1_res['text'] = "-"
    label_x2_res['text'] = "-"
    var_a.set("")
    var_b.set("")
    var_c.set("")

    btn_calcular['state'] = NORMAL
    btn_reset['state'] = DISABLED
    label_info['text'] = "Digite os valores que deseja calcular..."
    #label_info.widget.grid_remove()

"""
label_titulo = Label(root_bhaskara,
                     text = "Software desenvolvido para calcular Bháskara.",
                     bg = "#363636",
                     fg = "#ffffff",
                     relief = "raised",
                     bd = 5,
                     font = "Arial 15 bold italic",
                     padx = 30,
                     ).grid(row = 0, column = 0)
"""

label_titulo = Label(root_bhaskara,
                     text = "Software desenvolvido para calcular Bháskara.",
                     bg = "#363636",
                     fg = "#ffffff",
                     #relief = "raised",
                     #bd = 5
                     ).grid(row = 0, column = 0)


#Label A
label_a = Label(root_bhaskara,
                text = "Valor de A:",
                bg = "#363636",
                fg = "#ffffff")
label_a.grid(row = 1, column = 0, sticky = W)

#Entry A
var_a = StringVar()
txt_a = Entry(root_bhaskara, textvariable = var_a).grid(row = 1, column = 0)


#Label B
label_b = Label(root_bhaskara,
                text = "Valor de B:",
                bg = "#363636",
                fg = "#ffffff")

label_b.grid(row = 2, sticky = W)

#Entry B
var_b = StringVar()
txt_b = Entry(root_bhaskara, textvariable = var_b).grid(row = 2, column = 0)



#Label C
label_c = Label(root_bhaskara,
                text = "Valor de C:",
                bg = "#363636",
                fg = "#ffffff")

label_c.grid(row = 3, sticky = W)

#Entry C
var_c = StringVar()
txt_c = Entry(root_bhaskara, textvariable = var_c).grid(row = 3, column = 0)


#Label de delta
label_delta = Label(root_bhaskara,
                text = "Valor de delta : ",
                bg = "#363636",
                fg = "#ffffff")

label_delta.grid(row = 1, column = 1)


#Label resposta de delta
label_delta_res = Label(root_bhaskara,
                text = "-",
                bg = "#363636",
                fg = "#ffffff")

label_delta_res.grid(row = 1, column = 2)



#Label de x1
label_x1 = Label(root_bhaskara,
                text = "Valor de X¹ : ",
                bg = "#363636",
                fg = "#ffffff")

label_x1.grid(row = 2, column = 1)



#Label resposta de x1
label_x1_res = Label(root_bhaskara,
                text = "-",
                bg = "#363636",
                fg = "#ffffff")

label_x1_res.grid(row = 2, column = 2)



#Label de x2
label_x2 = Label(root_bhaskara,
                text = "Valor de X² : ",
                bg = "#363636",
                fg = "#ffffff")

label_x2.grid(row = 3, column = 1)



#Label resposta de x2
label_x2_res = Label(root_bhaskara,
                text = "-",
                bg = "#363636",
                fg = "#ffffff")

label_x2_res.grid(row = 3, column = 2)


#root_bhaskara.geometry("500x250+500+500")
root_bhaskara.resizable(0, 0) #indica que tanto largura quanto altura nao poderam ser redimensionadas
#root_bhaskara.minsize(500, 250) #indica o minimo pra redimensionar a tela
#root_bhaskara.maxsize(1000, 500) #indica o maximo pra redimensionar a tela
#root_bhaskara.state("zoomed") #faz com que a tela seja automaticamente maximizada ao executar o programa

#botao calcular
#global btn_calcular
btn_calcular = Button(root_bhaskara, text = "Calcular", command = calcularBhaskara, state = NORMAL)
btn_calcular.grid(row = 4, column = 0)
#btn_calcular.pack()

root_bhaskara['bg'] = "#363636" #cor do background dessa tela

#botao reset
btn_reset = Button(root_bhaskara, text = "Resetar", command = resetarCampos, state = DISABLED)
btn_reset.grid(row = 4, column = 1)

#label fe informacoes
label_info = Label(root_bhaskara,
                    text = "Digite os valores que deseja calcular...",
                    fg = "red",
                    bg = "#363636",
                    font = "Arial 10 bold") #.grid(row = 5, column = center)

label_info.place(relx=0.5, rely=0.5, anchor=CENTER)

#label de erro
label_erro = Label(root_bhaskara,
                    text = nenhum_erro,
                    fg = "red",
                    bg = "#363636",
                    font = "Arial 10 bold")

label_erro.place(relx=0.5, rely=0.9, anchor = CENTER)

root_bhaskara.mainloop()
