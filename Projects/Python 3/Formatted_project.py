# DECI Adventure Game Project.
# Modules import
import time
import random

name = input("Enter your name:- ")
print(f"Hello {name}")
# --------------------------------------------------------------------------------------------
# Lists and randomness
adjectives = ["a wide", "a free", "an open"]
adj = random.choice(adjectives)

villains = ["dragon", "vampire", "zombie", "pirate", "witch", "pigmy"]
v = random.choice(villains)

colours = ["blue", "yellow", "red", "pink", "black", "white"]
c = random.choice(colours)

losing_statements = ["Bad luck! you lost", "unfortunately! you lost"]
l = random.choice(losing_statements)

murderers = ["vampire", "zombie", "pirate", "pigmy"]
r_m = random.choice(murderers)

winning_statement = ["Good game! you win!", "Victory!"]
w = random.choice(winning_statement)
# --------------------------------------------------------------------------------------------
def print_pause(output):
    """Prints some text and stops 2.5 seconds"""
    print(output)
    time.sleep(2.5)


def update_score(value):
    """Takes an argument value and adds it to the score"""
    global score
    score += value
    return score


def run():
    """The user run choice for the first time"""
    print_pause("You run back into the field.")
    print_pause("Fortunately, you don't have been followed.")


def run_again_before_cave():
    """The user run choice for second time before he enters the cave"""
    print_pause("You run back into the field.")
    print_pause("Unfortunately, you have been followed this time.")
    print_pause("After a long run, he catches you!")
    print_pause(f"The {v} takes you to his house!")
    if v in murderers:
        print_pause(f"Then {v} kills you")
    elif v == "witch":
        print_pause("The witch turns you into a frog")
    elif v == "dragon":
        print_pause("The dragon uses you as food")


def run_again_after_cave():
    """The user run choice for second time after he enters the cave"""
    print_pause("You run back into the field.")
    print_pause("Unfortunately, you have been followed this time.")
    print_pause("After a long run both of you are tired")
    print_pause("Now both of your are trapped in a building")
    print_pause(f"The {v} move to take action against you")
    print_pause("The rod of Ogoroth shines suddenly!")
    print_pause(f"The {v} is hit by a lightning strike which led him to death")


def enter_cave():
    """The user enters the cave"""
    print_pause("You enter carefully the cave.")
    print_pause("It appears to be only a very small cave.")
    print_pause("You see a shine of metal near a rock.")
    print_pause("You have found the magical rod of Ogoroth!")
    print_pause("You leave your old magic rod and take the rod of Ogoroth.")
    print_pause("You walk back to the area")


def enter_cave_again():
    """The user enters the cave for the second time"""
    print_pause("You have been here before")
    print_pause("The cave is empty now")
    print_pause(f"You turn around to exit the cave when you see the {v}")
    print_pause(f"The {v} moves to attack you")
    print_pause("but his attacks is no match for Ogoroth rod")
    print_pause("You cast a stronger spell")
    print_pause(f"The {v} lays dead with the effect of Ogoroth rod")


def ring_bell_before_cave():
    """The user rings the bell before he enters the cave"""
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to ring when the door opens and out steps a {v}")
    print_pause(f"Opps! This is the {v}'s house!")
    print_pause(f"The {v} sees you!")
    print_pause("You are in trouble now!")
    print_pause("You feel not all set for that, as having a, rusty old magic rod.")


def ring_bell_again_before_cave():
    """The user rings the bell before he enters the cave for the second time"""
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to ring when the door opens and out steps a {v}")
    print_pause(f"Opps! This is the {v}'s house!")
    print_pause(f"The {v} sees you!")
    print_pause("You are in trouble now!")
    print_pause(f"The {v} attacks you due to annoying him")
    print_pause("You lay dead with effect of the attack")


def ring_bell_after_cave():
    """The user rings the bell for the first time after he exits the cave"""
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to ring when a {v} steps out")
    print_pause("Opps! this is his house")
    print_pause("He sees you!")


