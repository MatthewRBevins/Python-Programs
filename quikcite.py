print("Welcome to QuikCite® by MSGUY®!")
input("(ENTER)")
print("if you do not have an answer to any question (author's name not given, etc.), just type \"no\".")
input("(ENTER)")
print("Also, some parts of the cites must be italicised, which cannot be done in python. Phrases that need to be italicised will be in curly brackets {}.")
input("(ENTER TO START)")
done = 0
general = 0
right = 0
now = 0
yeet = 0
auth = 0
addauths = 0
whatbook = 0
chapbook = 0
yearPub = 0
bookTitle = 0
edition = 0
edTransAuth = 0
dataBase = 0
eReader = 0
i = 0
cites = []
authors = []
while general == 0:
    while right == 0:
        source = input("Type \"webpage\" for a webpage and \"book\" for a book. ")
        if source == "webpage" or source == "book":
            right = 1
        else:
            right = 0
    if source == "webpage":
        while auth == 0:
            addauths = 0
            author1 = input("author's first name. ")
            author2 = input("author's last name ")
            author3 = input("author's middle initial ")
            author = author2 + ", " + author1 + " " + author3 + "."
            authors.append(author)
            while addauths == 0:
                addAuth = input("Add author? (yes or no) ")
                if addAuth == "yes":
                    addauths = 1
                    auth = 0
                elif addAuth == "no":
                    addauths = 1
                    auth = 1
                else:
                    addauths = 0
                    auth = 0
        while now == 0:
            dateType = input("input \"last modified\" if the website gives the date last modified, and input \"date accessed\" if not included. ")
            if dateType == "last modified" or dateType == "date accessed":
                now = 1
            else:
                now = 0
        if dateType == "last modified":
            dateType = ""
            print("for the following questions, enter the date the webpage was last modified.")
            date1 = input("month (typed) ")
            date2 = input("date ")
            date3 = input("year ")
        if dateType == "date accessed":
            dateType = "Accessed"
            print("for the following questions, enter the date you accessed the webpage. ")
            date1 = input("month (typed) ")
            date2 = input("date ")
            date3 = input("year ")
        url = input("Enter webpage URL ")
        siteTitle = input("Enter name of the website ")
        docTitle = input("Enter the document title ")
        publisher = input("Enter publisher's name ")
        if dateType == "":
            if len(authors) >= 3:
                gh = authors[0]
                totalCite = gh + ", et al. \"" + docTitle + ".\" [" + siteTitle + "], " + publisher + ", " + date2 + " " + date1 + " " + date3 + ", " + url + "."
            else:
                gh = authors[0]
                totalCite = gh + ". \"" + docTitle + ".\" [" + siteTitle + "], " + publisher + ", " + date2 + " " + date1 + " " + date3 + ", " + url + "."
        if dateType == "Accessed":
            if len(authors) >= 3:
                gh = authors[0]
                totalCite = gh + ", et al. \"" + docTitle + ".\" {" + siteTitle + "}, " + publisher + ", " + url + ". " +  dateType + " " + date2 + " " + date1 + " " + date3 + "."
            else:
                totalCite = authors + ". \"" + docTitle + ".\" {" + siteTitle + "}, " + publisher + ", " + url + ". " +  dateType + " " + date2 + " " + date1 + " " + date3 + "."
        cites.append(totalCite)
        input("Enter to see your current citations")
        print("***SAVED CITATIONS***")
        print(cites)
        yeet = 0
        while yeet == 0:
            nextTime = input("Would you like to save another cite? (yes/no) ")
            if nextTime == "no":
                yeet= 1
                general = 1
                yeet = 1
            if nextTime == "yes":
                yeet = 1
                general = 0
                yeet = 1
    """elif source == "book":
        while i == 0:
            whatbook = input("Did you access this book in print, online, or on an e-reader? ")
            if whatbook == "print" or whatbook = "e-reader" or whatbook = "online":
                i = 1
            else:
                i = 0
        if whatbook == "print":
            i = 0
            while i = 0:
                chapbook = input("Are you referencing the full book or one chapter? (Type full or chapter) ")
                if chapbook == "full" or chapbook == "chapter":
                    i = 1
                else:
                    i = 0
            if chapbook == "full":
                while i = 0:
                    edTransAuth = input("For the following questions, you will add the names of contributers. For this contributer, is it a translator (trans), editor """
