# Dice rolling project
import time
import random

Numbers = [1, 2, 3, 4, 5, 6]

print("Hello to the Dice roller")
time.sleep(2)
while True:
    start = input("Do you want to assign events to every number? (y/n) ").lower()
    while start not in ["y", "n"]:
        print("Invalid input")
        start = input("Do you want to assign events to every number? (y/n) ").lower()
        if start in ["y", "n"]:
            break
    if start == "y":
        e1 = input("Enter event 1 ")
        e2 = input("Enter event 2 ")
        e3 = input("Enter event 3 ")
        e4 = input("Enter event 4 ")
        e5 = input("Enter event 5 ")
        e6 = input("Enter event 6 ")
        x = random.choice(Numbers)
        print("Please wait. Rolling the dice for you")
        time.sleep(3)
        if x == 1:
            print(f"The number is {x}")
            print(f"The event is {e1}")
        elif x == 2:
            print(f"The number is {x}")
            print(f"The event is {e2}")
        elif x == 3:
            print(f"The number is {x}")
            print(f"The event is {e3}")
        elif x == 4:
            print(f"The number is {x}")
            print(f"The event is {e4}")
        elif x == 5:
            print(f"The number is {x}")
            print(f"The event is {e5}")
        elif x == 6:
            print(f"The number is {x}")
            print(f"The event is {e6}")
        r = input("Do you want to roll again? (y/n) ")
        while r not in ["y", "n"]:
            print("Invalid input")
            r = input("Do you want to roll again? (y/n) ")
            if r in ["y", "n"]:
                break
        if r != "y":
            break

    elif start == "n":
        print("Please wait. Rolling the dice for you")
        time.sleep(3)
        x = random.choice(Numbers)
        print(f"The number is {x}")
        r = input("Do you want to roll again? (y/n) ")
        while r not in ["y", "n"]:
            print("Invalid input")
            r = input("Do you want to roll again? (y/n) ")
            if r in ["y", "n"]:
                break
        if r != "y":
            break