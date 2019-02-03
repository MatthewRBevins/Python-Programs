#Some code from Python.org
#Some code from StackOverflow.com
#This is a work-in-progress
#First variables:
mainvar = 1
tasdfasfdhjasdhfkjashdfk = 2
while tasdfasfdhjasdhfkjashdfk == 2:
    #Variables called in this loop:
    typee = 0
    x = 1
    n = 2.1
    rwethereyet = 1
    wait = 1
    tingytwo = 1
    mrb = 1
    choice = 0
    #Imports modules
    from fractions import Fraction
    from decimal import Decimal, ROUND_UP
    import random
    import sys
    #Intro:
    print("Welcome to Linear Equation Calculator! Made by MSGUY in Python 3.")
    input("(Enter)")
    print("Formula Finder: Instead of doing all the math to turn a line into an equation, just choose an equation and know two points on the line.")
    input("(Enter)")
    print("Or, you can choose converter, and convert one equation type to another type of equation. Information inputs very depending on the type of equation.")
    input("(Enter)")
    print("Fullscreen mode works best.")
    input("(Enter)")
    print("In some cases, the program will print things that should've been simplified, like 4/2 to 2. I am working on fixing this, but for now you will have to simplify on your own.")
    input("(Enter)")
    #Type of calculator choice
    while mainvar == 1:
        wait = 1
        typee = 0
        x = 1
        n = 2.1
        rwethereyet = 1
        wait = 1
        tingytwo = 1
        mrb = 1
        tingytwo = 1
        while wait == 1:
            choice = input("Please choose a type of calculator. c for converter and f for formula finder. ")
            if choice == "c" or choice == "f":
                wait = 2
        #Formula finder start
        if choice == "f":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Welcome to Python Linear Equation Formula Finder!")
            input("(Enter)")
            print("Note: If you do not answer in numbers for certain questions, the program will not work.")
            input("(Enter)")
            print("Let M represent the slope of the equation, and let B represent the y-intercept.")
            input("(Enter)")
            #Equation choice
            while x == 1:
                y =input("Which kind of equation? 1 for slope intercept (y = mx + b), 2 for point slope (y - y1 = m(x - x1)), or 3 for standard (Ax + By = C). ")
                if y == "1":
                    typee = 1
                    x = 2
                    print("y = mx + b")
                if y == "2":
                    typee = 2
                    x = 2
                    print("y - y1 = m(x - x1)")
                if y == "3":
                    typee = 3
                    x = 2
                    ("Ax + By = C")
            #Integer choice- are numbers not decimals?
            while rwethereyet == 1:
                integer = input("Are all your coordinate points integers (no decimal places)? Please answer 1(yes) or 2(no). ")
                if integer == "1":
                    print((str(integer)))
                    rwethereyet = 2
                    integer = 1
                elif integer == "2":
                    print((str(integer)))
                    integer = 2
                    rwethereyet = 2
                else:
                    rwethereyet = 1
            #Enter line coordinates
            if integer == 1:
                xone = int(input("What is the first X value? "))
                yone = int(input("What is the first Y value? "))
                xtwo = int(input("What is the second X value? "))
                ytwo = int(input("What is the second Y value? "))
                finalmy = int(ytwo) - int(yone)
                finalmx = int(xtwo) - int(xone)
            elif integer == 2:
                xone = float(input("What is the first X value? "))
                yone = float(input("What is the first Y value? "))
                xtwo = float(input("What is the second X value? "))
                ytwo = float(input("What is the second Y value? "))
                finalmy = float(ytwo) - float(yone)
                finalmx = float(xtwo) - float(xone)
            if finalmx < 0:
                finalmx = abs(finalmx)
                finalmy = -abs(finalmy)
            if finalmy < 0 and finalmx < 0:
                finalmx = abs(finalmx)
                finalmy = abs(finalmy)
            if not finalmy == 0 and not finalmx == 0:
                m = finalmy / finalmx
                if not isinstance(m, int):
                    mtwo = ((str(finalmy)) + "/" + (str(finalmx)))
                elif isinstance(m, int):
                    mtwo = m
            #Prints slope
            print("Slope: " + (str(mtwo)))
            #Determines Y intercept (B)
            if m > 0:
                b = yone - xone
            if m < 0:
                b = yone - xone
            if m == 0:
                b = yone
            #Determines X intercept
            xi = b / m
            #Prints Y and X intercept
            print("the y intercept is (0," + str(b) + ")")
            if integer == 1:
                print("the x intercept is (" + str(int(xi)) + ",0)")
            if integer == 2:
                print("the x intercept is (" + str(float(xi)) + ",0")
            print("Equation: ")
            #Determines equation for slope intercept
            if typee == 1:
                if b > 0:
                    if m > 1:
                        print("y = " + (str(mtwo)) + "x + " + (str(b)))
                    if m < 1:
                        print("y = " + (str(mtwo)) + "x + " + (str(b)))
                    if m == 1:
                        print("y = x + " + (str(b)))
                if b < 0:
                    if m > 1:
                        print("y = " + (str(mtwo)) + "x " + (str(b)))
                    if m < 1:
                        print("y = " + (str(mtwo)) + "x " + (str(b)))
                    if m == 1:
                        print("y = x " + (str(b)))
                if b == 0:
                    if m > 1:
                        print("y = " + (str(mtwo)) + "x")
                    if m < 1:
                        print("y = " + (str(mtwo)) + "x")
                    if m == 1:
                        print("y = x")
            #Determines equation for point slope
            if typee == 2:
                if yone > 0:
                    if xone > 0:
                        print("y - " + (str(yone)) + " = " + (str(mtwo)) + "(x - " + (str(xone)) + ")")
                    if xone < 0:
                        print("y - " + (str(yone)) + " = " + (str(mtwo)) + "(x + " + (str(abs(xone))) + ")")
                    if xone == 0:
                        print("y - " + (str(yone)) + " = " + (str(mtwo)) + "(x)")
                if yone < 0:
                    if xone > 0:
                        print("y + " + (str(abs(yone))) + " = " + (str(mtwo)) + "(x - " + (str(xone)) + ")")
                    if xone < 0:
                        print("y + " + (str(abs(yone))) + " = " + (str(mtwo)) + "(x + " + (str(abs(xone))) + ")")
                    if xone == 0:
                        print("y + " + (str(abs(yone))) + " = " + (str(mtwo)) + "(x)")
                if yone == 0:
                    if xone > 0:
                        print("y = " + (str(mtwo)) + "(x - " + (str(xone)) + ")")
                    if xone < 0:
                        print("y = " + (str(mtwo)) + "(x + " + (str(abs(xone))) + ")")
                    if xone == 0:
                        print("y = " + (str(mtwo)) + "(x)")
            #Determines equation for point slope
            if typee == 3:
                if b > 0:
                    if m > 1:
                        print((str(mtwo)) + "x + y = " + (str(b)))
                    if m < 1:
                        print((str(mtwo)) + "x + y = " + (str(b)))
                    if m == 1:
                        print("x + y = " + (str(b)))
                if b < 0:
                    if m > 1:
                        print((str(mtwo)) + "x + y = " + (str(b)))
                    if m < 1:
                        print((str(mtwo)) + "x + y = " + (str(b)))
                    if m == 1:
                        print("x + y = " + (str(b)))
                if b == 0:
                    if m > 1:
                        print((str(mtwo)) + "x + y = 0")
                    if m < 1:
                        print((str(mtwo)) + "x + y = 0")
                    if m == 1:
                        print("x + y = 0")
            #Ends program or starts it over.
            while mrb == 1:
                end = input("Type 'yes' for another conversion/calculation, and type 'no' to end the program. ")
                if end == "no":
                    tasdfasfdhjasdhfkjashdfk = 1
                    mainvar = 2
                    mrb = 2
                    print("Successfully ended.")
                    sys.exit()
                elif end == "yes":
                    choice = 0
                    mainvar = 1
                    mrb = 0
                    input("(Enter to continue)")
                    mrb = 0
                    mrb = 0
                else:
                    mrb = 1
        if choice == "c":
            #SI: Slope Intercept
            #PS: Point Slope
            #S: Standard
            #Conversion list:
            #SI->PS->DONE!
            #SI->S
            #PS->S->DONE!
            #PS->SI->DONE!
            #S->SI
            #S->PS
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #Slope intercept -> point slope
            def converter_sips():
                tingy = 1
                tingytwo = 1
                print("Step one: Enter information. An easy way to answer the X and Y value questions is to use the Y intercept (y = mx + (B)).")
                xthing = float(input("Enter an X value "))
                ything = float(input("Enter a Y value "))
                mslope = float(input("Enter the slope's numerator. "))
                mslopeythingy = float(input("Enter the slope's denominator. If the slope is an integer, just enter 1. ")) 
                print("Step two: Are all the numbers integers (no decimal places)?")
                while tingy == 1:
                    thingchoice = input("y for yes, n for no ")
                    if thingchoice == "y":
                        tingy = 2
                        xthing = int(xthing)
                        ything = int(ything)
                        mslope = int(mslope)
                        mslopeythingy = int(mslopeythingy)
                    elif thingchoice == "n":
                        tingy = 2
                        xthing = float(xthing)
                        ything = float(ything)
                        mslope = float(mslope)
                        mslopeythingy = float(mslopeythingy)
                    else:
                        tingy = 1
                if mslopeythingy != 1:
                    mslopeactual = ((str(mslope)) + "/" + (str(mslopeythingy)))
                    mslope = mslopeactual
                else:
                    mslope = mslope
                if xthing == 0 and ything != 0:
                    if ything > 0:
                        print("y - " + (str(ything)) + " = " + (str(mslope)) + "(x)")
                    if ything < 0:
                        print("y + " + (str(abs(ything))) + " = " + (str(mslope)) + "(x)") 
                if ything == 0 and xthing != 0:
                    if xthing > 0:
                        print("y = " + (str(mslope)) + "(x + )" + (str(xthing)) + ")") 
                    if xthing < 0:
                        print("y = " + (str(mslope)) + "(x + )" + (str(abs(xthing))) + ")") 
                if ything == 0 and ything == 0:
                    print("y = " + (str(mslope)) + "(x)")
                if xthing != 0 and ything !=0:
                    if xthing > 0 and ything > 0:
                        print("y - " + (str(ything)) + " = " + (str(mslope)) + "(x - " + (str(xthing)) + ")")
                    if xthing > 0 and ything < 0:
                        print("y + " + (str(abs(ything))) + " = " + (str(mslope)) + "(x - " + (str(xthing)) + ")")
                    if xthing < 0 and ything > 0:
                        print("y - " + (str(ything)) + " = " + (str(mslope)) + "(x + " + (str(abs(xthing))) + ")")
                    if xthing < 0 and ything < 0:
                        print("y + " + (str(abs(ything))) + " = " + (str(mslope)) + "(x + " + (str(abs(xthing))) + ")")
            #Slope intercept -> standard
            def converter_sis():
                tingy = 1
                tingytwo = 1
                print("Step one: Enter information.")
                xthing = float(input("Enter an X value "))
                ything = float(input("Enter a Y value "))
                mslope = float(input("Enter the slope's numerator. "))
                mslopeythingy = float(input("Enter the slope's denominator. If the slope is an integer, just enter 1. "))
                mslopeactuall = mslope / mslopeythingy
                bbb = float(input("What is the y-intercept of the equation? "))
                print("Step two: Are all the numbers integers (no decimal places)?")
                while tingy == 1:
                    thingchoice = input("y for yes, n for no ")
                    if thingchoice == "y":
                        tingy = 2
                        xthing = int(xthing)
                        ything = int(ything)
                        mslope = int(mslope)
                        mslopeythingy = int(mslopeythingy)
                        bbb = int(bbb)
                    elif thingchoice == "n":
                        tingy = 2
                        xthing = float(xthing)
                        ything = float(ything)
                        mslope = float(mslope)
                        mslopeythingy = float(mslopeythingy)
                        bbb = float(bbb)
                    else:
                        tingy = 1
                if mslopeythingy != 1:
                    mslopeactual = ((str(mslope)) + "/" + (str(mslopeythingy)))
                    mslope = mslopeactual

                else:
                    mslope = mslope
                if bbb >= 0:
                    typeOfBB = "+ " 
                    slopeIntercept = "y = " + str(mslope) + "x " + typeOfBB + str(bbb)
                else:
                    typeOfBB = "- "
                    slopeIntercept = "y = " + str(mslope) + "x " + typeOfBB + (str(abs(bbb)))
                if mslopeactuall >= 0:
                    finalFINAL = ("y - " + str(mslope) + "x = " + str(bbb))
                if mslopeactuall < 0:
                    finalFINAL = ("y + " + (str(abs(mslope))) + "x = " + str(bbb))
                print("Conversion: " + finalFINAL)
            #Point slope -> standard
            def converter_pss():
                #Information entry:
                tingythree = 1
                print("Step one: Enter information")
                xthing1 = float(input("Enter variable X1 "))
                ything1 = float(input("Enter variable Y1 "))
                mslopeynum = float(input("Enter slope numerator "))
                mslopeyden = float(input("Enter slope denominator. If the slope is a whole number, enter 1. "))
                print("Step two: Are all these numbers integers (No decimal points)? ")
                #y - y1 = m(x - x1)
                #y = mx + b
                while tingythree == 1:
                    #integer choice:
                    thingchoice1 = input("y for yes, n for no ")
                    if thingchoice1 == "y":
                        xthing1 = int(xthing1)
                        ything1 = int(ything1)
                        mslopeynum = int(mslopeynum)
                        mslopeyden = int(mslopeyden)
                        tingythree = 2
                    elif thingchoice1 == "n":
                        tingythree = 2
                    else:
                        tingythree = 1
                    #Finds Y intercept:
                    xthing22 = xthing1
                    if xthing22 == 0:
                        ything2 = ything1
                    while xthing22 != 0:
                        if mslopeynum >= 0 and mslopeyden >= 0:
                            ything2 = ything1 - mslopeynum
                            xthing22 = xthing22 - mslopeyden
                        if mslopeynum < 0 and mslopeyden < 0:
                            mslopeynum123 = abs(mslopeynum)
                            mslopeyden123 = abs(mslopeyden)
                            ything2 = ything1 + mslopeynum123
                            xthing22 = xthing22 + mslopeyden123
                        if mslopeynum < 0 and mslopeyden >= 0:
                            mslopeynum123 = abs(mslopeynum)
                            ything2 = ything1 + mslopeynum123
                            xthing22 = xthing22 - mslopeyden
                        if mslopeynum >= 0 and mslopeyden < 0:
                            mslopeyden123 = abs(mslopeyden)
                            ything2 = ything1 - mslopeynum
                            xthing22 = xthing22 + mslopeyden123
                    bb = ything2
                    print(bb)
                    if mslopeynum >= 0 and mslopeyden >= 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = str(mslopeynum) + "/" + str(mslopeyden)
                    if mslopeynum < 0 and mslopeyden < 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = mslopeynum + "/" + mslopeyden
                    if mslopeynum < 0 and mslopeyden >= 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = mslopeynum + "/" + mslopeyden
                    if mslopeynum >= 0 and mslopeyden < 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = mslopeynum + "/" + mslopeyden
                    if mslopeyden == 1:
                        mslopeyFinal4 = mslopeynum 
                    finalThreeOne = "y = " + str(mslopeyFinal4) + "x + " + str(bb)
                    if mslopeyFinal4 >= 0:
                        finalThreeTwo = ("y - " + str(mslopeyFinal4) + "x = " + str(bb))
                    if mslopeyFinal4 < 0:
                        finalThreeTwo = ("y + " + (str(abs(mslopeyFinal4))) + "x = " + str(bb))
                    print("Conversion: " + finalThreeTwo)
            #Point slope -> slope intercept
            def converter_pssi():
                #Information entry:
                tingythree = 1
                print("Step one: Enter information")
                xthing1 = float(input("Enter variable X1 "))
                ything1 = float(input("Enter variable Y1 "))
                mslopeynum = float(input("Enter slope numerator "))
                mslopeyden = float(input("Enter slope denominator. If the slope is a whole number, enter 1. "))
                print("Step two: Are all these numbers integers (No decimal points)? ")
                #y - y1 = m(x - x1)
                #y = mx + b
                while tingythree == 1:
                    #integer choice:
                    thingchoice1 = input("y for yes, n for no ")
                    if thingchoice1 == "y":
                        xthing1 = int(xthing1)
                        ything1 = int(ything1)
                        mslopeynum = int(mslopeynum)
                        mslopeyden = int(mslopeyden)
                        tingythree = 2
                    elif thingchoice1 == "n":
                        tingythree = 2
                    else:
                        tingythree = 1
                    #Finds Y intercept:
                    xthing22 = xthing1
                    if xthing22 == 0:
                        ything2 = ything1
                    while xthing22 != 0:
                        if mslopeynum >= 0 and mslopeyden >= 0:
                            ything2 = ything1 - mslopeynum
                            xthing22 = xthing22 - mslopeyden
                        if mslopeynum < 0 and mslopeyden < 0:
                            mslopeynum123 = abs(mslopeynum)
                            mslopeyden123 = abs(mslopeyden)
                            ything2 = ything1 + mslopeynum123
                            xthing22 = xthing22 + mslopeyden123
                        if mslopeynum < 0 and mslopeyden >= 0:
                            mslopeynum123 = abs(mslopeynum)
                            ything2 = ything1 + mslopeynum123
                            xthing22 = xthing22 - mslopeyden
                        if mslopeynum >= 0 and mslopeyden < 0:
                            mslopeyden123 = abs(mslopeyden)
                            ything2 = ything1 - mslopeynum
                            xthing22 = xthing22 + mslopeyden123
                    bb = ything2
                    print(bb)
                    if mslopeynum >= 0 and mslopeyden >= 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = str(mslopeynum) + "/" + str(mslopeyden)
                    if mslopeynum < 0 and mslopeyden < 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = mslopeynum + "/" + mslopeyden
                    if mslopeynum < 0 and mslopeyden >= 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = mslopeynum + "/" + mslopeyden
                    if mslopeynum >= 0 and mslopeyden < 0:
                        mslopeyy = mslopeynum / mslopeyden
                        if isinstance(mslopeyy, int):
                            mslopeyFinal4 = mslopeyy
                        else:
                            mslopeyFinal4 = mslopeynum + "/" + mslopeyden
                    if mslopeyden == 1:
                        mslopeyFinal4 = mslopeynum 
                    finalFour = "y = " + str(mslopeyFinal4) + "x + " + str(bb)
                    print("Conversion: " + finalFour)
            #Standard -> slope intercept
            def converter_ssi():
                i = 0
                A = float(input("Enter value x is multiplied by (example: (2)x + By = C) "))
                B = float(input("Enter value y is multiplied by (example: Ax + (2)y = C) "))
                C = float(input("Enter the constraint at the end of the equation "))
                while i == 0:
                    integer = input("Are these numbers integers? (y/n) ")
                    if integer == "y":
                        i = 1
                        A = int(A)
                        B = int(B)
                        C = int(C)
                    elif integer == "n":
                        i = 1
                        A = float(A)
                        B = float(B)
                        C = float(C)
                    else:
                        i = 0
                if B >= 0:
                    abcONE = str(A) + "x + " + str(B) + "y = " + str(C)
                elif B < 0:
                    abcONE = str(A) + "x - " + (str(abs(B))) + "y = " + str(C)
                if C >= 0:
                    if B != 1:
                        afinal = A / B
                        if isinstance(afinal, int):
                            afinal = A / B
                        else:
                            afinal = str(A) + "/" + str(B)
                            print(afinal)
                        if A != 1:
                            abcTWO = "y = " + str(afinal) + "x + " + str(C)
                        else:
                            abcTWO = str(B) + "y = x + " + str(C)
                    else:
                        afinal = A
                        if A != 1:
                            abcTWO = "y = " + str(afinal) + "x + " + str(C)
                        else:
                            abcTWO = "y = x + " + str(C)
                if C < 0:
                    if B != 1:
                        afinal = A / B
                        if isinstance(afinal, int):
                            afinal = A / B
                        else:
                            afinal = str(A) + "/" + str(B)
                        if A != 1:
                           abcTWO = "y = " + str(afinal) + "x - " + (str(abs(C)))
                        else:
                            abcTWO = str(B) + "y = " + str(afinal) + "x - " + (str(abs(C)))
                    else:
                        afinal = A
                        if A != 1:
                            abcTWO = "y = " + str(afinal) + "x - " + (str(abs(C)))
                        else:
                            abcTWO = "y = x + " + (str(abs(C)))
                print("Conversion: " + abcTWO)
            #Standard -> point slope
            def converter_sps():
                i = 0
                A = float(input("Enter value x is multiplied by (example: (2)x + By = C) "))
                B = float(input("Enter value y is multiplied by (example: Ax + (2)y = C) "))
                C = float(input("Enter the constraint at the end of the equation "))
                while i == 0:
                    integer = input("Are these numbers integers? (y/n) ")
                    if integer == "y":
                        i = 1
                        A = int(A)
                        B = int(B)
                        C = int(C)
                    elif integer == "n":
                        i = 1
                        A = float(A)
                        B = float(B)
                        C = float(C)
                    else:
                        i = 0
                if B >= 0:
                    abcONE = str(A) + "x + " + str(B) + "y = " + str(C)
                elif B < 0:
                    abcONE = str(A) + "x - " + (str(abs(B))) + "y = " + str(C)
                if C >= 0:
                    if B != 1:
                        afinal = A / B
                        if isinstance(afinal, int):
                            afinal = A / B
                        else:
                            afinal = str(A) + "/" + str(B)
                            print(afinal)
                        if A != 1:
                            abcTWO = "y = " + str(afinal) + "x + " + str(C)
                        else:
                            abcTWO = str(B) + "y = x + " + str(C)
                    else:
                        afinal = A
                        if A != 1:
                            abcTWO = "y = " + str(afinal) + "x + " + str(C)
                        else:
                            abcTWO = "y = x + " + str(C)
                if C < 0:
                    if B != 1:
                        afinal = A / B
                        if isinstance(afinal, int):
                            afinal = A / B
                        else:
                            afinal = str(A) + "/" + str(B)
                        if A != 1:
                           abcTWO = "y = " + str(afinal) + "x - " + (str(abs(C)))
                        else:
                            abcTWO = str(B) + "y = " + str(afinal) + "x - " + (str(abs(C)))
                    else:
                        afinal = A
                        if A != 1:
                            abcTWO = "y = " + str(afinal) + "x - " + (str(abs(C)))
                        else:
                            abcTWO = "y = x + " + (str(abs(C)))
                print("Conversion: " + abcTWO)
                tingy = 1
                tingytwo = 1
                xthing = 0
                ything = C
                mslope = A
                while tingy == 1:
                    if integer == "y":
                        tingy = 2
                        xthing = int(xthing)
                        ything = int(ything)
                        mslope = int(mslope)
                    elif integer == "n":
                        tingy = 2
                        xthing = float(xthing)
                        ything = float(ything)
                        mslope = float(mslope)
                    else:
                        tingy = 1
                if xthing == 0 and ything != 0:
                    if ything > 0:
                        print("y - " + (str(ything)) + " = " + (str(mslope)) + "(x)")
                    if ything < 0:
                        print("y + " + (str(abs(ything))) + " = " + (str(mslope)) + "(x)") 
                if ything == 0 and xthing != 0:
                    if xthing > 0:
                        print("y = " + (str(mslope)) + "(x + )" + (str(xthing)) + ")") 
                    if xthing < 0:
                        print("y = " + (str(mslope)) + "(x + )" + (str(abs(xthing))) + ")") 
                if ything == 0 and ything == 0:
                    print("y = " + (str(mslope)) + "(x)")
                if xthing != 0 and ything !=0:
                    if xthing > 0 and ything > 0:
                        print("y - " + (str(ything)) + " = " + (str(mslope)) + "(x - " + (str(xthing)) + ")")
                    if xthing > 0 and ything < 0:
                        print("y + " + (str(abs(ything))) + " = " + (str(mslope)) + "(x - " + (str(xthing)) + ")")
                    if xthing < 0 and ything > 0:
                        print("y - " + (str(ything)) + " = " + (str(mslope)) + "(x + " + (str(abs(xthing))) + ")")
                    if xthing < 0 and ything < 0:
                        print("y + " + (str(abs(ything))) + " = " + (str(mslope)) + "(x + " + (str(abs(xthing))) + ")")
            #Asks for decision and executes function
            print("What would you like to convert?")
            print("1: slope intercept to point slope")
            print("2: slope intercept to standard")
            print("3: point slope to standard")
            print("4: point slope to slope intercept")
            print("5: standard to slope intercept")
            print("6: standard to point slope")
            while tingytwo == 1:
                choicee = input("Type the number of your conversion here. ")
                if choicee == "1":
                    tingytwo = 2
                    converter_sips()
                elif choicee == "2":
                    tingytwo = 2
                    converter_sis()
                elif choicee == "3":
                    tingytwo = 2
                    converter_pss()
                elif choicee == "4":
                    tingytwo = 2
                    converter_pssi()
                elif choicee == "5":
                    tingytwo = 2
                    converter_ssi()
                elif choicee == "6":
                    tingytwo = 2
                    converter_sps()
                else:
                    tingytwo = 1
            #Ends program, or starts program over.
            while mrb == 1:
                end = input("Type 'yes' for another conversion/calculation, and type 'no' to end the program. ")
                if end == "no":
                    tasdfasfdhjasdhfkjashdfk = 1
                    mainvar = 2
                    mrb = 2
                    print("Successfully ended.")
                    sys.exit()
                elif end == "yes":
                    choice = 0
                    mainvar = 1
                    mrb = 0
                    input("(Enter to continue)")
                    mrb = 0
                    mrb = 0
                else:
                    mrb = 1
