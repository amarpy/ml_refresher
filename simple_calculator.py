#basic_calculator

#add 2 numbers
def add(num1, num2):
    return num1+num2

#subtract 2 numbers
def subtract(num1, num2):
    return num1-num2

#multiply 2 numbers
def multiply(num1, num2):
    return num1*num2

#divide 2 numbers
def divide(num1, num2):
    if num2 == 0:
        print("Error! Divition by zero not allowed.")
    else:
        return num1/num2

def calculator():
    print("Select an operation (1/2/3/4) :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        operation = input("Enter your selection: ")

        if operation in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                print(f"{num1} + {num2} =  {add(num1, num2)}")
            
            if operation == '2':
                print(f"{num1} - {num2} =  {subtract(num1, num2)}")

            if operation == '3':
                print(f"{num1} * {num2} =  {multiply(num1, num2)}")

            if operation == '4':
                print(f"{num1} / {num2} =  {divide(num1, num2)}")
        else: 
            print("Please select a valid operation.")

        next_calculation = input("Do you want to perform another operation? (yes/no) : ")

        if next_calculation.lower() != 'yes':
            break
    print("Exiting calculator. Bye!")

calculator()
        


