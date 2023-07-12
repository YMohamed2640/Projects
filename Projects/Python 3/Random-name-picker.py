# Random name picker
import random

while True:
    my_list = []
    no_of_names = int(input("Enter number of names: "))
    for i in range(no_of_names):
        x = input("Enter name: ")
        my_list.append(x)

    x = random.choice(my_list)
    print(f"The name is {x}")
    r = input("Do you want to restart the app? (y/n) ")
    while r not in ["y", "n"]:
        print("Invalid input")
        r = input("Do you want to restart the app? (y/n) ")
        if r in ["y", "n"]:
            break
    if r != "y":
        break