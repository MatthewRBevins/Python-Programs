print("Welcome to Guess That Number!")
input("(Enter to continue)")
print("Try to guess the number that the computer is thinking of!")
for i in range(1000):
    difficulty = input("Choose the difficulty: 1: pick a number between 1 and 10. 2: 1-20. 3: 1-50. 4: 1-100.")
    if difficulty == "1":
        import random
        higher_value = 10
        lower_value = 1
        final_value = random.randint(lower_value,higher_value)
        print("I'm thinking of a number between one and 10.")
        guess = int(input("What do you think it is? "))
        if guess == final_value:
            print("You got it! The answer was",final_value,"!")
            input("Press enter to play again")
        else:
            print("Sorry. The correct answer was",final_value,".")
            input("Press enter to play again")
    if difficulty == "2":
        import random
        higher_value = 20
        lower_value = 1
        final_value = random.randint(lower_value,higher_value)
        print("I'm thinking of a number between one and 20.")
        guess = int(input("What do you think it is? "))
        if guess == final_value:
            print("You got it! The answer was",final_value,"!")
            input("Press enter to play again")
        else:
            print("Sorry. The correct answer was",final_value,".")
            input("Press enter to play again")
    if difficulty == "3":
        import random
        higher_value = 50
        lower_value = 1
        final_value = random.randint(lower_value,higher_value)
        print("I'm thinking of a number between one and 50.")
        guess = int(input("What do you think it is? "))
        if guess == final_value:
            print("You got it! The answer was",final_value,"!")
            input("Press enter to play again")
        else:
            print("Sorry. The correct answer was",final_value,".")
            input("Press enter to play again")            
    if difficulty == "4":
        import random
        higher_value = 100
        lower_value = 1
        final_value = random.randint(lower_value,higher_value)
        print("I'm thinking of a number between one and 100.")
        guess = int(input("What do you think it is? "))
        if guess == final_value:
            print("You got it! The answer was",final_value,"!")
            input("Press enter to play again")
        else:
            print("Sorry. The correct answer was",final_value,".")
            input("Press enter to play again")
    else:
        print("Sorry. Invalid input. Please type in a number between 1 and 4.")
        input("(Enter to continue)")

