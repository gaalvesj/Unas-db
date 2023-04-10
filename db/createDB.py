import sqlite3
import openpyxl

# Carregar o arquivo do Excel
arquivos_excel = ('/Users/gabrielalves/projetos-pessoais/Unas-db/excel/cca_resposta.xlsx',
                   '/Users/gabrielalves/projetos-pessoais/Unas-db/excel/ps_resposta.xlsx',
                     '/Users/gabrielalves/projetos-pessoais/Unas-db/excel/cei_resposta.xlsx')

# Conectar ou criar um banco de dados SQLite
conn = sqlite3.connect('unas_banco_de_dados.db')
cursor = conn.cursor()

# Criar uma tabela no banco de dados
cursor.execute('''CREATE TABLE IF NOT EXISTS Tabela_UNAS (id INTEGER PRIMARY KEY, nome TEXT, idade TEXT, sexo TEXT, projeto TEXT, raca TEXT, bairro TEXT )''')

# Ler as linhas do arquivo do Excel e inserir na tabela do banco de dados
for arquivo in arquivos_excel:
    workbook = openpyxl.load_workbook(arquivo)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        cursor.execute("INSERT INTO Tabela_UNAS (projeto, nome, idade, sexo, raca, bairro) VALUES (?, ?, ?, ?, ?, ?)", (row[1], row[2], row[3], row[4], row[5], row[6]))

# Salvar as alterações e fechar a conexão com o banco de dados
conn.commit()
conn.close()
