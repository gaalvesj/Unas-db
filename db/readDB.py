import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('unas_banco_de_dados.db')
cursor = conn.cursor()

# Executar uma consulta SQL para selecionar todos os dados da tabela
cursor.execute("SELECT * FROM Tabela_CCA")

# Recuperar e imprimir todos os resultados da consulta
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fechar a conexão com o banco de dados
conn.close()
