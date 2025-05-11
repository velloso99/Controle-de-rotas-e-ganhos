from pacotes import *
import sqlite3

#criando conexão

try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com Banco de Dados!")
 
# Tabela Mercado Livre
def criar_dados_ml(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Rota_Mercado_Livre(data,dia_semana,valor_rota,valor_bomba,km,lucro,entregas,devolvidas,total) values(?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dados
#-----------------------------------------------------------------------------------------------------------------
def ver_dados():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM Rota_Mercado_Livre')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados:{e}")
        return []

#-----------------------------------------------------------------------------------------------------------------
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Rota_Mercado_Livre SET data=?,dia_semana=?,valor_rota=?,valor_bomba=?,km=?,lucro=?,entregas=?,devolvidas=?,total=? WHERE id=?"
        cur.execute(query, i)
#-----------------------------------------------------------------------------------------------------------------
def excluir_dados(i):   
    with con:
        cur = con.cursor()
        query = "DELETE FROM Rota_Mercado_Livre WHERE id=?"
        cur.execute(query, (i,))
##############################################################################################################################################################
# Tabela Shoppee
def criar_dados_s(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Rota_Shoppee(data,valor_rota,valor_bomba,km,valor_total,lucro,entregas,devolvidas,dia_semana) values(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dados
#-----------------------------------------------------------------------------------------------------------------
def ver_dados():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM Rota_Shoppee')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []

#-----------------------------------------------------------------------------------------------------------------
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Rota_Shoppee SET data=?,valor_rota=?,valor_bomba=?,km=?,valor_total=?,lucro=?,entregas=?,devolvidas=? WHERE id=?"
        cur.execute(query, i)
#-----------------------------------------------------------------------------------------------------------------  
def excluir_dados(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Rota_Shoppee WHERE id=?"
        cur.execute(query, (i,))






 