## VALIDAR SE OS NÚMEROS SÃO VÁLIDOS
def valid_number1(num1):
    while True:
        try:
            return float(input(num1))
        except ValueError:
            print("Write a valid number!")
def valid_number2(num2):
    while True:
            try:
                return float(input(num2))
            except ValueError:
                print("Write a valid number!")

## FORMATAR O NUMERO PARA INT CASO NÃO TENHA CASA DECIMAL
def format_number(num):
    if num.is_integer():
        return int(num)
    else:
        return num

## MENU DE OPERAÇÕES
def list_operations(num1, num2):
    running = True
    operation = int(input("> "))
    while running:
        match operation:
            case 1:
                return num1 * num2
            case _:
                return "Unavailable operation/ERROR"



