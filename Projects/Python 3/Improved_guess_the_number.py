# Guess the number app.
import random

difficulty = ["1", "2", "3", "4", "easy", "normal", "hard", "expert"]

while True:
    d = input("Choose difficulty: \n 1. Very easy  2.Easy \n 3.Normal  4.Hard  5.Expert ").lower()
    while d not in difficulty:
        print("Invalid input")
        d = input("Choose difficulty: \n 1.Easy  2.Normal \n 3.Hard  4.Expert").lower()
        if d in difficulty:
            break

    if d == "very easy" or d == "1":
        x = random.randint(1,2)
        guess = int(input("Guess a random number from 1 to 2. "))
        while guess < 1 or guess > 2:
            print("Invalid input")
            guess = int(input("Guess a random number from 1 to 2. "))
            if guess >= 1:
                if guess <= 2:
                    break

        if guess == x:
            print(f"you won. the number is {x}")
        else:
            print(f"Bad luck! you lost. the number is {x}")


    elif d == "easy" or d == "2":
        x = random.randint(1, 25)
        guess = int(input("Guess a random number from 1 to 25. "))
        while guess < 1 or guess > 25:
            print("Invalid input")
            guess = int(input("Guess a random number from 1 to 25. "))
            if guess >= 1:
                if guess <= 25:
                    break

        if guess == x:
            print(f"you won. the number is {x}")
        else:
            print(f"Bad luck! you lost. the number is {x}")


    elif d == "normal" or d == "3":
        x = random.randint(1, 50)
        guess = int(input("Guess a random number from 1 to 50. "))
        while guess < 1 or guess > 50:
            print("Invalid input")
            guess = int(input("Guess a random number from 1 to 50. "))
            if guess >= 1:
                if guess <= 50:
                    break

        if guess == x:
            print(f"you won. the number is {x}")
        else:
            print(f"Bad luck! you lost. the number is {x}")


    elif d == "hard" or d == "4":
        x = random.randrange(1, 75)
        guess = int(input("Guess a random number from 1 to 75. "))
        while guess < 1 or guess > 75:
            print("Invalid input")
            guess = int(input("Guess a random number from 1 to 75. "))
            if guess >= 1:
                if guess <= 75:
                    break

        if guess == x:
            print(f"you won. the number is {x}")
        else:
            print(f"Bad luck! you lost. the number is {x}")


    elif d == "expert" or d == "5":
        x = random.randrange(1, 100)
        guess = int(input("Guess a random number from 1 to 100. "))
        while guess < 1 or guess > 100:
            print("Invalid input")
            guess = int(input("Guess a random number from 1 to 100. "))
            if guess >= 1:
                if guess <= 100:
                    break

        if guess == x:
            print(f"you won. the number is {x}")
        else:
            print(f"Bad luck! you lost. the number is {x}")

    p = input("Do you want to play again? (y/n) ").lower()
    while p not in ["y", "n"]:
        print("Invalid input")
        p = input("Do you want to play again? (y/n) ").lower()
        if p in ["y", "n"]:
            break
    if p != "y":
        break