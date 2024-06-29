#NeoCity, 2142

rooms = ["Your Hideout", "The Market", "The Underpass", "The Mainframe", "The Exit"]

itemsgained = ["Map", "Keycard", "Energy Drink"]

itemsneeded = ["AI Assistant", "Blaster"]

items = [itemsgained, itemsneeded]

inv = [itemsneeded,]

def hideout():
    print("Welcome to your hideout, this is your control center.")
    print("Once you leave here you cant come back until the end of your mission")
    print("I'm your AI assistant, I will be guiding you through your mission.")
    print(" I'm sure my programmer gave you the heads down before you woke up here.")

    print("At points during the mission I will ask you if you want to see your inventry")

    invopen = input("Do you want to open your backpack? (press 'e')")

    if invopen == 'e':
        print(inv)

    print("Now you are going to get a random item you can use to complete your task")

