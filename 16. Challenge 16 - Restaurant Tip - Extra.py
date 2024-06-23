import time

text = ("Please wait while I calculate...")

while True:

    cost = float(input("What is the cost of dinner? £"))

    time.sleep(0.5)

    people = int(input("How mny people are eating with you? "))

    time.sleep(1)

    print("You want to share the bill eqaly and tip 15%. ")

    time.sleep(1)

    print("")

    time.sleep(1)

    for i in range(1):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.1)

            print(" ")

    time.sleep(3)

    tip = cost*0.15

    finalcost = tip + cost

    perperson = finalcost/people

    print("")


    print("Thank you for waiting...")
    print("")
    time.sleep(1)
    print(f"Your final bill, with tip, is £{finalcost:.2f}")
    print("")
    time.sleep(1)

    print(f"That is £{perperson:.2f} split evenly per person.")
    print("")
    break