import sys

print("***WELCOME TO BINARY CONVERTER!***")
print("NOTE: Please enter a positive integer for converting base 10 to binary.")
while 1 == 1:
    choice = int(input("Enter 1 for base 10 to binary and 2 for binary to base 10: "))
    #Base 10 to binary:
    if choice == 1:
        number = int(input("ENTER YOUR BASE 10 NUMBER: "))
        #These numbers may not work with the algorithm
        if number == 1:
            final = "01"
            print(str(number) + " IN BINARY: " + final)
        elif number == 0:
            final = "00"
            print(str(number) + " IN BINARY: " + final)
        else:
            i = 2
            j = 1
            #find the largest power of 2 just below the number entered
            while 1 == 1:
                if number > i:
                    i = i * 2
                else:
                    if i != number:
                        i = i / 2
                    break
                j = j + 1
            currentNum = i
            final = "01"
            #Iterate through each power of 2
            while 1 == 1:
                #increase the power of 2
                i = i / 2
                #If the current number added to the current power of 2 is not more than the number inputted, add a 0
                if currentNum + i <= number:
                    final = final + "1"
                    currentNum = currentNum + i
                #Otherwise, add a 0
                else:
                    final = final + "0"
                #Stop the loop when i has reached 1
                if i == 1:
                    break
            print(str(number) + " IN BINARY: " + final)
    #Binary to base 10:
    elif choice == 2:
        number = input("ENTER YOUR BINARY NUMBER: ")
        i = 1
        j = 1
        currentNum = 0
        #Go through every number in the inputted binary number
        while j < len(number):
            #If the number is 1, add it to the current total
            if number[len(number)-j:len(number)-(j-1)] == "1":
                currentNum = currentNum + i
            j = j + 1
            #increase the current power of 2
            i = i * 2
        print(number + " IN BASE 10: " + str(currentNum))

        
    end = input("type 'end' to end the program, type anything else to keep going: ")
    if end == "end":
        sys.exit()
