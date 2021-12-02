from art import logo
#Calculation
#Add
def add(n1,n2): 
    return n1+ n2
#Substract 
def substract(n1,n2): 
    return n1 - n2
#Multiply 
def multiply(n1,n2): 
    return n1*n2
#Divide
def divide(n1,n2): 
    return n1/n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

#User input
def calculator(): 
    print(logo)
    num_1 = float(input("Enter the first number: "))
    for symbol in operations: 
        print(symbol)
    should_continue = True

    while should_continue: 
        operator = input("Enter an operator: ")
        num_2= float(input("Enter the next number: "))
        calculation_function = operations[operator]
        answer = calculation_function(num_1,num_2)

        print(f"{num_1} {operator} {num_2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ") == "y": 
            num_1 = answer
        else: 
            should_continue = False
            calculator()

calculator()


    



    