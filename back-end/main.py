from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query):
    conn = sqlite3.connect('/Users/gabrielalves/projetos-pessoais/Unas-db/unas_banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/', methods=['GET'])
def get_pessoas():
    rows = query_db("SELECT * FROM Tabela_UNAS")
    pessoas = []
    for row in rows:
        pessoas.append({'id': row[0], 'projeto': row[1], 'nome': row[2], 'idade': row[3]})
    return jsonify(pessoas)

if __name__ == '__main__':
    app.run(debug=True)
