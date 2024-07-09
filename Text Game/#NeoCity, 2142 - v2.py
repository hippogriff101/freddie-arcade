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
def lady():
    print("You walk away from the stranger.")
    time.sleep(1)
    print("You see a interesting stall.")
    time.sleep(1)
    print("The sign reads:'PREDICTIONS'")
    time.sleep(1)
    print("You walk inside.")
    time.sleep(1)
    print("'")
    time.sleep(1)
    print("Hello my friiiend")
    time.sleep(1)
    print("In a woorld surrounded with people and gunns and warr and computeers we must seek peace insted of violence!")
    time.sleep(1)
    print("If you spear me a bitcoin then I'll read your future....")
    time.sleep(1)
    print("'")
    time.sleep(1)
    print("It's me, that was quite contrediting.")
    time.sleep(1)
    print("I've sent a bit to your watch where my electrics are housed.")
    time.sleep(1)
    print("Tap me on her card reader.")
    time.sleep(1)
    print("'")
    time.sleep(1)
    print("Thaaannnk youu my friiend, your donnatiooon was mutccch appriciaated....")
    time.sleep(1)
def drone():
    global health
    global marketgames

    dronehealth = 4

    while dronehealth > 0 and health > 0:
        print("You see a drone in the distance...")
        time.sleep(1)
        print("By fighting it you gain a new item but risk losing...")

        time.sleep(1)

        dronefight = input("Do you want to fight the drone? (yes/no): ")
        
        time.sleep(1)

        if dronefight == "yes":
            print("Let the fight begin...")
            time.sleep(1)
            print("You can go about this two ways.")
            time.sleep(1)
            print("Sneak up and take out the drone,")
            time.sleep(1)
            print("Or battle for better loot.")
            time.sleep(1)

            while True:
                dronecho = input("Do you, 'sneak' or 'battle'? : ")
                time.sleep(1)
                if dronecho == "sneak":
                    print("You maneuver behind a stall.")
                    time.sleep(1)
                    print("Slowly, you stalk through the cover of the bright flashing lights of the futuristic billboards.")
                    time.sleep(1)
                    print("Ahead you see the drone, whirring as it scans the passers by.")
                    time.sleep(1)
                    print("Time to aim,")
                    time.sleep(1)
                    shot = int(input("Press '1' to fire: "))
                    if shot == 1:
                        print("CRITICAL HIT!")
                        print("The drone is down to half health")
                        dronehealth -= 2
                        break
                    else:
                        print("You gave away your cover!")
                        time.sleep(1)
                        print("It hits you!")
                        health -= 1
                        time.sleep(1)
                        print("Your health is now at", health)
                        break

                elif dronecho == "battle":
                    print("You charge at the drone!")
                    time.sleep(1)
                    print("It hits you!")
                    health -= 1
                    print("Your health is now at", health)
                    time.sleep(1)
                    shot = int(input("Press '1' to fire at the drone: "))
                    if shot == 1:
                        print("CRITICAL HIT!")
                        print("The drone is down to half health")
                        dronehealth -= 2
                        break
                    else:
                        print("You missed!")
                        time.sleep(1)
                        print("It hits you!")
                        health -= 1
                        time.sleep(1)
                        print("Your health is now at", health)
                        break

                else:
                    print("I'm sorry I don't know that.")

            if dronehealth > 0:
                print("Try to shoot the drone!")
                time.sleep(1)
                shot = int(input("Press '1' to fire: "))
                if shot == 1:
                    print("You HIT!")
                    dronehealth -= 1
                    print("The drone's health is at", dronehealth)
                else:
                    print("You missed!")
                    time.sleep(1)
                    print("It hits you!")
                    health -= 1
                    time.sleep(1)
                    print("Your health is now at", health)
                    time.sleep(1)
                    print("You need to step up your game!")

                print("I'm going to try hacking the drone")
                time.sleep(1)
                print("There is a 50% chance this will work!")
                time.sleep(1)
                hack = "Hacking... \n"
                for i in range(4):
                    for char in hack:
                        print(char, end='', flush=True)
                        time.sleep(0.1)

                dronehack = random.randint(1, 2)
                if dronehack == 1:
                    print("Hack successful!")
                    time.sleep(1)
                    dronehealth = 0
                    print("Drone disarmed")
                    break
                else:
                    print("Hack failed!")
                    time.sleep(1)
                    print("You're on your own.")
                    time.sleep(1)
                    print("Sorry!")
                    time.sleep(1)
                    shot = int(input("Press '1' to fire: "))
                    if shot == 1:
                        print("You HIT!")
                        dronehealth -= 3
                        time.sleep(1)
                        print("The drone's health is at", dronehealth)
                        break
                    else:
                        print("I'm done with you!")
                        time.sleep(1)
                        print("I HIT!")
                        dronehealth = 0
                        time.sleep(1)
                        print("The drone's health is at", dronehealth)
                        break

        elif dronefight == "no":
            print("Alright, let's go a different direction.")
            time.sleep(1)
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
        time.sleep(1)
        print("I'm proud of you!")
        time.sleep(1)
        print("Now your going to get a new item")
        time.sleep(1)
        
        itemrandom = random.choice(itemsgained)
        itemsgained.remove(itemrandom)
        print("You got a", itemrandom)
        time.sleep(1)
        if dronecho == ("battle") and health == 9:
            print("Becasue you beat the drone with your health at nine and chosing the battle path you get another item!")
            time.sleep(1)
            itemrandom = random.choice(itemsgained)
            itemsgained.remove(itemrandom)
            print("You got a", itemrandom)
            time.sleep(1)
        invopen = input("Do you want to open your backpack? (press 'e')")

        if invopen == 'e':
            print(inv)
        else:
            print("Ok then")

        print("")
