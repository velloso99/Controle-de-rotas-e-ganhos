from pacotes import*


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
def abrir_mlrota():
    # Caminho do arquivo que será aberto
    mlrota= "ml_rota.py"
    # Abre o novo arquivo
    subprocess.Popen([sys.executable, mlrota])
    # Fecha a janela atual
    root.destroy()
    
def abrir_sprota():
    # Caminho do arquivo que será aberto
    sp_rota= "shoppee.rota.py"
    # Abre o novo arquivo
    subprocess.Popen([sys.executable, sp_rota])
    # Fecha a janela atual
    root.destroy()

#################---------TITULO------##################################################################################
l_titulo= Label(frame_cima, text="Controle de Rotas e Ganhos", anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------BOTÕES------##################################################################################
bt_ml = Button(frame_baixo, command=abrir_mlrota, text="Mercado Livre", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_ml.place(x=20, y=30)

bt_sp = Button(frame_baixo, command=abrir_sprota, text="Shooppee", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
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




root.mainloop()
                                                                                                                                       