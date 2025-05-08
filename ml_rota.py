from pacotes import*


mlrota = Tk()
mlrota.title("Controle de Rotas e Ganhos")
mlrota.geometry("900x400")
mlrota.configure(background=co0)
mlrota.resizable(width=False, height=False)
largura_root= 900
altura_root= 400
#obter tamanho da tela
largura_tela = mlrota.winfo_screenwidth()
altura_tela = mlrota.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
mlrota.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

###############---------FRAME------##################################################################################
frame_cima = Frame(mlrota, width=900, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(mlrota, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_botao = Frame(mlrota, width=900, height=50, bg=co1, relief='flat')
frame_botao.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(mlrota, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_baixo = Frame(mlrota, width=900, height=350, bg=co1, relief='flat')
frame_baixo.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)


#################---------TITULO------##################################################################################
l_titulo=Label(frame_cima, text="Rota do Mercado Livre",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------BOTÕES------##################################################################################
bt_adcionar = Button(frame_botao, command=None, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_adcionar.place(x=5, y=5)

bt_excluir = Button(frame_botao, command=None, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_excluir.place(x=95, y=5)

bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_imprimir.place(x=165, y=5)
#################---------CONFIGURAÇÕES------##################################################################################
def calendario():
    def pegar_data():
        data_selecionada = cal.selection_get()
        entry_data.delete(0, END)
        entry_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))
        calendario_root.destroy()

    calendario_root = Toplevel()
    calendario_root.title("Selecionar Data")
    calendario_root.resizable(width=False, height=False)

    largura_root = 200
    altura_root = 270
    largura_tela = calendario_root.winfo_screenwidth()
    altura_tela = calendario_root.winfo_screenheight()
    pos_x = (largura_tela - largura_root) // 2
    pos_y = (altura_tela - altura_root) // 2
    calendario_root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

    cal = Calendar(calendario_root, selectmode="day", date_pattern="dd/mm/yyyy")
    cal.pack(pady=20)

    Button(calendario_root, text="Selecionar", command=pegar_data).pack(pady=10) # Botão para selecionar a data



#################--------LABEL------##################################################################################
bt_calendario = Button(frame_baixo, text="Data", command=calendario)
bt_calendario.place(x=10, y=10)
entry_data = Entry(frame_baixo, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
entry_data.place(x=70, y=10) 









mlrota.mainloop()