def npc():
    print("You continue on through the stalls.")
    time.sleep(1)
    print("You see a person in a dark cloak standing near a marque.")
    time.sleep(1)
    while True:
        wnpc = input("Do you (a)Talk to the mysterious person OR (b)Find a stall selling an item your intersted in? (a or b): ")
        time.sleep(1)
        if wnpc == ("a"):
            print("You walk towards the person. You see a glimps of there face.")
            time.sleep(1)
            niceornot = ["nice", "not"]
            wnpcgame = random.choice(niceornot)
            if wnpcgame == "not":
                time.sleep(1)
                gard()
                break
            else:
                print("The man mutters.")
                time.sleep(1)
                print("'")
                time.sleep(1)
                print("Hello,")
                time.sleep(1)
                print("My name is Pablo,")
                time.sleep(1)
                print("If you play my game then you might get something in return.")
                time.sleep(1)
                playagame = input("Do you want to play a game? (yes) OR (no): ")
                time.sleep(1)
                if playagame == ("yes"):
                    print("Yes, goood")
                    time.sleep(1)
                    #FINISH HERE!
                elif playagame == ("no"):
                    print("What...")
                    time.sleep(1)
                    print("What redicule is this.")
                    time.sleep(1)
                    print("'")
                    time.sleep(1)
                    print("It's me, that could have terned sour quickly.")
                    time.sleep(1)
                    print("Lets move on")
                    time.sleep(1)
                    lady()
                    break
        elif wnpc == ("b"):
            lady()
        else:
            print("I'm sorry I don't know that!")

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
    time.sleep(1)
    print("Once you leave here you cant come back until the end of your mission")
    time.sleep(1)
    print("I'm your AI assistant, I will be guiding you through your mission.")
    time.sleep(1)
    print(" I'm sure my programmer gave you the heads up before you woke up here.")
    time.sleep(1)
    print("At points during the mission I will ask you if you want to see your inventry")
    time.sleep(1)

    print("")

    invopen = input("Do you want to open your backpack? (press 'e')")

    time.sleep(1)

    if invopen == 'e':
        print(inv)
    else:
        print("Ok then")

    print("")

    time.sleep(1)

    print("Now you are going to get a random item you can use to complete your task")

    itemrandom = random.choice(itemsgained)
    itemsgained.remove(itemrandom)
    time.sleep(1)
    print("You got a", itemrandom)
    time.sleep(1)
    print("Now your going to go out and escape from this blasted city!")
    time.sleep(1)
    print("Your going to go to The Market.")
    
def market():
    print("Welcome to The Market, you have to navigate through the stalls to find the exit.")
    time.sleep(1)
    while True:

        dir = input("Do you want to go left right or straight? (left, right, straight): ")
        time.sleep(1)
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

    time.sleep(1)

    if marketplot == ("drone"):
        drone()
    elif marketplot == ("npc"):
        npc()
    elif marketplot == ("gard"):
        gard()
    
    print("That was an interesting turn of events.")
    time.sleep(1)
    print("You will become used to the characters you have met or fought just then.")
    time.sleep(1)
    print("Your heading to the underpass now.")
    time.sleep(1) 
               
def underpass():
    print("Welcome to The UnderPass, you have to make a very important desision.")

#The Game:

