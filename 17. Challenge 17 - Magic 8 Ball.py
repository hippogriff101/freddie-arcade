#import
import random
import time

#Starting Code
text = ("shaking.... \n")
answers = ["Yes.", "No.", "Absolutely!", "No waaaayyy!"]

#the games code
def game():
        
    print("")
    print("Welcome to the Magic 8 Ball game—use it to answer your questions...")
    time.sleep(1)
    print("Ask me for any advice and I’ll help you out.")
    time.sleep(1)
    question = input("Type in your question and then press 'Enter' for an answer: ")

    print("")
    

    for i in range(4):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.1)

            print(" ")
    
    choice=random.randint(1,4)

    time.sleep(2)


    choice = random.choice(answers)


    for i in range(1):
            for char in choice:
                print(char, end='', flush=True)
                time.sleep(0.1)
            print("")

#Game Ending
while True:

    game()

    print("")

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Bye then...")
        print("")
        break
                
    
