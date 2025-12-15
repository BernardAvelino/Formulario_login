import customtkinter as ctk

# Iremos nesse código, configurar a aparência
ctk.set_appearance_mode("dark")

# Criação dos botões de ação e funções de funcionalidades.
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "Pedro" and senha == "1234":
        verificacao.configure(text="Login bem sucedido!", text_color="green")
    else:
        verificacao.configure(text="Login falhou. Tente novamente.", text_color="red")
# Crição da janela principal do formulário
janela = ctk.CTk()
janela.title("Formulário de Cadastro")
janela.geometry("300x300")

# Texto indentificando o campo de entrada do usuário
Lbel_usuario = ctk.CTkLabel(janela, text="Login do Usuário: ")
Lbel_usuario.pack(pady=10)
Lbel_usuario.configure(font=("Arial", 15))

# Campo de entrada para o usuário, "Digite seu Usuário"
entry_usuario = ctk.CTkEntry(janela, placeholder_text="Digite seu usuário")
entry_usuario.pack(pady=10)
entry_usuario.configure(font=("Arial", 15,))

# Texto indentificando o campo de entrada da senha
Lbel_usuario = ctk.CTkLabel(janela, text="Senha do Usuário: ")
Lbel_usuario.pack(pady=10)
Lbel_usuario.configure(font=("Arial", 15))

# Campo de entrada para o usuário, "Digite sua senha"
entry_senha = ctk.CTkEntry(janela, placeholder_text="Digite sua senha: ")
entry_senha.pack(pady=10)
entry_senha.configure(font=("Arial", 15,))

# Botão de ação para entrar no sistema.
bot_loguin = ctk.CTkButton(janela, text="Loguin", command=verificar_login)
bot_loguin.pack(pady=10)
bot_loguin.configure(font=("Arial", 15,))

# Label para exibir a verificação do loguin
verificacao = ctk.CTkLabel(janela, text="")
verificacao.pack(pady=10)

# Inicia o loop de aplicação
janela.mainloop()