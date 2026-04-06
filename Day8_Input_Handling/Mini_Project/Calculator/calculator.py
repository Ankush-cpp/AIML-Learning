# Make a calculator using function -------------->

def calculator(a, b, operation) :
    if (operation == "+") :
        return a + b
    elif operation == "-" :
        return a - b
    elif operation == "*" :
        return a * b 
    elif operation == "/" :
        if b != 0 :
            return a / b
        else :
            return "Division by 0 not allowed"
    else :
        return "Invalid operation"
    
a = float(input("Enter first value : "))
b = float(input("Enter second value : ")) 
operation = input("Enter operations (+, -, *, /):")

result = calculator(a, b, operation)
print("Result", result)