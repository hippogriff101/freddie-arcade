import random
import time


while True:
    
    topvalue = 99
    attempts = 0
    dice = random.randint(1,topvalue)

    while True:
        guess = int(input("I am thinking of a number between 1 and 99? What do you think it is? "))

        time.sleep(1)

        if guess == dice:
                print ("You Win!")
                time.sleep(1)
                print("You took", attempts ,"attempts to get the correct number!")
                time.sleep(1)
                print("Bye the...\n\n")
                break
        elif guess > (topvalue * 2):
                print("OOPS!")
                time.sleep(1)
                print("WAAAAAAAAY too high")
                attempts += 1
        elif guess > dice:
                print ("Too High")
                attempts += 1
        elif guess < dice:
                print ("Too Low")
                attempts += 1

