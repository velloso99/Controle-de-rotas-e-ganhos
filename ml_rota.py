from pacotes import*


mlrota = Tk()
mlrota.title("Controle de Rotas e Ganhos")
mlrota.geometry("600x400")
mlrota.configure(background=co0)
mlrota.resizable(width=False, height=False)
largura_root= 600
altura_root= 400
#obter tamanho da tela
largura_tela = mlrota.winfo_screenwidth()
altura_tela = mlrota.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
mlrota.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")




mlrota.mainloop()