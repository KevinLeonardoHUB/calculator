import customtkinter as ctk
import operator
"""
GUARDAR OS NUMEROS E SIMBOLOS
VARIAVEL GLOBAL PARA SER UTILIZADA DEPOIS
"""
global numbers_saved, signals, num
numbers_saved = []
signals_saved = []
num = 0


## DIFERENCIAR SIMBOLOS DE NUMEROS
def clicked(caractere):
    if caractere == "=" or caractere == "-" or caractere == "x" or caractere == "÷" or caractere == "+":
        signals_saved.append(caractere)
        print(f"Sinais utilizados: {signals_saved}")
    else:
        numbers_saved.append(caractere)
        print(f"Números utilizados: {numbers_saved}")
        
    # Função para juntar os números e transformar em float
    join_numbers()

## JUNTAR OS TEXTOS E TRANSFORMAR EM FLOAT
def join_numbers():
    ## VALIDAR SE TEM 1 OU 2 PONTOS
    if numbers_saved.count(".") > 1:
        numbers_saved.pop()
        print("O número só pode ter um ponto decimal.")
        return

    numeros_completos = "".join(numbers_saved)
    ## VALIDAR SE O NUMERO COMEÇA VAZIO 
    if numeros_completos == "" or numeros_completos == ".":
        return

    num = float(numeros_completos)
    print(f"O numero completo é: {num}")
    
def operators():
    ops = 
    {
        "+": operator.add,
        "-": operator.sub,
        "x": operator.mul,
        "÷": operator.truediv
    }
    


def rows(app):
    ## BOTOES
    textos = ["7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "÷", "0", ".", "=", "+"]

    """
    PARA INDICE(QUE TB CONTEM UM TEXTO), 
    USO ENUMERATE PARA CONTAR QUANTOS ELEMENTOS TENHO EM textos(numeros)
    E CRIAR UM BOTAO PARA CADA, TODOS DO MESMO TAMANHO
    """
    for indice, texto in enumerate(textos):
        botao = ctk.CTkButton(
            app,
            text=texto,
            width=120,
            height=120,
            corner_radius=1,
            # QUANDO É CLICADO, CHAMO A FUNCAO CLICKED
            command=lambda caractere=texto: clicked(caractere)
        )
        ## A CADA 4 TROCAMOS DE COLUNA
        botao.grid(
            row=indice // 4,
            column=indice % 4,
            padx=0,
            pady=(200, 0) if indice < 4 else 0
        )

        ## OS SIMBOLOS TEM COR DIFERENTE DOS NUMEROS
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
    # Appearance mode
    ctk.set_appearance_mode("dark")

    #  Header and size
    app = ctk.CTk()
    app.title("Calculadora MilGrau")
    app.geometry("480x670")
    
    # Buttons function
    rows(app)
    
    
    app.mainloop()
