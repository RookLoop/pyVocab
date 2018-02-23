'''pyVocab By Matthew Hargrave. Based on the glossaries in Think Python: How To
Think Like A Computer Scientist By Allen B. Downey. Many of the functions in
here are general enough that they could be used to make other multiple choice
tests or trivia games from a properly formated group of .txt files. '''

import random # used to get random questions and answers
import os # used to clear the screen mainly

def clearscreen():
    '''Depending on the platform(windows or linux/mac) we can clear the screen'''
    if OS == 'nt':
        os.system("cls")
    elif OS == 'posix':
        os.system("clear")

def splitglossary(filename):
    '''Takes properly formated .txt file and returns a list for later use'''
    glossary = open(filename, encoding = "ISO-8859-1")
    gls1 = glossary.read()
    glossary.close()
    gls1colon = gls1.replace(".",":")   # Change all "." to ":" so we can easily delineate
    gls1strip = gls1colon.replace("\n", " ")
    gls1split = gls1strip.split(": ") # This list will contain alternat between word and definition
    return gls1split

def pause():
    input("\nPress <Enter> to continue.")

def dictglossary(glossarylist):
    '''Takes a list, which alternates between a word (key) and its definition (key +1) and creates
    a dictionary out of it, for this program I decided to make the definition the key
    and the word the value, which seems counter intuitive, but it can easily be switched'''
    glossarydict = dict()
    for key in range(0,len(glossarylist),2):
        glossarydict[glossarylist[key +1]] = glossarylist[key]
    return glossarydict

def writesavefile():
    '''create a .txt file from the list chapterstatus which effectivly saves your accomplishments'''
    savefile = open('status.txt','w')
    for index in range(numOfChapters):
        savefile.write(chapterstatus[index])
        savefile.write("\n") # add a new line break for ease of reading by readline()
    savefile.close

def readsavefile():
    '''reads a .txt file back into the chapterstatus list, one line per index'''
    savefile = open('status.txt')
    for lineindex in range(len(chapterstatus)):
        lineinstatus = savefile.readline()
        print(lineinstatus)
        linestrip = lineinstatus.replace("\n","") # remove the new line break
        chapterstatus[lineindex] = linestrip
    savefile.close()

def splashscreen():
    '''A short description/introduction to the program and the first use of the clearscreen() function'''
    clearscreen()

    print("\n","*"*80,sep = "")
    print("Welcome to PyVocab. Test your knowledge of Python and general programming ",\
    "\nterminlogy. Based on the glossaries in Think Python: How To Think Like A \nComputer Scientist ",\
    "By Allen B. Downey.","\n", sep = "")
    print("*"*80)
    pause()

def mainmenu():
    ''' The user is presented with 21 chapter/tests to complete, the index of that choice is returned
    we can also exit the program from here, if not done so, progress is lost'''
    clearscreen()
    global gameloop # setting this to false will end the main game loop ending the game
    global chapterloop # a list of 21 boolean Falses, if we turn 1 on, we begin a chapter

    listof21stringnumbers = [] # this is useful for writing and reading the chapters and selection of the chapters
    for x in range(21):
        listof21stringnumbers.append(str(x + 1))

    print("\nMain Menu \n") # list all the chapters and chapterstatus(if any) and some formatting
    for x in range(21):
        stringP = listof21stringnumbers[x] + "." + " Chapter" +listof21stringnumbers[x] + " " + chaptertitlesplit[x]
        padx = (55 - len(stringP)) # 55 is where the chapter status column will be
        print(stringP," "*padx, chapterstatus[x])

    print("\nx. To exit program")

    mainChoice = input("\n\nEnter a chapter number to begin test: ")

    if mainChoice == "x":  # will effectivly exit the main game loop gracefully
        gameloop = False
        return

    for y in listof21stringnumbers: # compare the srings "1"-"21" to the user input
        if mainChoice == y:
            mainChoice = int(y) # turn the user input into an intger so we can use it as an index
            chapterloop[mainChoice -1] = True # turn a specific chapter boolean to True based on the index
            chapterindex = mainChoice - 1  # again make sure the user input is the index for the chapter
            return chapterindex  # this chapter index will be used frequently througout the loop

    print("\n",pad,"  Invalid Entry  ",pad, sep="")
    pause()

