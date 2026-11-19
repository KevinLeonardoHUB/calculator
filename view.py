from controller import *

def app_mainframe():
    # Appearance mode
    ctk.set_appearance_mode("dark")

    #  Header and size
    app = ctk.CTk()
    app.title("Calculadora MilGrau")
    app.geometry("480x670")
    
    # Buttons function
    main_calc(app)
    
    
    app.mainloop()
