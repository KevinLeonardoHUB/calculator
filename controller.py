import customtkinter as ctk
import operator

"""
GUARDAR OS NUMEROS E SIMBOLOS
VARIAVEL GLOBAL PARA SER UTILIZADA DEPOIS
"""
global numbers_saved, lista_operations_saved, num_1, tela

numbers_saved = []
lista_operations_saved = []
num_1 = 0
tela = None


def atualizar_tela(valor=None):
    global tela

    if tela is None:
        return

    if valor is not None:
        tela.configure(text=str(valor))
        return

    if numbers_saved:
        texto = "".join(numbers_saved)
    elif lista_operations_saved:
        texto = " ".join(str(item) for item in lista_operations_saved)
    else:
        texto = "0"

    tela.configure(text=texto)


## DIFERENCIAR SIMBOLOS DE NUMEROS
def clicked(caractere):
    global num_1

    if caractere not in ("=", "-", "x", "÷", "+"):
        numbers_saved.append(caractere)
        print(f"Números utilizados: {numbers_saved}")
        join_numbers()
        atualizar_tela()
        return

    if not numbers_saved:
        return

    join_numbers()
    if caractere == "=":
        lista_operations_saved.append(num_1)
        resultado = calculate()
        print(f"Resultado: {resultado}")
        atualizar_tela(resultado)
        lista_operations_saved.clear()
        numbers_saved.clear()
        num_1 = 0
    else:
        lista_operations_saved.append(num_1)
        lista_operations_saved.append(caractere)
        numbers_saved.clear()
        num_1 = 0
        atualizar_tela()

    print(lista_operations_saved)

## JUNTAR OS TEXTOS E TRANSFORMAR EM FLOAT
def join_numbers():
    global num_1

    ## VALIDAR SE TEM 1 OU 2 PONTOS
    if numbers_saved.count(".") > 1:
        numbers_saved.pop()
        print("O número só pode ter um ponto decimal.")
        return

    numeros_completos = "".join(numbers_saved)

    ## VALIDAR SE O NUMERO COMEÇA VAZIO 
    if numeros_completos == "" or numeros_completos == ".":
        return

    num_1 = float(numeros_completos)
    print(f"O numero completo é: {num_1}")

def calculate():
    global num_1

    if not lista_operations_saved:
        raise ValueError("Não há operações para calcular.")

    num_1 = lista_operations_saved[0]
    ops = operators()
    for i in range(1, len(lista_operations_saved), 2):
        operador = lista_operations_saved[i]
        if operador not in ops:
            raise ValueError(f"Operador inválido: {operador}")
        num_2 = lista_operations_saved[i + 1]
        num_1 = ops[operador](num_1, num_2)

    return num_1

def operators():
    return {
        "+": operator.add,
        "-": operator.sub,
        "x": operator.mul,
        "÷": operator.truediv
    }


def main_calc(app):
    ## BOTOES
    global lista_operations_saved, tela
    textos_botoes = ["7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "÷", "0", ".", "=", "+"]
    app.grid_rowconfigure(0, weight=1)
    tela = ctk.CTkLabel(app, text="0", font=("Arial", 30))
    tela.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 0), sticky="nsew")
    """
    PARA INDICE(QUE TB CONTEM UM TEXTO), 
    USO ENUMERATE PARA CONTAR QUANTOS ELEMENTOS TENHO EM textos_botoes(numeros)
    E CRIAR UM BOTAO PARA CADA, TODOS DO MESMO TAMANHO
    """
    for indice, texto in enumerate(textos_botoes):
        botao = ctk.CTkButton(
            app,
            text=texto,
            width=120,
            height=120,
            corner_radius=1,
            # QUANDO É CLICADO, CHAMO A FUNCAO CLICKED
            command=lambda caractere=texto: clicked(caractere)
        )
        ## A CADA 4 TROCAMOS qDE COLUNA
        botao.grid(
            row=(indice // 4) + 1,
            column=indice % 4,
            padx=0
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


