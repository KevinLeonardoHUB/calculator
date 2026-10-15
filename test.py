
"""import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("420x380")

# Título
titulo = ctk.CTkLabel(
    app,
    text="Bem-vindo!",
    font=("Arial", 26, "bold")
)
titulo.pack(pady=(30, 10))

# Campo de utilizador
utilizador = ctk.CTkEntry(
    app,
    width=260,
    placeholder_text="Nome de utilizador"
)
utilizador.pack(pady=10)

# Campo de palavra-passe
senha = ctk.CTkEntry(
    app,
    width=260,
    placeholder_text="Palavra-passe",
    show="*"
)
senha.pack(pady=10)

# Mensagem de resultado
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

# Função para validar o login
def fazer_login():
    nome = utilizador.get()
    password = senha.get()

    if nome == "admin" and password == "1234":
        resultado.configure(
            text="Login realizado com sucesso!",
            text_color="green"
        )
    else:
        resultado.configure(
            text="Dados incorretos!",
            text_color="red"
        )

# Botão
botao = ctk.CTkButton(
    app,
    text="Entrar",
    command=fazer_login,
    width=260,
    height=40,
    corner_radius=10
)
botao.pack(pady=10)

app.mainloop()"""