def getrandomquestion(attempts,correct,totalpossible,glossarydict,deflist,checklistx):
    ''' The main engine of the game. Here is where we generate random questions and answers
    and ensure we do on repeat an answered question, nor duplicate wrong multiple choice answers
    here is also where we set the chapterstatus based on the users completion'''

    clearscreen()

    global updatechecklistflag # This variable will be used later to call the updatechecklist function

    definition = random.choice(list(glossarydict)) # we get our random definition/question from our dictionary

    if correct == totalpossible:  # one way out of the chapter loop is to answer all questions correctly
        print("\n", correct, " out of ", totalpossible, " answered",\
        "\n",correct, " correct out of ", attempts, " attempts","\n",sep = "")

        percentScore = correct / attempts * 100
        percentString = format(percentScore,'.0f') + "%"
        print("You scored ",percentString)

        chapterstatus[chapterindex] = "Completed. Score: " + percentString #update the chapter status
        return False # exit the function and break the outside loop to return to main menu

    for indexV in range(len(deflist)):  # we check the random definition from the dict to find its index in the list of defs
        if deflist[indexV] == definition:
            indexcheck = indexV  # we assign the index to indexcheck

    while checklistx[indexcheck] == True:  # we lookup to see if the definition/question has been answered already
        definition = random.choice(list(glossarydict))   # if it has we get a new one
        for indexV2 in range(len(deflist)):   # we get the new index of this definition and repeat until we have a nonanswered question/definition
            if deflist[indexV2] == definition:
                indexcheck = indexV2

    title = "Chapter " + str(chapterindex + 1) + " " + chaptertitlesplit[chapterindex]

    print("\n","*"*80,"\n\n",title,"\n\n",\
    "Enter <1-4> to make selection Or <x> to return to the Main Menu",\
    "\n""\n", correct, " out of ", totalpossible, " answered",\
    "\n\n",correct, " correct out of ", attempts, " attempts","\n\n\n",\
    "*"*80,"\n\n", definition,"\n", sep = "")

    answer = glossarydict[definition]  # get term/answer/value that matches the random key/def from earlier
    wronganswer1 = random.choice(list(glossarydict.values()))  # create 3 random wrong answers
    wronganswer2 = random.choice(list(glossarydict.values()))
    wronganswer3 = random.choice(list(glossarydict.values()))

    # Make sure the wrong answers do not repeat or match the answer
    while wronganswer1 == answer or wronganswer1 == wronganswer2 or wronganswer1 == wronganswer3:
        wronganswer1 = random.choice(list(glossarydict.values()))
    while wronganswer2 == answer or wronganswer2 == wronganswer1 or wronganswer1 == wronganswer3:
        wronganswer2 = random.choice(list(glossarydict.values()))
    while wronganswer3 == answer or wronganswer3 == wronganswer2 or wronganswer3 == wronganswer1:
        wronganswer3 = random.choice(list(glossarydict.values()))

    listofchoices = [answer, wronganswer1, wronganswer2, wronganswer3] # create a list from our answer and 3 wrongs
    random.shuffle(listofchoices)  # randomly shuffle the list, a nice function
    print("1. ",listofchoices[0],"\n""\n","2. ", listofchoices[1],"\n""\n",\
    "3. ",listofchoices[2],"\n""\n","4. ",listofchoices[3],"\n""\n", sep = "")

    for choice in range(len(listofchoices)):  # determine where in the (now random) list of choices our real answer is
        if listofchoices[choice] == answer:
            answerindex = str(choice + 1)

    playerAnswer = input("Answer: ")

    if playerAnswer == answerindex: # see if the plyare input matches the answer index we just found
        print("\n\n",pad, "  Correct!  ",pad,"\n" ,sep ="")
        pause()
        updatechecklistflag = True  # once back in the parent fucntion we will run an update based on this
        return definition  # the update will use this return value to look up, it also doubles as a boolean to keep the loop going
    elif playerAnswer == "x": # kicks us out of the parent loop and funtion returning us the main menu without saving any data
        return False
    else:
        print("\n",pad,"  Incorrect  ",pad,"\n",sep ="")
        pause()
        return True

def updatechecklist(correctanswer,deflist,checklist):
    ''' takes a correct answer, finds its index, and updates the corresponding
    index in a checklist of the same legnth'''

    for index in range(len(deflist)):
        if deflist[index] == correctanswer:
            answerindex = index

    checklist[answerindex] = True

def getallwordlists(filename):
    '''The main .txt reading funtions all call from here, and the 3 lists and
    one dict are all created here'''

    glossarylist = splitglossary(filename)
    glossarydict = dictglossary(glossarylist)

    checklist = []
    deflist = []

    for vocabindex in range(0,len(glossarylist),2):
        checklist.append("False")

    for definition in range(1,len(glossarylist),2):
        deflist.append(glossarylist[definition])

    # this is a little unusual and perhaps uncessary but we return a tuple that includes
    # a dictionary and 2 lists we will use again, this is a powerful feature but perhaps confusing here

    return (glossarydict,deflist,checklist)

