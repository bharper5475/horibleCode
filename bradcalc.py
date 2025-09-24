def calculator():
    print("Calculator By Brad Harper and Jacob Pierno")
    print ("Options: +, -, *, /")
    print ("Type 'exit' to quit")

    while True:
        firstNum = input("\nEnter first number: ")
        if firstNum.lower() == 'exit':
            break
        firstNum = float(firstNum)

        op = input("Enter operator: ")
        if op.lower() == 'exit':
            break

        secondNum = input("Enter second number: ")
        if secondNum.lower() == 'exit':
            break
        secondNum = float(secondNum)

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

if __name__ == "__main__":
    calculator()