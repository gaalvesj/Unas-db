import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('/Users/gabrielalves/projetos-pessoais/Unas-db/unas_banco_de_dados.db')
cursor = conn.cursor()

# Executar uma consulta SQL para selecionar todos os dados da tabela
cursor.execute("SELECT COUNT(*) FROM Tabela_UNAS ")

# Recuperar e imprimir todos os resultados da consulta
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fechar a conexão com o banco de dados
conn.close()