def chapterloopx(filename):
    ''' A child of the main game loop and a parent of the main engine getrandomquestion()
    This function sets everything up for the chapter and prepares to start generating random
    questions after some counters are also created, these variables conviently get wiped out
    for each new chapter as the scope is local'''

    global updatechecklistflag
    tOfChXLists = getallwordlists(filename) # here is where that neat/strange tuple is created
    masterAnswer = True
    updatechecklistflag = False
    attempts = 0
    correct = 0
    totalpossible = len(list(tOfChXLists[0].keys()))


    while masterAnswer:  # the answer returned doubles as a boolean
        attempts += 1  # always incremented
        masterAnswer = getrandomquestion(attempts,correct,totalpossible,\
        tOfChXLists[0],tOfChXLists[1],tOfChXLists[2]) # call the question generator with a ton of values passed
        checklisty = []
        if updatechecklistflag:
            correct += 1   # only incremeted when answer was correct
            updatechecklist(masterAnswer,tOfChXLists[1],tOfChXLists[2]) # send over the answered question to check it off as answered so it wont repeat
            updatechecklistflag = False # important to turn this off so wrong answers don't get checked off

    return False


# All the functions have now been defined, the program can start by naming a few variables

OS = os.name  # imporant for the clearscreen function to know if its windows or linux/mac
pad = "*"*5  # some string formatting
numOfChapters = 21
chapterstatus = [] # this is the list where the saved data is kept
chapterloop = [] # this is a list of 21 Falses, only the main menu can turn one True

for index in range(numOfChapters):  # the two previous lists have their values filled
    chapterloop.append(False)
    chapterstatus.append("")

# the following string would probably be better read from a file, but it contains all the chaper names for later use
chaptertitlesstring = "The Way of the Program:Variables, Expressions and Statements:Functions:Case Study - Interface Design:Conditionals and Recursion:Fruitful Functions:Iteration:Strings:Case Study - Word Play:Lists:Dictionaries:Tuples:Case Study - Data Structure Selection:Files:Classes and Objects:Classes and Functions:Classes and Methods:Inheritance:The Goodies:Debugging:Analysis of Algorithms"
chaptertitlesplit = chaptertitlesstring.split(":")



# read the saved data into the chapterstatus list, or create the savefile if it does not exist
try:
    readsavefile()
except:
    writesavefile()

splashscreen()

gameloop = True  # The main game loop, this will run until you exit from the main menu
while gameloop:

    chapterindex = mainmenu() # determines which chapter to go into

    # could have used a loop here as we did everywhere else, but this makes it a little more readable
    if chapterloop[0]:
        chapterloop[0] = chapterloopx("glossary1.txt")
    elif chapterloop[1]:
        chapterloop[1] = chapterloopx("glossary2.txt")
    elif chapterloop[2]:
        chapterloop[2] = chapterloopx("glossary3.txt")
    elif chapterloop[3]:
        chapterloop[3] = chapterloopx("glossary4.txt")
    elif chapterloop[4]:
        chapterloop[4] = chapterloopx("glossary5.txt")
    elif chapterloop[5]:
        chapterloop[5] = chapterloopx("glossary6.txt")
    elif chapterloop[6]:
        chapterloop[6] = chapterloopx("glossary7.txt")
    elif chapterloop[7]:
        chapterloop[7] = chapterloopx("glossary8.txt")
    elif chapterloop[8]:
        chapterloop[8] = chapterloopx("glossary9.txt")
    elif chapterloop[9]:
        chapterloop[9] = chapterloopx("glossary10.txt")
    elif chapterloop[10]:
        chapterloop[10] = chapterloopx("glossary11.txt")
    elif chapterloop[11]:
        chapterloop[11] = chapterloopx("glossary12.txt")
    elif chapterloop[12]:
        chapterloop[12] = chapterloopx("glossary13.txt")
    elif chapterloop[13]:
        chapterloop[13] = chapterloopx("glossary14.txt")
    elif chapterloop[14]:
        chapterloop[14] = chapterloopx("glossary15.txt")
    elif chapterloop[15]:
        chapterloop[15] = chapterloopx("glossary16.txt")
    elif chapterloop[16]:
        chapterloop[16] = chapterloopx("glossary17.txt")
    elif chapterloop[17]:
        chapterloop[17] = chapterloopx("glossary18.txt")
    elif chapterloop[18]:
        chapterloop[18] = chapterloopx("glossary19.txt")
    elif chapterloop[19]:
        chapterloop[19] = chapterloopx("glossary20.txt")
    elif chapterloop[20]:
        chapterloop[20] = chapterloopx("glossary21.txt")



# The last thing done on a proper exit is to save the chapterstatus list to a .txt file
writesavefile()

























