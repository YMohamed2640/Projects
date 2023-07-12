import time
import random

min_input = range(5 , 1001, 5)

gifts = ["JEEP car", "PS5", "Ferarri car", "Lamporghini car", "5 million pounds",
         "Villa", "Mercedes G-Class", "Journey", "BMW X6", "Palace"]

valid_start = ["log in", "create account", "1", "2"]

valid_operation =   ["1", "2", "3", "4", "5", "6", "7",
            "deposit", "withdraw", "donate", "exit",
            "create visa", "delete account", "update visa"]

print("Hello to the bank app.")
time.sleep(1)
print("Starting the app...")
print("please wait...")
time.sleep(3)

while True:
    print("1. Create account.")
    print("2. Log in.")
    start = input("Enter action: ")

    if start == "create account" or start == "1":
        name = input("please Enter your name: ")
        age = int(input("Please enter your age: "))
        balance = input("Please enter starting balance. ")
        if age < 18:
            print("You are not allowed to create an account.")
            break
        else:
            pass
        password = input("Please enter password: ")
        with open("accounts.txt", "a") as info:
            info.write("name: " + name + "\n")
            info.write(f"age: {age} \n")
            info.write("balance: " + balance + "\n")
            info.write("password: " + password + "\n")
            info.write("\n")
        print("Accont created successfully.")

    elif start == "log in" or start == "2":
        file = open("accounts.txt", "r")
        a_info = file.read()
        a_name = input("please enter you name. ")
        while a_name not in a_info:
            print("Account is not available.")
            a_name = input("please enter account name. ")
            if a_name in a_info:
                break

        a_password = input("please enter your password. ")
        while a_password not in a_info:
            print("wrong password.")
            a_password = input("Please try again. ")
            if a_password in a_info:
                break
        print("logging you in. please wait..")
        time.sleep(3.5)
        print("You are now logged in")

    print("1. Deposit.")
    time.sleep(1)
    print("2. Withdraw.")
    time.sleep(1)
    print("3. Donate.")
    time.sleep(1)
    print("4. Create visa")
    time.sleep(1)
    print("5. Delete acoount")
    time.sleep(1)
    print("6. Update visa")
    time.sleep(1)
    print("7. Exit")
    time.sleep(1)
    print("-----------------------")
    operation = input("Enter operation:-").lower()
    while operation not in valid_operation:
        print("Invalid operation")
        operation = input("Enter operation:-")
        if operation in valid_operation:
            break

    if operation == "deposit" or operation == "1":
        d_value = input("Enter value: ")
        time.sleep(3)
        print(f"{d_value} dollars is transferred to your bank account.")


    elif operation == "withdraw" or operation == "2":
        w_money = input("Enter amount of money")
        time.sleep(3)
        print(f"{w_money} dollars is transferred to your paypal account")


    elif operation == "donate" or operation == "3":
        min_value = int(input("Enter a min value greater than 5: "))
        while min_value not in min_input:
            print("Invalid input")
            min_value = int(input("Enter a min value greater than 5: "))
            if min_value in min_input:
                break

        max_value = int(input("Enter max value: "))
        while max_value not in min_input:
            print("Invalid input")
            max_value = input("Enter max value: ")
            if max_value in min_input:
                break

        while max_value <= min_value:
            max_value = int(input("please enter max value greater than 5 "))
            if max_value > min_value:
                break

        r_value = random.randrange(min_value, max_value, step=5)
        print(f"The value is {r_value}")

        x = int(input("Enter number of gifts: "))
        while x > 3:
            print("Too many gifts is not allowed")
            x = int(input("Enter number of gifts: "))
            if x <= 3:
                break
            
        random_gift = random.choices(gifts, k = x)
        print(random_gift)


    elif operation == "create visa" or operation == "4":
        v_pass = input("Please enter password")
        time.sleep(2)
        print("Please head to the bank to recieve your visa")


    elif operation == "delete account" or operation == "5":
        print("do you really wish to delete your account?")
        submit = input("y/n").lower()
        while submit not in ["y", "n"]:
            print("Invalid input")
            submit = input("Do you want to start again? (y/n) ")
            if submit in ["y", "n"]:
                break
        if submit == "y":
            print("your account is deleted successfully")
            time.sleep(1)
            print("Please head to the bank to take your money")


    elif operation == "update visa" or operation == "6":
        print("Please enter your visa number: ")
        visa_num = input("")
        print("Please enter your password: ")
        visa_pass = input("")
        time.sleep(3)
        print("Your visa was updated successfully")
        print("Please head to the bank to recieve the new visa")


    elif operation == "exit" or operation == "7":
        break


    restart = input("Do you want to start again? (y/n) ")
    while restart not in ["y", "n"]:
        print("Invalid input")
        restart = input("Do you want to start again? (y/n) ")
        if restart in ["y", "n"]:
            break

    if restart != "y":
        print("Thanks for choosing our bank")
        time.sleep(1)
        print("Exiting the app")
        time.sleep(2)
        break