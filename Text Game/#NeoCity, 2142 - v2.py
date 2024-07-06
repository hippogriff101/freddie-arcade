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

health = 10

#charcters & more
def loading():
        
        load = ("Loading... \n")
        for i in range(4):
            for char in load:
                print(char, end='', flush=True)
                time.sleep(0.1)

def drone():
    global health
    global marketgames

    dronehealth = 4

    while dronehealth > 0 and health > 0:
        print("You see a drone in the distance...")
        print("By fighting it you gain a new item but risk losing...")

        dronefight = input("Do you want to fight the drone? (yes/no): ").strip().lower()

        if dronefight == "yes":
            print("Let the fight begin...")
            print("You can go about this two ways.")
            print("Sneak up and take out the drone,")
            print("Or battle for better loot.")

            while True:
                dronecho = input("Do you, 'sneak' or 'battle'? : ").strip().lower()
                if dronecho == "sneak":
                    print("You maneuver behind a stall.")
                    print("Slowly, you stalk through the cover of the bright flashing lights of the futuristic billboards.")
                    print("Ahead you see the drone, whirring as it scans the passers by.")
                    print("Time to aim,")
                    shot = int(input("Press '1' to fire: "))
                    if shot == 1:
                        print("CRITICAL HIT!")
                        print("The drone is down to half health")
                        dronehealth -= 2
                        break
                    else:
                        print("You gave away your cover!")
                        print("It hits you!")
                        health -= 1
                        print("Your health is now at", health)
                        break

                elif dronecho == "battle":
                    print("You charge at the drone!")
                    print("It hits you!")
                    health -= 1
                    print("Your health is now at", health)
                    shot = int(input("Press '1' to fire at the drone: "))
                    if shot == 1:
                        print("CRITICAL HIT!")
                        print("The drone is down to half health")
                        dronehealth -= 2
                        break
                    else:
                        print("You missed!")
                        print("It hits you!")
                        health -= 1
                        print("Your health is now at", health)
                        break

                else:
                    print("I'm sorry I don't know that.")

            if dronehealth > 0:
                print("Try to shoot the drone!")
                shot = int(input("Press '1' to fire: "))
                if shot == 1:
                    print("You HIT!")
                    dronehealth -= 1
                    print("The drone's health is at", dronehealth)
                else:
                    print("You missed!")
                    print("It hits you!")
                    health -= 1
                    print("Your health is now at", health)
                    print("You need to step up your game!")

                print("I'm going to try hacking the drone")
                print("There is a 50% chance this will work!")
                hack = "Hacking... \n"
                for i in range(4):
                    for char in hack:
                        print(char, end='', flush=True)
                        time.sleep(0.1)

                dronehack = random.randint(1, 2)
                if dronehack == 1:
                    print("Hack successful!")
                    dronehealth = 0
                    print("Drone disarmed")
                    break
                else:
                    print("Hack failed!")
                    print("You're on your own.")
                    print("Sorry!")
                    shot = int(input("Press '1' to fire: "))
                    if shot == 1:
                        print("You HIT!")
                        dronehealth -= 3
                        print("The drone's health is at", dronehealth)
                        break
                    else:
                        print("I'm done with you!")
                        print("I HIT!")
                        dronehealth = 0
                        print("The drone's health is at", dronehealth)
                        break

        elif dronefight == "no":
            print("Alright, let's go a different direction.")
            dirtwo = random.choice(marketgames)

            if dirtwo == "drone":
                gard()
                break
            elif dirtwo == "npc":
                npc()
                break
            elif dirtwo == "gard":
                gard()
                break

        else:
            print("I'm sorry I don't know that.")

    if dronehealth == 0:
        print("Great job!")
        print("I'm proud of you!")
        print("Now your going to get a new item")
        
        itemrandom = random.choice(itemsgained)
        itemsgained.remove(itemrandom)
        print("You got a", itemrandom)
        if dronecho == ("battle") and health == 9:
            print("Becasue you beat the drone with your health at nine and chosing thye battle path you get another item!")
            itemrandom = random.choice(itemsgained)
            itemsgained.remove(itemrandom)
            print("You got a", itemrandom)
        invopen = input("Do you want to open your backpack? (press 'e')")

        if invopen == 'e':
            print(inv)
        else:
            print("Ok then")

        print("")
def npc():
    print("You continue on through the stalls.")
    print("You see a person in a dark cloak standing near a marque.")
    while True:
        wnpc = input("Do you (a)Talk to the mysterious person OR (b)Find a stall selling an item your intersted in? (a or b): ")
        if wnpc == ("a"):
            print("You walk towards the person. You see a glimps of there face.")
            niceornot = ["nice", "not"]
            wnpcgame = random.choice(niceornot)
            if wnpcgame == "not":
                gard()
                break
            else:
                print("The man mutters.")
                print("'")
                print("Hello,")
                print("My name is Pablo,")
                print("If you play my game then you might get something in return.")
                playagame = input("Do you want to play a game? (yes) OR (no): ")
                if playagame == ("yes"):
                    print("Yes, goood")
                elif playagame == ("no"):
                    print("What...")
                    print("What redicule is this.")
                    print("'")
                    print("It's me, that could have terned sour quickly.")
                    print("Lets move on")
                    drone()
                    break
        elif wnpc == ("b"):
            print("You walk away from the stranger.")
            print("You see a interestinmg stall.")
            print("The sign reads:'PREDICTIONS'")
            print(" You inside.")
            print("'")
            print("Hello my friiiend")
            print("In a woorld surrounded with people and gunns and warr and computeers we must seek peace insted of violence!")

def gard():
    print("A man leaps out to reval gard uniform!")
    gardact = ["bag", "shoot"]
    action = random.choice(gardact)
    if action == ("bag"):
        print("The gard pulls out a bag and chucks it over your head.")
        fightorflight = input("You can fight or let it be? (fight) or (flight): ")
        if fightorflight == (""):
            print("")
    


#rooms
def hideout():

    print("Welcome to your hideout, this is your control center.")
    print("Once you leave here you cant come back until the end of your mission")
    print("I'm your AI assistant, I will be guiding you through your mission.")
    print(" I'm sure my programmer gave you the heads up before you woke up here.")

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
               
def underpass():
    print("Welcome to The UnderPass, you have to make a very important desision.")

