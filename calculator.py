from functions import valid_number1, valid_number2, format_number, list_operations


    
def main():
    number1 = valid_number1("> ")
    number1 = format_number(number1)
    number2 = valid_number2("> ")
    number2 = format_number(number2)

    print(f"Available operations\n[press the assigned number for the assigned operation]:\n1. {number1} x {number2} | 2. {number1} / ? | 2. {number1} -  ? | 3. {number1} + ? | 4. {number1}^2 | 5. {number1}^? | 6. sqrt({number1})\n")

    result = list_operations(number1, number2)

    print(result)
    
    

if __name__ == "__main__":
    main()