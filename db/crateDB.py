import sqlite3
import openpyxl

# Carregar o arquivo do Excel
workbook = openpyxl.load_workbook('/Users/gabrielalves/projetos-pessoais/Unas-db/db/cca_resposta.xlsx')
sheet = workbook.active
print(sheet)

# Conectar ou criar um banco de dados SQLite
conn = sqlite3.connect('unas_banco_de_dados.db')
cursor = conn.cursor()

# Criar uma tabela no banco de dados (ajuste os campos conforme necessário)
cursor.execute('''CREATE TABLE IF NOT EXISTS Tabela_CCA (id INTEGER PRIMARY KEY, nome TEXT, idade TEXT, projeto TEXT, raca TEXT, bairro TEXT )''')

# Ler as linhas do arquivo do Excel e inserir na tabela do banco de dados
for row in sheet.iter_rows(min_row=2, values_only=True):
    cursor.execute("INSERT INTO Tabela_CCA (projeto, nome, idade, raca, bairro) VALUES (?, ?, ?, ?, ?)", (row[1], row[2], row[3], row[4], row[5]))

# Salvar as alterações e fechar a conexão com o banco de dados
conn.commit()
conn.close()
