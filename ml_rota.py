from pacotes import*


ml_rota = Tk()
ml_rota.title("Controle de Rotas e Ganhos")
ml_rota.geometry("900x400")
ml_rota.configure(background=co0)
ml_rota.resizable(width=False, height=False)
largura_root= 900
altura_root= 400
#obter tamanho da tela
largura_tela = ml_rota.winfo_screenwidth()
altura_tela = ml_rota.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
ml_rota.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

###############---------FRAME------##################################################################################
frame_cima = Frame(ml_rota, width=900, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(ml_rota, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_botao = Frame(ml_rota, width=900, height=50, bg=co1, relief='flat')
frame_botao.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(ml_rota, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_baixo = Frame(ml_rota, width=900, height=350, bg=co1, relief='flat')
frame_baixo.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(ml_rota, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

frame_tabela = Frame(ml_rota, width=900, height=350, bg=co1, relief='flat')
frame_tabela.grid(row=6, column=0, padx=0, pady=0, sticky=NSEW)
#################---------TITULO------##################################################################################
l_titulo=Label(frame_cima, text="Rota do Mercado Livre",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------CONFIGURAÇÕES BOTÕES------##################################################################################
def abrir_painel():
    painel = "main.py"  # nome do script a ser aberto
    subprocess.Popen([sys.executable, painel])
    ml_rota.destroy()  # fecha a janela atual

#################---------BOTÕES------##################################################################################
bt_adcionar = Button(frame_botao, command=None, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_adcionar.grid(row=0, column=1)

bt_excluir = Button(frame_botao, command=None, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_excluir.grid(row=0, column=2)

bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_imprimir.grid(row=0, column=3)

bt_calc = Button(frame_botao, command=None, text="Calcular", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_calc.grid(row=0, column=4)

bt_atualizar = Button(frame_botao, command=None, text="Atualizar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_atualizar.grid(row=0, column=5)

bt_voltar = Button(frame_botao, command=abrir_painel, text="Painel", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_voltar.grid(row=0, column=6)
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

l_valor = Label(frame_baixo, text="Valor Rota:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_valor.place(x=10, y=40)
e_valor= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_valor.place(x=90, y=40)

l_comb_gasto = Label(frame_baixo, text="Comb. Gasto R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_comb_gasto.place(x=10, y=70)
e_comb_gasto = Label(frame_baixo, text="0", font=('Ivy 10 bold'), bg=co1, fg=co6)
e_comb_gasto.place(x=130, y=70)

l_lucro = Label(frame_baixo, text="Lucro R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_lucro.place(x=10, y=100)
e_lucro = Label(frame_baixo, text="0", font=('Ivy 10 bold'), bg=co1, fg=co6)
e_lucro.place(x=130, y=100)

l_entregas = Label(frame_baixo, text="Entregas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_entregas.place(x=170, y=40)
e_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_entregas.place(x=240, y=40)

l_entregas = Label(frame_baixo, text="Entregas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_entregas.place(x=170, y=70)
e_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_entregas.place(x=240, y=70)

l_lucro = Label(frame_baixo, text="Lucro %:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_lucro.place(x=170, y=100)
e_lucro = Label(frame_baixo, text="0", font=('Ivy 10 bold'), bg=co1, fg=co6)
e_lucro.place(x=240, y=100)







ml_rota.mainloop()