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

@app.route('/cca', methods=['GET'])
def get_cca():
    nome_termo = request.args.get('cca', default=None, type=str)

    query = "SELECT * FROM Tabela_UNAS"
    rows = query_db(query)

    cca = []
    for row in rows:
        if nome_termo is None or nome_termo.lower() in row[1].lower():
            cca.append({'id': row[0], 'nome': row[1], 'data_nascimento': row[2]})

    return jsonify(cca)


if __name__ == '__main__':
    app.run(debug=True)
