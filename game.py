def game():
    name = input("Enter your name: ")
    import random
    number = random.randint(1, 99)
    guess = int(input("Enter your guess between 1 to 99: "))


    while number != guess:
        if number > guess:
            print("Number is bigger")
        else:
            print("Number is smaller")
        guess = int(input("Enter your guess between 1 to 99: "))
        print(f"Yayyyyy {name}, you have won the game")


    request = input("Would you like to play again: y,n: ")
    if request == "n":
        print("Thanks for playing!")
    else:
        game()
game()