def ring_bell_again_after_cave():
    """The user rings the bell for the second time after he exits the cave"""
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to ring when a {v} steps out")
    print_pause("Opps! this is his house")
    print_pause("He sees you!")
    print_pause("He tries to attack you ")
    print_pause("You tackle his attack well")
    print_pause("You give him a stronger attack")
    print_pause("He dies because of your strong attack")


def cast_a_spell_before_cave():
    """The user tries to cast a spell before he enters the cave"""
    print_pause("Good job! you do your best.")
    print_pause(f"but your old magic wand is no match for the {v}")
    if v in murderers:
        print_pause(f"so the {v} kills you")
    elif v == "witch":
        print_pause("The witch turns you into a frog")
    elif v == "dragon":
        print_pause("The dragon uses you as food")


def cast_a_spell_after_cave():
    """The user tries to casts a spell after he enters the cave"""
    print_pause(f"The {v} moves to cast a spell")
    print_pause("you raise your new rod of Ogoroth.")
    print_pause("The rod shines in your hand as you brace yourself to the spell.")
    print_pause("He looks at the shiny rod of ogoroth")
    print_pause("He runs escaping")
    print_pause("Great job! you rid the village of the evil")


def beginning():
    """The game start"""
    print_pause("the game ends when you reach the following goal")
    print_pause("The goal is:- rid the village of the evil by anyway")
    print_pause(f"You find yourself in an open area, full of grass and {c} flowers.")
    print_pause(f"Rumors say that a {v} is present nearby")
    print_pause("It has been scaring the nigh village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand is a trusty weak old magic rod.")


