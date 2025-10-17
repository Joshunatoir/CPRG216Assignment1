

#this is a first attempt at just creating a program which collects student names and their GPA's and makes it viewable later
import time, os
#declaring variables:
dataStorage = {"Jimmy":3.2,"Jared":2.9}


print  ("Welcome Admin")

def addStudent():
    global dataStorage
    name = 'default'
    gpa = 0
    gpaSum = []
    print("what is the students Name?")
    name = input(": ")
    print("what was ", name ,"'s GPA?")
    while True:

        gpa = input("(to stop hit enter): ")
        # a little function to stop the while loop when nothing has been entered
        if gpa == "":
            break
        try:
            float(gpa)
            gpaSum.append(gpa)
        except:
            print("Invalid input, please try again.")
    gpaSum = sum(gpaSum)
    dataStorage[name] = gpaSum
    viewStudent()
    return

def viewStudent():
    global dataStorage
    print (dataStorage)
    input("Please press any key to continue. . .")
    

def removeStudent():
    global dataStorage
    print ("Here is the list of students you can remove:\n",dataStorage)

    
    return

def editStudent():
    global dataStorage
    print ("Here is the list of students you can edit:\n",dataStorage)
    print("which student would you like to edit?")
    edit = input(": ")
    
    return


running = True
while running == True:
    os.system('cls')
    print("please choose an option")
    choice = input("| To view student gpa's type 'V' |\n| To add a new student type 'A' |\n| To remove a student type 'R' |\n| To edit a student type 'E'| \n: ")
    time.sleep(0.5)
    choice = choice.upper()
    if choice == "A":
        addStudent()
    elif choice == "V":
        viewStudent()
    elif choice == "R":
        removeStudent()
    elif choice == "E":
        editStudent()
    else:
        print("please try again")
        time.sleep(0.5)

        


    
