import random
import time

text = ("shaking.... \n")
 
answer1=("Absolutely!")
answer2=("Yes...")
answer3=("Go for it tiger.")

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
    
    choice=random.randint(1,3)

    time.sleep(2)


    if choice == 1:
        answer=answer1
    elif choice == 2:
        answer=answer2
    else:
        answer=answer3


    for i in range(1):
            for char in answer:
                print(char, end='', flush=True)
                time.sleep(0.1)
            print("")

#GAME ON!





while True:

    print(game())

    print("")
     
    tryagain = input("Type 'y' to play again and anything to stop ")

    print("")

    if tryagain == ("y"):
        print("Alright lets go again!")
        continue

    else:
        print("Bye then...")
        print("")
        break
                
    