import customtkinter as ctk 
import sqlite3
from tkinter import messagebox
import os 
print(os.path.abspath("Sistema_cadastros.db"))


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#banco de dados
class BackEnd():
    def conecta_db(self):
        self.comn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.comn.cursor()
        print("Banco de dados conectado")

    def desconecta_db(self):
        self.comn.close()
        print("Banco de dados desconectado")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_senha TEXT NOT NULL
            );
        """)
        self.comn.commit()
        print("Tabela criada com sucesso")
        self.desconecta_db()        

    def cadastrar(self):
        username = self.username_cadastro_entre.get().strip()
        email = self.email_cadastro_entre.get().strip()
        senha = self.senha_cadastro_entre.get().strip()
        confirma = self.confirma_senha_entre.get().strip()

        if not username or not email or not senha or not confirma:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        elif len(username) < 4:
            messagebox.showwarning("Aviso", "O nome de usuário deve ter pelo menos 4 caracteres!")
            return
        elif senha != confirma:
            messagebox.showerror("Erro", "As senhas não coincidem")
            return
        elif len(senha) > 12:
            messagebox.showwarning("Aviso", "A senha deve ter no máximo 12 caracteres")
            return
        elif "@" not in email or "." not in email:
            messagebox.showerror("Erro", "E-mail inválido. Inclua um '@' e um domínio válido")
            return
        try:
            self.conecta_db()
            self.cursor.execute("SELECT * FROM Usuarios WHERE Username = ?", (username,))
            if self.cursor.fetchone():
                messagebox.showwarning("Aviso", "Esse nome de usuário já está cadastrado.")
                self.desconecta_db()
                return
            
            self.cursor.execute("SELECT * FROM Usuarios WHERE Email = ?", (email,))
            if self.cursor.fetchone():
                messagebox.showwarning("Aviso", "Esse e-mail já está cadastrado.")
                self.desconecta_db()
                return
            

            self.cursor.execute("""
                INSERT INTO Usuarios (Username, Email, Senha, Confirma_senha)
                VALUES (?, ?, ?, ?)
            """, (username, email, senha, confirma))
            self.comn.commit()
            messagebox.showinfo("Sucesso", f"Usuário {username} cadastrado com sucesso!")
            self.limpa_entre_cadastro()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")
        finally:
            self.desconecta_db()                           
                    
    def verifica_login(self):
        username = self.username_login_entre.get().strip()
        senha = self.senha_login_entre.get().strip()

        if not username or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        self.conecta_db()
        self.cursor.execute("SELECT * FROM Usuarios WHERE Username = ? AND Senha = ?", (username, senha))
        usuario = self.cursor.fetchone()
        self.desconecta_db()

        if usuario:
            messagebox.showinfo("Login", f"Bem vindo, {username}!")
            self.limpa_entre_login()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")      

class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.cria_tabela()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()

    def toggle_senha(self, entry):
        #mostrar senha
        if entry.cget("show") == "*":
            entry.configure(show="")
        else:
            entry.configure(show="*")    

    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False, False)

    def tela_de_login(self):
       if hasattr(self, "frame_cadastro"):
        self.frame_cadastro.place_forget()

        #frame login
       self.frame_login = ctk.CTkFrame(self, width=350, height=380)
       self.frame_login.place(x=350, y=10)  

        #Colocando widgets dentro do formulario
       self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu login", font=("Century Gothic bold", 22))
       self.lb_title.grid(row=0, column=0, padx=10, pady=10)

       self.username_login_entre = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Nome de usuário",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
       self.username_login_entre.grid(row=1, column=0, pady=10, padx=10)

       self.senha_login_entre = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
       self.senha_login_entre.grid(row=2, column=0, pady=10, padx=10)

       self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Mostrar senha",
        command=lambda: self.toggle_senha(self.senha_login_entre))
       self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

       self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Fazer Login".upper(),
        font=("Century Gothic bold", 14), corner_radius=15, command=self.verifica_login)
       self.btn_login.grid(row=4, column=0, pady=10, padx=10)

       self.span = ctk.CTkLabel(self.frame_login, text="Ainda não tem conta? Cadastre-se agora",
        font=("Century Gothic", 10))
       self.span.grid(row=5, column=0, pady=10, padx=10)

       self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300,  fg_color="green", hover_color="#050",
        text="Fazer Cadastro".upper(),
        font=("Century Gothic bold", 14), corner_radius=15,
        command=self.tela_de_cadastro)
       self.btn_cadastro.grid(row=6, column=0, pady=10, padx=10)

    def tela_de_cadastro(self):
        #Remover formulário de login
        self.frame_login.place_forget()

         #frame de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)  

        #Criando titulo
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Cadastra-se", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=5)

        #criar widgets tela cadastro
        self.username_cadastro_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        self.username_cadastro_entre.grid(row=1, column=0, pady=5, padx=10)

        self.email_cadastro_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="E-mail de usuário",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        self.email_cadastro_entre.grid(row=2, column=0, pady=5, padx=10)

        self.senha_cadastro_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha de usuario",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        self.senha_cadastro_entre.grid(row=3, column=0, pady=5, padx=10)

        self.confirma_senha_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar a senha",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        self.confirma_senha_entre.grid(row=4, column=0, pady=5, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Mostrar senhas",
        command=lambda: (self.toggle_senha(self.senha_cadastro_entre),
        self.toggle_senha(self.confirma_senha_entre)))
        self.ver_senha.grid(row=5, column=0, pady=10)

        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300,  fg_color="green", hover_color="#050",
        text="Fazer Cadastro".upper(),
        font=("Century Gothic bold", 16), corner_radius=15,
        command=self.cadastrar)
        self.btn_cadastrar_user.grid(row=6, column=0, pady=5, padx=10)

        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar Login".upper(),
        font=("Century Gothic bold", 14), corner_radius=15, fg_color="#144", hover_color="#333", command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, pady=10, padx=10)

    def limpa_entre_cadastro(self):
        self.username_cadastro_entre.delete(0, ctk.END)
        self.email_cadastro_entre.delete(0, ctk.END)
        self.senha_cadastro_entre.delete(0, ctk.END)
        self.confirma_senha_entre.delete(0, ctk.END)

    def limpa_entre_login(self):
        self.username_login_entre.delete(0, ctk.END)
        self.senha_login_entre.delete(0, ctk.END)

if __name__=="__main__":
    app = App()
    app.mainloop()
