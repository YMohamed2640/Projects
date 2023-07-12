import random

s = ["rock", "paper", "scissors"]
valid_in = [1, 2]
valid_p = ["y", "n"]
choice = random.choice(s)

while True:
    user = input("1.Rock  2.paper  3.scissors ").lower()

    while user not in s:
        print("Invalid input.")
        user = input("1.Rock  2.paper  3.scissors ").lower()
        if user in s:
            break

    if choice ==  "rock" and user == "paper":
        print("You win! The computer chose rock.")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "rock" and user == "scissors":
        print("You lose! The computer choose rock.")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "rock" and user == "rock":
        print("Draw! the computer also chose rock.")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "paper" and user == "rock":
        print("You lose! the computer chose paper.")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "paper" and user == "scissors":
        print("You win! the computer chose paper.")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "paper" and user == "paper":
        print("Draw! the computer also chose paper.")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "scissors" and user == "rock":
        print("You win! the computer chose scissors")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "scissors" and user == "paper":
        print("You lose! the computer chose scissors")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue

    elif choice == "scissors" and user == "scissors":
        print("Draw! the computer also chose scissors")
        p = input("Do you want to play again? (y/n) ").lower()
        while p not in valid_p:
            print("Invalid input")
            p = input("Do you want to play again? (y/n) ").lower()
            if p in valid_p:
                break
        if p != "y":
            break
        else:
            choice = random.choice(s)
            continue