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

#################---------TITULO------##################################################################################
l_titulo= Label(frame_cima, text="Controle de Rotas e Ganhos", anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------BOTÕES------##################################################################################
bt_ml = Button(frame_baixo, command=None, text="Mercado Livre", bd=3, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_ml.place(x=20, y=30)

bt_sp = Button(frame_baixo, command=None, text="Shooppee", bd=3, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_sp.place(x=20, y=60)

bt_loggi = Button(frame_baixo, command=None, text="Loggi", bd=3, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_loggi.place(x=20, y=90)

bt_colagem = Button(frame_baixo, command=None, text="Colagem", bd=3, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_colagem.place(x=20, y=120)

bt_calmensal = Button(frame_baixo, command=None, text="Calculo Mensal", bd=3, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
bt_calmensal.place(x=50, y=30)
                                                                                                                                       