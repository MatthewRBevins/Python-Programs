
next = 0
print("Welcome to mean calculator on Python!")
input("(ENTER)")
print("Enter at least two numbers, and this program will give you the average!")
input("Enter to start the program!")
while next == 0:
    i = 1
    numbers = [];
    print(numbers)
    number = input("number: ")
    print(numbers)
    numbers.append(float(number))
    print(numbers)
    while i == 1:
        number = input("number: ")
        numbers.append(float(number))
        print(numbers)
        b = input("are those all your numbers? (y/n)")
        if b == "y":
            i = 2
        elif b == "n":
            i = 1
    added = sum(numbers)
    print(str(added))
    hi = len(numbers)
    average = added / hi
    print("Your average is " + str(average) + "!")
    next = input("Would you like to do another average? (y/n) ")
    if next == "n":
        next = 1
    if next == "y":
        next = 0
    else:
        next = 1
    greatest.numbers
