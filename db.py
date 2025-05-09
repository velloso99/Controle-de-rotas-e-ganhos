from pacotes import *
import sqlite3

#criando conexão

try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com Banco de Dados!")
    
# Crinado  Tabela do Banco de dados
#Tabela Rota Mercado lIvre
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Rota_Mercado_Livre(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                valor_rota TEXT,
                km TEXT,
                valor_bomba TEXT,
                valor_total TEXT,
                lucro TEXT,
                entregues TEXT,
                devolvidas TEXT,
            )""")
        print("Tabela Rota Mercado Livre criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Rota Mercado Livre!")
    
    
    