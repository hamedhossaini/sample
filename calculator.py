first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))

sign = input("Enter a math sign: ")

if sign == "+":
    total = first + second
elif sign == "-":
    total = first - second
elif sign == "*":
    total = first * second
elif sign == "/":
    total = first / second
else:
    print("Invalid sign")
print(total)    
