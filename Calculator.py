print("Welcome to Matthew's Python Calculator")
input("(Enter to begin!)")
for i in range(1000):
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    print("Choose a math operation")
    print("Press one to add")
    print("Press two to subtract")
    print("Press three to multiply")
    print("Press four to divide")
    choice = input("Choose number (1, 2, 3, or 4)")
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))
    if choice == "1":
        print(num1,"+",num2,"=",add(num1,num2))
        input("(Enter to continue)")
    if choice == "2":
        print(num1,"-",num2,"=",subtract(num1,num2))
        input("(Enter to continue)")
    if choice == "3":
        print(num1,"*",num2,"=",multiply(num1,num2))
        input("(Enter to continue)")
    if choice == "4":
        if num1 == 0:
            if num2 == 0:
                import random
                low = 1
                high = 3
                total = random.randint(low,high)
                if total == 1:
                    print("Don't knock my smock or I'll clean your clock!")
                if total == 2:
                    print("CHANCE TIME!")
                    input("Enter to continue")
                    print("You lose!",divide(0,0))
                if total == 3:
                    print("You just won...")
                    input("Enter to continue")
                    print("A brand new 3 of hearts playing card! It will be sent to you on February 23, 3672! What a deal!")
                    
        else:
            print(num1,"/",num2,"=",divide(num1,num2))
        input("(Enter to continue)")
        
    

        

        
              
