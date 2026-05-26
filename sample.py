a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
operator = input("enter operator (+,-,*,/): ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:    print("Invalid operator. Please use +, -, *, or /.")
 
 