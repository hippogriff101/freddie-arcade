#NeoCity, 2142

#I need:
import random
import time

#Main Variables
rooms = ["Your Hideout", "The Market", "The Underpass", "The Mainframe", "The Exit"]

itemsgained = ["Map", "Keycard", "Energy Drink", "Smoke Bomb", "Laser Cutter", "Hoverboard"]

itemsneeded = ["AI Assistant", "Blaster"]

items = [itemsgained, itemsneeded]

inv = [itemsneeded,]

marketgames = ["drone", "npc", "gard"]

health = (10)

#charcters & more
def loading():
        
        load = ("Loading... \n")
        for i in range(4):
            for char in load:
                print(char, end='', flush=True)
                time.sleep(0.1)

def drone():

    print("You see a drone in the distance...")
    print("By fighting it you gain a new item but risk losing...")
    while True:
        dronefight = input("Do you want to fight the drone? (yes/no): ")
        if dronefight == ("yes"):
            print("let the fight begin")
            #fight logic here
            continue
        elif dronefight == ("no"):
            print("Alright let's go a differant direction.")
        
            dirtwo = random.choice(marketgames)

            if dirtwo == ("drone"):
                gard()
                break
            elif dirtwo == ("npc"):
                npc()
                break
            elif dirtwo == ("gard"):
                gard()
                break

def npc():
    print("NEED TO FINISH!")

def gard():
    print("NEED TO FINISH!")
#rooms
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
    
def market():
    print("Welcome to The Market, you have to navigate through the stalls to find the exit.")

    while True:

        dir = input("Do you want to go left right or straight? (left, right, straight): ")

        if dir == ("left"):
            print("You choose left.")
            break
        elif dir == ("right"):
            print("You choose right.")
            break
        elif dir == ("straight"):
            print("You choose straight.")
            break
        else:
            print("I'm sorry I dont know that?")

    marketplot = random.choice(marketgames)


    if marketplot == ("drone"):
        drone()
    elif marketplot == ("npc"):
        npc()
    elif marketplot == ("gard"):
        gard()
    
    print("TEST!")
     
