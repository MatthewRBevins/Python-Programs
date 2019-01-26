print("Welcome to Name Generator!")
print("Code by MSGUY")
i = 0
j = 0
errors = 0
generated = []
input("(ENTER TO GENERATE NAME)")
import random
import sys
while True:
    ne = random.randint(1, 2)
    en = random.randint(1, 2)
    firsts = ["Matthew", "Teddy", "Tristan", "Francis", "Heinz", "Linda", "Vanessa", "Gina", "Kaden", "Lucas", "Kate", "Charlotte", "Ella", "Natalie", 'Bryn', 'Sean', 'Will', 'George', 'Frosty', "Ralph", "Gladys", "Imogene", "Leroy", "Ollie", "Claude", "Elizabeth", "Elmer", "Hobie", "Grace", "Janet", "Helen", "Emmy", "Severus", "Harry", "Geneva", "Drake", "Draco", "Gregory", "Vincent", "Ron", "Donald", "Nate", "Dee Dee", "Chad", "Marcus", "Ruby", "Mr.", "Mrs.", "Ms.", "Nicole"]
    firsts2 = random.randint(0, len(firsts) - 1)
    names = ["Stinky", "Lady", "Lazy", "Hungry", "Horrible", "Cool", "Sticky", "Bad", "Von", "Icky", "Chunky", "Hairy", "Donut", "Fishy", "Lumpy"]
    names2 = ["paw", "claw", "fur", "fuzz", "toe", "cat", "kitty", "goop", "hair", "ball", "hairball", "breath", "bones", "lump", "chips"]
    name1 = random.randint(0, 14)
    name2 = random.randint(0, 14)
    hi = names[name1]
    if ne == 1:
        hi2 = names2[name2]
    elif ne == 2:
        hi2 = names[name2]
    if en == 1:
        hi = names[name1]
    elif en == 2:
        hi = names2[name1]
    firsts3 = firsts[firsts2]
    hitot = str(firsts3) + " " + str(hi) + str(hi2)
    if not hitot in generated:
        print("name: " + str(hitot))
        generated.append(hitot)
        print(len(generated))
        print(str(errors))
        """input("")
        again = input("Enter for another name. Type \"stop\" to stop the program. Type \"names\" to see all your generated names.")
        if again == "stop":
            sys.exit()
        if again == "names":
            print(generated)
        else:
            input("(ENTER TO GENERATE NAME)")"""
    else:
        errors = errors + 1
        print("----------------------------------------------------------------------ERROR NO. " + str(errors))
    if len(generated) == 45000:
        print("***STATS***")
        print("ERRORS: " + str(errors))
        print("NAMES GENERATED " + len(generated))
        hi = errors / generated
        print("AVERAGE ERRORS PER NAME: " + hi + " ERRORS")
        print("THANKS FOR USING MSGUY CODING PYTHON NAME GENERATOR!")
        input("ENTER FOR FULL LIST OF NAMES")
        print(generated)
        input("ENTER TO LEAVE")
        sys.exit()
