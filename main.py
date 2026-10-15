import customtkinter as ctk


def app_mainframe():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    app.title("Calculadora MilGrau")
    app.geometry("500x650")

    
    button_7 = ctk.CTkButton(
        app,
        text="7",
        width=140,
        height=140,
        corner_radius=10
    )
    button_7.pack(anchor="w",padx=0,pady=200)

    button_8 = ctk.CTkButton(
        app,
        text="8",
        width=140,
        height=140,
        corner_radius=10
    )
    button_8.pack(anchor="w",padx=150,pady=200)


    button_9 = ctk.CTkButton(
        app,
        text="9",
        width=140,
        height=140,
        corner_radius=10
    )
    button_9.pack(anchor="w",padx=290,pady=200)
    

    app.mainloop()



if __name__ == "__main__":
    app_mainframe()
    
