#NeoCity, 2142

import random
import time

rooms = ["Your Hideout", "The Market", "The Underpass", "The Mainframe", "The Exit"]

itemsgained = ["Map", "Keycard", "Energy Drink", "Smoke Bomb", "Laser Cutter", "Hoverboard"]

itemsneeded = ["AI Assistant", "Blaster"]

items = [itemsgained, itemsneeded]

inv = [itemsneeded,]

def hideout():

    print("Welcome to your hideout, this is your control center.")
    print("Once you leave here you cant come back until the end of your mission")
    print("I'm your AI assistant, I will be guiding you through your mission.")
    print(" I'm sure my programmer gave you the heads down before you woke up here.")

    print("At points during the mission I will ask you if you want to see your inventry")

    print("")

    invopen = input("Do you want to open your backpack? (press 'e')")

    if invopen == 'e':
        print(inv)
    else:
        print("Ok then")

    print("")

    print("Now you are going to get a random item you can use to complete your task")

    itemrandom = random.choice(itemsgained)
    itemsgained.remove(itemrandom)
    print("You got a", itemrandom)

    print("Now your going to go out and escape from this blasted city!")

    avaliblerooms = ("Market", "Underpass")

    nextroom = random.choice(avaliblerooms)

    print("Your going to go to the", nextroom)
   
def loading():
        
        load = ("Loading... \n")
        for i in range(4):
            for char in load:
                print(char, end='', flush=True)
                time.sleep(0.1)

hideout()
