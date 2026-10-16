import customtkinter as ctk


def rows(app):
    textos = ["7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "=", "÷"]

    for indice, texto in enumerate(textos):
        botao = ctk.CTkButton(
            app,
            text=texto,
            width=120,
            height=120,
            corner_radius=1
        )
        botao.grid(
            row=indice // 4,
            column=indice % 4,
            padx=0,
            pady=(200, 0) if indice < 4 else 0
        )

        if texto == "x" or texto == "-" or texto == "+" or texto == "÷":
            botao.configure(
                fg_color="#FF9500",
                hover_color="#FFB84D"
            )
        elif texto == "=":
            botao.configure(
                fg_color="#1111EE",
                hover_color="#00869E"
            )
        else:
            botao.configure(
                fg_color="#8a8181",
                hover_color="#00869E"
            )


def app_mainframe():
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("Calculadora MilGrau")
    app.geometry("480x650")

    rows(app)

    app.mainloop()
