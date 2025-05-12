from pacotes import*
import sys, os
import tkinter as tk

root = Tk()
root.title("Controle de Rotas e Ganhos")
root.geometry("600x400")
root.configure(background=co0)
root.resizable(width=False, height=False)
largura_root= 600
altura_root= 400
#obter tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

###############---------FRAME------##################################################################################
frame_cima = Frame(root, width=600, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

frame_baixo = Frame(root, width=600, height=350, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)



################---------CONFIGURAÇÃO------##################################################################################



#################---------TITULO------##################################################################################
l_titulo= Label(frame_cima, text="Controle de Rotas e Ganhos", anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------BOTÕES------##################################################################################
bt_ml = Button(frame_baixo, command=lambda: ml_rota(), text="Mercado Livre", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_ml.place(x=20, y=30)

bt_sp = Button(frame_baixo, command=None, text="Shopee", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_sp.place(x=140, y=30)

bt_colagem = Button(frame_baixo, command=None, text="Colagem", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_colagem.place(x=230, y=30)

bt_abast = Button(frame_baixo, command=None, text="Abastecimento", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_abast.place(x=20, y=70)

bt_lucroanual = Button(frame_baixo, command=None, text="Lucro Anual", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_lucroanual.place(x=140, y=70)

bt_lucpormes = Button(frame_baixo, command=None, text="Lucro por Mês", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_lucpormes.place(x=20, y=110)

bt_contas = Button(frame_baixo, command=None, text="Contas", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_contas.place(x=240, y=70)

bt_contaml = Button(frame_baixo, command=None, text="Conta Mercado Livre", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_contaml.place(x=310, y=30)

############################################################################################################################################
###################################### ROTA MERCADO LIVRE ##################################################################################
#############################################################################################################################################
def ml_rota():

    ml_rota = tk.Toplevel(root)
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

    frame_tabela = Frame(ml_rota, width=900, height=300, bg=co6, relief='flat')
    frame_tabela.grid(row=6, column=0, padx=0, pady=0, sticky=NSEW)
    #################---------TITULO------##################################################################################
    l_titulo=Label(frame_cima, text="Rota do Mercado Livre",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
    l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

    ##############################################################################################################################


    #################---------CONFIGURAÇÕES BOTÕES------##################################################################################
    def abrir_painel():
       painel = "controle_de_rota.py"  # nome do script a ser aberto
       subprocess.Popen([sys.executable, painel])
       ml_rota.destroy()  # fecha a janela atual # fecha a janela atual

    ################---------CONFIGURAÇÃO DE DADOS------##################################################################################
    v_mes_var = tk.StringVar()

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
        valor_rota = float(e_valor_rota.get())
        km = float(e_km.get())
        valor_bomba = float(e_v_comb.get())
        lucro = float(e_lucro.get())
        entregas = int(e_entregas.get())
        devolvidas = int(e_dev.get())
        total = float(e_Total_entregas.get())

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

    def calcular_total_valor_rota():
        try:
            with con:
                cur = con.cursor()
                cur.execute('SELECT SUM(valor_rota) FROM Rota_Mercado_Livre')
                resultado = cur.fetchone()[0]
                return resultado if resultado is not None else 0
        except Exception as e:
            print(f"Erro ao calcular total de valor_rota: {e}")
            return 0

    def atualizar_entry_valor_rota():
        total = calcular_total_valor_rota()
        v_mes_var.set(f"R$ {total:.2f}")

    def update_dados():
    
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Limpando campos
            for campo in [entry_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                campo.delete(0, END)

            # Preenchendo os campos com os valores selecionados
            entry_data.insert(0, tree_lista[1])
            e_d_semana.insert(0, tree_lista[2])
            e_valor_rota.insert(0, tree_lista[3])
            e_km.insert(0, tree_lista[4])
            e_v_comb.insert(0, tree_lista[5])
            e_lucro.insert(0, tree_lista[6])
            e_entregas.insert(0, tree_lista[7])
            e_dev.insert(0, tree_lista[8])
            e_Total_entregas.insert(0, tree_lista[9])

        

            # Tentando carregar a imagem
            def update():
                # Pegando os dados atualizados
                entry_data = entry_data.get()
                e_d_semana = e_d_semana.get()
                e_valor_rota = e_valor_rota.get()
                e_km = e_km.get()
                e_v_comb = e_v_comb.get()
                e_lucro = e_lucro.get()
                e_entregas = e_entregas.get()
                e_dev = e_dev.get()
                e_Total_entregas = e_Total_entregas.get()
            
            
                lista = [entry_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas, valor_id]

                # Verificação de campos vazios
                if not all(lista[:-1]):  # Exclui o ID da verificação
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return

                try:
                    atualizar_dados_ml(lista)  # Ensure this function is defined or imported
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                    # Limpa os campos
                    for campo in [entry_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                        campo.delete(0, END)

                    mostrar_ml()

                    if 'botao_update' in globals() and bt_update.winfo_exists():
                    bt_update.destroy()

                except Exception as e:
                    messagebox.showerror('Erro', f'Erro ao atualizar: {e}')

            # Botão de salvar alterações
            bt_update = Button(frame_botao, command=update_dados, text="Salvar Atualizações", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
            bt_update.grid(row=0, column=8)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def excluir_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Excluindo os dados
            excluir_dados_ml(valor_id)

            messagebox.showinfo('Sucesso', 'Os dados foram excluídos com sucesso!')

            # Atualizando a tabela
            mostrar_ml()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    #################---------BOTÕES------##################################################################################
    bt_adicionar = Button(frame_botao, command=cadastrar_dados, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_adicionar.grid(row=0, column=1)

    bt_excluir = Button(frame_botao, command=excluir_dados, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_excluir.grid(row=0, column=2)

    bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_imprimir.grid(row=0, column=3)

    bt_calc = Button(frame_botao, command=calcular_media_combustivel, text="Calcular", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_calc.grid(row=0, column=4)

    bt_rela = Button(frame_botao, command=None, text="Relatório", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_rela.grid(row=0, column=5)

    bt_atualizar = Button(frame_botao, command=update_dados, text="Atualizar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
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

    l_v_mês = Label(frame_baixo, text="Valor Mensal R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_mês.place(x=390, y=40)
    e_v_mês = Entry(frame_baixo,textvariable=v_mes_var, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_v_mês.place(x=510, y=40)

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
    e_lucro = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
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
    e_Total_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_Total_entregas.place(x=260, y=100)

    #Tabela Mercado Livre
    def mostrar_ml():

        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined


        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined


        app_nome = Label(frame_tabela, text="Registros de Rotas", height=1, pady=0, padx=0,relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        list_header = ['id', 'Data', 'Dia da Semana', 'Valor de Rota', 'Km ', 'valor Bomba', 'lucro', 'Entregas', 'devolvidas', 'Total']


        df_list = ver_dados_ml()

        global tree_lucro
        tree_lucro = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
    
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_lucro.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_lucro.xview)

        tree_lucro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_lucro.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)
    
        hd = ["center"] * len(list_header)
        h = [40, 100, 100, 100, 50, 100, 100, 100, 100, 100]

        for n, col in enumerate(list_header):
            tree_lucro.heading(col, text=col.title(), anchor="center")
            tree_lucro.column(col, width=h[n], anchor=hd[n])

        for item in df_list:
            tree_lucro.insert("", "end", values=item)
    mostrar_ml()

root.mainloop()
                                                                                                                                       