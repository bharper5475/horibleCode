"""
Simple terminal based calculator app.

Authors: Brad Harper and Jacob Pierno
Description: Basic calculator app in the terminal. Provides functionality for addition, subtraction, multiplication, and division.
Users can exit at any point by typing 'exit'

"""
def calculator():
    """
    Runs an interactive calculator loop.
    Prompts the user for two numbers and an operator, then prints the result and starts over. 
    """
    print("Calculator App")
    print ("Options: +, -, *, /")
    print ("Type 'exit' to quit")

    while True:
        # Prompt for first number or exit
        firstNum = input("\nEnter first number: ")
        if firstNum.lower() == 'exit':
            break
        firstNum = float(firstNum)
        
        # Prompt for operator or exit
        op = input("Enter operator: ")
        if op.lower() == 'exit':
            break
        # Prompt for second number or exit
        secondNum = input("Enter second number: ")
        if secondNum.lower() == 'exit':
            break
        secondNum = float(secondNum)
        
        # Perform calculation
        if op == '+':
            result = firstNum + secondNum
        elif op == '-':
            result = firstNum - secondNum
        elif op == '*':
            result = firstNum * secondNum
        elif op == '/':
            if secondNum == 0:
                print("Error: Division by zero")
            else:
                result = firstNum / secondNum

        print("Result: ", result)
# Main program
if __name__ == "__main__":
    calculator()