# ------------------------------------------------------------------------------------------------
time.sleep(1)
print("Starting the game...")
time.sleep(1.5)
print("Please wait...")
time.sleep(3.5)
while True:
    score = 0
    valid_inputs = ["1", "2"]
    # Valid_inputs list to validate numeric inputs
    play_agian_choice = ["y", "n"]
    # Play_again_choice list to validate the play_again input
    beginning()
    c1 = input("Would you like to ring bell (1) or enter cave (2)? ")
    # User first choice
    while c1 not in valid_inputs:
        # User first choice validation
        print("Invalid input")
        c1 = input("Would you like to ring bell (1) or enter cave (2)? ")
        if c1 in valid_inputs:
            break
            # Break statement to exit the infinity loop
    if c1 == "1":
        ring_bell_before_cave()
        print(f"The score now is {update_score(-5)}")
        c2_1 = input("would you like to cast a spell(1) or run(2)? ")
        # User second choice
        while c2_1 not in valid_inputs:
            # User second choice validation
            print_pause("Invalid input")
            c2_1 = input("would you like to cast a spell(1) or run(2)? ")
            if c2_1 in valid_inputs:
                break
                # Break statement to exit the infinity loop
        if c2_1 == "1":
            cast_a_spell_before_cave()
            print(f"The score now is {update_score(-5)}")
            print_pause(l)
            # The user lost
            play_again = input("Do you want to play again? ").lower()
            # Asking the user if he wants to play again
            while play_again not in play_agian_choice:
                # Play_again validation
                print_pause("Invalid input")
                play_again = input("Do you want to play again? ").lower()
                if play_again in play_agian_choice:
                    break
            if play_again != "y":
                break
                # Break statement to exit the loop if the user don't want to play again

        elif c2_1 == "2":
            run()
            print(f"The score now is {update_score(5)}")
            c3_1 = input("Would you like to ring bell (1) or enter cave (2)? ")
            # The user third choice
            while c3_1 not in valid_inputs:
                # The user third choice validation
                print_pause("Invalid input")
                c3_1 = input("Would you like to ring bell (1) or enter cave (2)? ")
                if c3_1 in valid_inputs:
                    break
            if c3_1 == "1":
                ring_bell_again_before_cave()
                print(f"The score now is {update_score(-5)}")
                # lose
                print_pause(l)
                play_again = input("Do you want to play again? ").lower()
                # Play again option
                while play_again not in play_agian_choice:
                    # play again validation
                    print_pause("Invalid input")
                    play_again = input("Do you want to play again? ").lower()
                    if play_again in play_agian_choice:
                        break
                if play_again != "y":
                    break

            elif c3_1 == "2":
                enter_cave()
                print(f"The score now is {update_score(5)}")
                c4_1 = input("Would you like to ring bell (1) or enter cave (2)? ")
                # User fourth choice
                while c4_1 not in valid_inputs:
                    # The choice validation
                    print_pause("Invalid input")
                    c4_1 = input("Would you like to ring bell (1) or enter cave (2)? ")
                    if c4_1 in valid_inputs:
                        break
                if c4_1 == "1":
                    ring_bell_again_after_cave()
                    print(f"The score now is {update_score(5)}")
                    # win
                    print_pause(w)
                    play_again = input("Do you want to play again? ").lower()
                    while play_again not in play_agian_choice:
                        print_pause("Invalid input")
                        play_again = input("Do you want to play again? ").lower()
                        if play_again in play_agian_choice:
                            break
                    if play_again != "y":
                        break
                elif c4_1 == "2":
                    enter_cave_again()
                    print(f"The score now is {update_score(5)}")
                    # win
                    print_pause(w)
                    play_again = input("Do you want to play again? ").lower()
                    while play_again not in play_agian_choice:
                        print_pause("Invalid input")
                        play_again = input("Do you want to play again? ").lower()
                        if play_again in play_agian_choice:
                            break
                    if play_again != "y":
                        break

    elif c1 == "2":
        enter_cave()
        print(f"The score now is {update_score(5)}")
        c2_2 = input("Would you like to ring bell (1) or enter cave (2)? ")
        while c2_2 not in valid_inputs:
            print_pause("Invalid input")
            c2_2 = input("Would you like to ring bell (1) or enter cave (2)? ")
            if c2_2 in valid_inputs:
                break
        if c2_2 == "1":
            ring_bell_after_cave()
            print(f"The score now is {update_score(5)}")
            c3_2 = input("Would you like to cast a spell(1) or run(2)? ")
            while c3_2 not in valid_inputs:
                print_pause("Invalid input")
                c3_2 = input("Would you like to cast a spell(1) or run(2)? ")
                if c3_2 in valid_inputs:
                    break
            if c3_2 == "1":
                cast_a_spell_after_cave()
                print(f"The score now is {update_score(5)}")
                # win
                print_pause(w)
                play_again = input("Do you want to play again? ").lower()
                while play_again not in play_agian_choice:
                    print_pause("Invalid input")
                    play_again = input("Do you want to play again? ").lower()
                    if play_again in play_agian_choice:
                        break
                if play_again != "y":
                    break
            elif c3_2 == "2":
                run()
                print(f"The score now is {update_score(-5)}")
                c4_2 = input("Would you like to ring bell (1) or enter cave (2)? ")

                while c4_2 not in valid_inputs:
                    print_pause("Invalid input")
                    c4_2 = input("Would you like to ring bell (1) or enter cave (2)? ")
                    if c4_2 in valid_inputs:
                        break

                if c4_2 == "1":
                    ring_bell_again_after_cave()
                    print(f"The score now is {update_score(-5)}")
                    # win
                    print_pause(w)
                    play_again = input("Do you want to play again? ").lower()
                    while play_again not in play_agian_choice:
                        print_pause("Invalid input")
                        play_again = input("Do you want to play again? ").lower()
                        if play_again in play_agian_choice:
                            break
                    if play_again != "y":
                        break

                elif c4_2 == "2":
                    enter_cave_again()
                    print(f"The score now is {update_score(5)}")
                    # win
                    print_pause(w)
                    play_again = input("Do you want to play again? ").lower()
                    while play_again not in play_agian_choice:
                        print_pause("Invalid input")
                        play_again = input("Do you want to play again? ").lower()
                        if play_again in play_agian_choice:
                            break
                    if play_again != "y":
                        break

        elif c2_2 == "2":
            enter_cave_again()
            print(f"The score now is {update_score(5)}")
            # win
            print_pause(w)
            play_again = input("Do you want to play again? ").lower()
            while play_again not in play_agian_choice:
                print_pause("Invalid input")
                play_again = input("Do you want to play again? ").lower()
                if play_again in play_agian_choice:
                    break
            if play_again != "y":
                break