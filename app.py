from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "chave_secreta"  # usada para mostrar mensagens (flash)

# banco de dados
def conecta_db():
    # Garante que a conexão está sempre fechada no final
    return sqlite3.connect("Sistema_cadastros.db")

def cria_tabela():
    conn = conecta_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Confirma_senha TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

cria_tabela() 


# rota principal (index)
@app.route("/")
def index():
    return render_template("index.html")



#cadastrar
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    username = request.form["username"].strip()
    email = request.form["email"].strip()
    senha = request.form["senha"].strip()
    confirma = request.form["confirma"].strip()

    if not username or not email or not senha or not confirma:
        flash("Por favor, preencha todos os campos.", "error")
        return redirect(url_for("login", abrir="cadastro"))
    elif len(username) < 4:
        flash("O nome de usuário deve ter pelo menos 4 caracteres!", "warning")
        return redirect(url_for("login", abrir="cadastro"))
    elif senha != confirma:
        flash("As senhas não coincidem.", "error")
        return redirect(url_for("login", abrir="cadastro"))
    elif len(senha) < 6:
        flash("A senha deve ter pelo menos 6 caracteres!", "warning")
        return redirect(url_for("login", abrir="cadastro"))
    elif len(senha) > 12:
        flash("A senha deve ter no máximo 12 caracteres.", "warning")
        return redirect(url_for("login", abrir="cadastro"))
    elif "@" not in email or "." not in email:
        flash("E-mail inválido. Inclua um '@' e um domínio válido.", "error")
        return redirect(url_for("login", abrir="cadastro"))

    conn = conecta_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE Username = ?", (username,))
    if cursor.fetchone():
       flash("Esse nome de usuário já está cadastrado.", "warning")
       conn.close()
       return redirect(url_for("login", abrir="cadastro"))

    cursor.execute("SELECT * FROM Usuarios WHERE Email = ?", (email,))
    if cursor.fetchone():
        flash("Esse e-mail já está cadastrado.", "warning")
        conn.close()
        return redirect(url_for("login", abrir="cadastro"))

    cursor.execute("""
        INSERT INTO Usuarios (Username, Email, Senha, Confirma_senha)
        VALUES (?, ?, ?, ?)
    """, (username, email, senha, confirma))
    conn.commit()
    conn.close()

    flash(f"Usuário {username} cadastrado com sucesso!", "success")
    return redirect(url_for("login"))


# login
@app.route("/login", methods=["GET", "POST"]) 
def login():
    # Se a requisição for GET, o usuário tentou acessar /login diretamente.
    if request.method == "GET":
        return render_template("login.html")

    # Se a requisição for POST
    email = request.form["email"].strip()
    senha = request.form["senha"].strip()

    if not email or not senha:
        flash("Preencha todos os campos!", "warning")
        return redirect(url_for("login"))

    conn = conecta_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Usuarios WHERE Email = ? AND Senha = ?", (email, senha))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        #flash(f"Login realizado com sucesso!", "success")
        #return redirect(url_for("home"))
        session["usuario"] = email
        return redirect(url_for("home"))
    else:
        flash("Usuário ou senha incorretos.", "error")
        return redirect(url_for("login"))
    
@app.route("/home")
def home():
    return render_template("menu.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)