import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()

    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False, False)

    def tela_de_login(self):
        
        #Titulo da plataforma
        self.title = ctk.CTkLabel(self, text="Faça o login \n ou \n Cadastre-se!"
        , font=("Century Gothic bold", 14))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        #Criar a frame do formulario
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

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha",
        font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Fazer Login".upper(),
        font=("Century Gothic bold", 14), corner_radius=15)
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
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu login", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=5)

        #criar widgets tela cadastro
        self.username_cadastro_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        self.username_cadastro_entre.grid(row=1, column=0, pady=5, padx=10)

        self.username_cadastro_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="E-mail de usuário",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue")
        self.username_cadastro_entre.grid(row=2, column=0, pady=5, padx=10)

        self.senha_cadastro_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha de usuario",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        self.senha_cadastro_entre.grid(row=3, column=0, pady=5, padx=10)

        self.confirma_senha_entre = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar a senha",
        font=("Century Gothic bold", 16), corner_radius=15, border_color="blue", show="*")
        self.confirma_senha_entre.grid(row=4, column=0, pady=5, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha",
        font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=5, column=0, pady=10)

        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300,  fg_color="green", hover_color="#050",
        text="Fazer Cadastro".upper(),
        font=("Century Gothic bold", 16), corner_radius=15,
        command=self.tela_de_cadastro)
        self.btn_cadastrar_user.grid(row=6, column=0, pady=5, padx=10)

        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar Login".upper(),
        font=("Century Gothic bold", 14), corner_radius=15, fg_color="#144", hover_color="#333", command=self.tela_de_login)
        self.btn_login_back.grid(row=7, column=0, pady=10, padx=10)

        


if __name__=="__main__":
    app = App()
    app.mainloop()

# clientes = {}

# def cadastrar():
#     print("Cadastro de usuário")
#     nome = input("Nome: ")
#     senha = input("Senha: ")
#     clientes[nome] = senha
#     print("Usuário cadastro com sucesso!\n")


# def fazer_login():
#     nome = input("Nome: ")
#     senha = input("Senha: ")

#     if nome in clientes:
#         if clientes[nome] == senha:
#             print("Login bem sucedido!")
#         else :
#             print("Senha incorreta!")
#     else :
#         print("Usuário não encontrado!")
    

# def menu():
#    while True: 
#        print("Escolha uma opção")
#        print("Menu")
#        print("Cadastrar")
#        print("login")
#        print("Sair")

#        escolha = input("Escolha uma opção: ") 

#        if escolha == "1":
#            cadastrar()
#        elif escolha == "2":
#            fazer_login()
#        elif escolha == "3":
#            print("Saindo do programa!!")
#            break
#        else:
#            print("Opção inválida. Tente novamente.\n")
    
# menu()