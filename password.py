name = input("Enter your name: ")
password = input("Enter you password: ")


if len(password) < 6:
    print("The password cannot have less than 6 characters")
else:
    print("The password has been created")
print("To check it enter name and password")

first = input("Your name: ")
pin = input("Enter password: ")
if first == name and pin == password:
    print("Correct")
else:
    print("Wrong name or password")   