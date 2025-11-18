import flask
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'chave_secreta'

DATABASE = 'database.db'
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
 
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movimentacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida')),
                data TEXT NOT NULL
            )
        ''')
        db.commit()



    import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

@app.route('/historico')
def historico():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM movimentacao ORDER BY data DESC")
    movimentacoes = cursor.fetchall()
    historico = []
    for linha in movimentacoes:
        historico.append({
            'id': linha['id'],
            'descricao': linha['descricao'],
            'valor': linha['valor'],
            'tipo': linha['tipo'],
            'data': linha['data']
        })
    return jsonify(historico)

if __name__ == "__main__":
    init_db()  # cria a tabela
    app.run(debug=True)