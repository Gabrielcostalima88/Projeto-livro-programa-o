from random import randint
secret = randint(1,100)
print("Welcome.")
guess = 0
while secret != guess:
    g = input("Guess the number: ")
    guess = int(g)
    if secret == guess:
        print("You win!")
    else:
        if guess > secret:
            print("Too high")
        else:
            print("too low")
print("Game over!")

