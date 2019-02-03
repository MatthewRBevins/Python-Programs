again = 0
askAgain = 0
rightinput = 0
import sys
print("Welcome to MSGUY's Python Calculator")
input("(Enter to begin!)")
while again == 0:
    print("Choose a math operation")
    print("Type 1 to add")
    print("Type 2 to subtract")
    print("Type 3 to multiply")
    print("Type 4 to divide")
    while rightinput == 0:
        choice = input("Choose number (1, 2, 3, or 4)")
        num1 = float(input("What is the first number? "))
        num2 = float(input("What is the second number? "))
        if choice == "1":
            rightinput = 1
            added = num1 + num2
            print(str(added))
        elif choice == "2":
            rightinput = 1
            subtracted = num1 - num2
            print(str(subtracted))
        elif choice == "3":
            rightinput = 1
            multiplied = num1 * num2
            print(str(multiplied))
        elif choice == "4":
            rightinput = 1
            if num1 == 0:
                if num2 == 0:
                    import random
                    low = 1
                    high = 3
                    total = random.randint(low,high)
                    if total == 1:
                        print("Please Restart Your Computer")
                    if total == 2:
                        print("CHANCE TIME!")
                        input("Enter to continue")
                        print("You lose!",divide(0,0))
                    if total == 3:
                        print("You just won...")
                        input("Enter to continue")
                        print("A brand new 3 of hearts playing card! It will be sent to you on February 23, 3672! What a deal!")
                 else:
                    print("0")

            else:
                divided = num1 / num2
                print(str(divided))
        else:
            rightinput = 0
    
    input("(Enter to play again)")
            
        
    

        

        
              
