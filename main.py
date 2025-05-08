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









root.mainloop()