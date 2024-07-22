import random
import time

# Possible choices
guesses = ["rock", "paper", "scissors"]

print("Hello World!")
time.sleep(1)
print("Do you want to play rock, paper, scissors?")
time.sleep(1)
print("Well you don't actually have a say.")
time.sleep(1)
print("Alright, if you want to be sure I'm not cheating look at the code...")
time.sleep(1)

# Initialize scores
user_score = 0
computer_score = 0

while True:
    print("\nROCK")
    time.sleep(0.5)
    print("PAPER")
    time.sleep(0.5)
    print("SCISSORS")
    time.sleep(0.5)
    print("SHOOT!!!")
    time.sleep(0.1)

    # Get user choice and validate input
    while True:
        cho = input("\nWHAT DO YOU PICK? (rock, paper, scissors): ").lower()
        if cho in guesses:
            break
        else:
            print("Invalid choice, please try again.")

    # Get computer choice
    compcho = random.choice(guesses)
    time.sleep(1)
    print("\nI choose", compcho)
    time.sleep(1)

    # Determine the winner
    if cho == compcho:
        print("We chose the same thing! It's a tie!")
        user_score += 1
        computer_score += 1
    elif (cho == "rock" and compcho == "scissors") or \
         (cho == "scissors" and compcho == "paper") or \
         (cho == "paper" and compcho == "rock"):
        print("Oh shucks, you win.")
        user_score += 1
    else:
        print("I guess... you loooooosseeeeee!!!!!!!!!!!")
        computer_score += 1

    # Display current scores
    time.sleep(1)
    print(f"\nCurrent Scores: You - {user_score}, Computer - {computer_score}")
    time.sleep(1)

    # Ask if the user wants to play again
    while True:
        play = input("\nDo you want to play again? (yes/no): ").lower()
        if play in ["yes", "no"]:
            break
        else:
            print("I don't understand that. Please type 'yes' or 'no'.")

    if play == "no":
        break

# Final message
print("\nThank you for playing! Final Scores: You -", user_score, ", Computer -", computer_score)
time.sleep(1)
