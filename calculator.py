import time
from functions import clear_console, valid_number1, valid_number2, format_number, list_operations


    
def main():
    while True:
        number1 = valid_number1("> ")
        number1 = format_number(number1)
        number2 = valid_number2("> ")
        number2 = format_number(number2)


        print(f"Available operations\n[press the assigned number for the assigned operation]:\n1. {number1} x {number2} | 2. {number1} / {number2} | 3. {number1} -  {number2} | 4. {number1} + {number2} | 5. {number1}^2 | 6. {number1}^{number2} | 7. sqrt({number1})\n")

        result = list_operations(number1, number2)

        print(result)
        time.sleep(3)
        clear_console() 
        
        

if __name__ == "__main__":
    main()