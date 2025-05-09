from pacotes import*
from views import*



ml_rota = Tk()
ml_rota.title("Controle de Rotas e Ganhos")
ml_rota.geometry("900x600")
ml_rota.configure(background=co0)
ml_rota.resizable(width=False, height=False)
largura_root= 900
altura_root= 600
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

frame_baixo = Frame(ml_rota, width=900, height=200, bg=co1, relief='flat')
frame_baixo.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(ml_rota, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

frame_tabela = Frame(ml_rota, width=900, height=300, bg=co1, relief='flat')
frame_tabela.grid(row=6, column=0, padx=0, pady=0, sticky=NSEW)
#################---------TITULO------##################################################################################
l_titulo=Label(frame_cima, text="Rota do Mercado Livre",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------CONFIGURAÇÕES BOTÕES------##################################################################################
def abrir_painel():
    painel = "main.py"  # nome do script a ser aberto
    subprocess.Popen([sys.executable, painel])
    ml_rota.destroy()  # fecha a janela atual

################---------CONFIGURAÇÃO DE DADOS------##################################################################################


def calcular_media_combustivel():
    try:
        valor_rota = float(e_valor_rota.get())
        km = float(e_km.get())
        valor_bomba = float(e_v_comb.get())
        entregue = int(e_entregas.get())
        devolvidas = int(e_dev.get())

        # Calcula total de entregas realizadas
        total_entregas = entregue - devolvidas
        e_Total_entregas.delete(0, END)
        e_Total_entregas.insert(0, str(total_entregas))

        # Calcula o gasto com combustível (média de 10 km por litro)
        gasto_combustivel = (km / 10) * valor_bomba

        # Calcula o lucro: valor da rota - gasto com combustível
        lucro = valor_rota - gasto_combustivel

        # Mostra o lucro no campo de lucro
        e_lucro.delete(0, END)
        e_lucro.insert(0, f"{lucro:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def cadastrar_dados():
    data = entry_data.get()
    dia_semana = e_d_semana.get()
    valor_rota = e_valor_rota.get()
    km = e_km.get()
    valor_bomba = e_v_comb.get()
    lucro = e_lucro.get()
    entregas = e_entregas.get()
    devolvidas = e_dev.get()
    total = e_Total_entregas.get()

    lista = [data,dia_semana, valor_rota, km, valor_bomba, lucro, entregas, devolvidas, total]

    # Verifica se algum campo está vazio
    for i in lista:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

    # Inserindo no banco de dados
    criar_dados_ml(lista)

    messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

    # Limpa os campos após o cadastro
    entry_data.delete(0, END)
    e_d_semana.delete(0, END)
    e_valor_rota.delete(0, END)
    e_km.delete(0, END)
    e_v_comb.delete(0, END)           # <<< adicionado
    e_lucro.delete(0, END)
    e_entregas.delete(0, END)
    e_dev.delete(0, END)
    e_Total_entregas.delete(0, END)


#################---------BOTÕES------##################################################################################
bt_adicionar = Button(frame_botao, command=cadastrar_dados, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_adicionar.grid(row=0, column=1)

bt_excluir = Button(frame_botao, command=None, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_excluir.grid(row=0, column=2)

bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_imprimir.grid(row=0, column=3)

bt_calc = Button(frame_botao, command=calcular_media_combustivel, text="Calcular", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_calc.grid(row=0, column=4)

bt_rela = Button(frame_botao, command=None, text="Relatório", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_rela.grid(row=0, column=5)

bt_atualizar = Button(frame_botao, command=None, text="Atualizar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_atualizar.grid(row=0, column=6)

bt_voltar = Button(frame_botao, command=abrir_painel, text="Painel", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_voltar.grid(row=0, column=7)
#################---------CONFIGURAÇÕES------##################################################################################
def calendario():
    def pegar_data():
        data_selecionada = cal.selection_get()
        entry_data.delete(0, END)
        entry_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))
        
        # Mostrar automaticamente o dia da semana:
        dia_semana = data_selecionada.strftime("%A")  # Dia da semana em inglês
        dias_traduzidos = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        dia_semana_pt = dias_traduzidos[dia_semana]
        
        e_d_semana.delete(0, END)
        e_d_semana.insert(0, dia_semana_pt)

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

    Button(calendario_root, text="Selecionar", command=pegar_data).pack(pady=10)

#################--------LABEL------##################################################################################
bt_calendario = Button(frame_baixo, text="Data", command=calendario)
bt_calendario.place(x=10, y=10)
entry_data = Entry(frame_baixo, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
entry_data.place(x=70, y=10) 

l_d_semana = Label(frame_baixo, text="Dia da Semana:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_d_semana.place(x=190, y=10)
e_d_semana = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_d_semana.place(x=305, y=10)

l_v_comb = Label(frame_baixo, text="Valor da Bomba R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_v_comb.place(x=390, y=10)
e_v_comb = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_v_comb.place(x=520, y=10)

l_valor_rota = Label(frame_baixo, text="Valor Rota:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_valor_rota.place(x=10, y=40)
e_valor_rota= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_valor_rota.place(x=90, y=40)

l_km = Label(frame_baixo, text="KM:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_km.place(x=10, y=70)
e_km= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_km.place(x=90, y=70)

l_lucro = Label(frame_baixo, text="Lucro R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_lucro.place(x=10, y=100)
e_lucro = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_lucro.place(x=90, y=100)

l_entregas = Label(frame_baixo, text="Entregas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_entregas.place(x=170, y=40)
e_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_entregas.place(x=240, y=40)

l_dev = Label(frame_baixo, text="Devolvidas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_dev.place(x=170, y=70)
e_dev = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_dev.place(x=250, y=70)

l_Total_entregas = Label(frame_baixo, text="Total:", font=('Ivy 10 bold'), bg=co1, fg=co6)
l_Total_entregas.place(x=190, y=100)
e_Total_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
e_Total_entregas.place(x=260, y=100)



#Tabela Alunos
#Tabela Alunos
def mostrar_dados():
    app_nome = Label(frame_tabela, text="Tabela de Estudantes", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co6)
    app_nome.grid(row=0 , column=0, padx=0, pady=10, sticky=NSEW)
        
    #CREATING A TREEVIEW WITH DUAL SCROLLBARS
    list_header = ['data', 'dia_semana', 'valor_rota', 'km', 'valor_bomba', 'lucro', 'entregas', 'devolvidas', 'total']
    df_list = ver_dados()

    global tree_ml
        
    tree_ml = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
        
    #VERTICAL SCROLLBAR
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_ml.yview)
    #HORIZONTAL SCROLLBAR
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_ml.xview)

    tree_ml.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_ml.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0,weight=12)

    hd=['center','center','center','center','center','center','center','center','center']
    h = [40,150,150,70,70,70,80,100,150]
    n=0
        
    for col in list_header:
        tree_ml.heading(col, text=col.title(), anchor=NW)
        #ADJUST THE COLUMN'S WIDTH TO THE HEADER STRING
        tree_ml.column(col, width=h[n], anchor=hd[n])
        n+=1
        for item in df_list:
            tree_ml.insert("", "end", values=item)
mostrar_dados()



ml_rota.mainloop()