from pacotes import*
from views import*
import sqlite3



sp_rota = Tk()
sp_rota.title("Controle de Rotas e Ganhos")
sp_rota.geometry("900x400")
sp_rota.configure(background=co0)
sp_rota.resizable(width=False, height=False)
largura_root= 900
altura_root= 400
#obter tamanho da tela
largura_tela = sp_rota.winfo_screenwidth()
altura_tela = sp_rota.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
sp_rota.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

###############---------FRAME------##################################################################################
frame_cima = Frame(sp_rota, width=900, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(sp_rota, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_botao = Frame(sp_rota, width=900, height=50, bg=co1, relief='flat')
frame_botao.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(sp_rota, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_baixo = Frame(sp_rota, width=900, height=350, bg=co1, relief='flat')
frame_baixo.grid(row=4, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(sp_rota, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680)

frame_tabela = Frame(sp_rota, width=900, height=350, bg=co1, relief='flat')
frame_tabela.grid(row=6, column=0, padx=0, pady=0, sticky=NSEW)
#################---------TITULO------##################################################################################
l_titulo=Label(frame_cima, text="Rota da Shoppee",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

#################---------CONFIGURAÇÕES BOTÕES------##################################################################################
def abrir_painel():
    painel = "main.py"  # nome do script a ser aberto
    subprocess.Popen([sys.executable, painel])
    sp_rota.destroy()  # fecha a janela atual






sp_rota.mainloop()