import random
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
capitals = ["Montgomery", "Juneau", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]
i = 0
score = 0
deleted = 0
print("Welcome to states and capitals quiz, by MSGuy01!")
input("Enter to start the game!")
while i < len(states) + 1:
    if len(states) != 0:
        r = random.randint(0, len(states) - 1)
    choice = input("What is the capital of " + states[r] + "?: ")
    if choice == capitals[r]:
        print("Correct!")
        del states[r]
        del capitals[r]
        deleted = deleted + 1
        score = score + 1
    else:
        print("Sorry, the correct answer was " + capitals[r] + ".")
        del states[r]
        del capitals[r]
        deleted = deleted + 1
    i = i + 1
print("Your score was " + str(score) + "!")
