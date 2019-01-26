import sys
go = 1
stop = 0
while go == 1:
    thingy = 0
    dice = input("How many dice? 1 or 2? ")
    if dice == "1":
        import random
        high_value = 6
        low_value = 1
        input("Enter to roll the die!")
        final_value = random.randint(low_value,high_value)
        print("You rolled a " + str(final_value) + "!")
        thingy = 1
        input("Enter to roll again. The program ends after 1000 times.")
    if dice == "2":
        import random
        high_value2 = 6
        low_value2 = 1
        input("Enter to roll the dice!")
        final_value2 = random.randint(low_value2,high_value2)
        final_value3 = random.randint(low_value2,high_value2)
        tot = final_value2 + final_value3
        print("You rolled a " + str(final_value2) + " and a " + str(final_value3) + ", which makes " + str(tot) + "!")
        thingy = 1
    elif thingy == 0:
        input("Be sure to type 1 or 2. Press enter to try again.")
    while stop == 0:
        again = input("Type roll to roll again, type stop to stop ")
        if again == "roll":
            go = 1
            stop = 1
        elif again == "stop":
            print("Ended")
            sys.exit()
        else:
            stop = 0
            print("Type roll or stop")
