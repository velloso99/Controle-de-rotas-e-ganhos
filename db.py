from pacotes import *
import sqlite3

#criando conexão

try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com Banco de Dados!")