import functions



userInput = ''
validUser = False
userType = ''

while(userInput != 'quit' or userInput != 'q'):

    #allow user to quit application
    if(userInput == 'q' or userInput == 'quit'):
        break

    if(validUser == False):
        #if user is not logged in 
        userInput = input("Login or Create Account: ")
        print()
    else:

        #search for users based on user type 
        if(userType == 'student'):
            #students search for tutors
            search = input("Search for Tutors by Name or Class: ")
            print()

            functions.classSearch(search,'student')
            functions.nameSearch(search,'student')

        elif(userType == 'tutor'):
            #tutors search for students
            search = input("Search for Students by Name or Class: ")
            print()
            functions.classSearch(search,'tutor')
            functions.nameSearch(search,'tutor')

    #user login
    if(userInput == 'login'.casefold()):
        userInput = input("Student or Tutor: ")
        print()

        #login as a student
        if(userInput == 'student'.casefold()):
            username = input("Username: ")
            password = input("Password: ")
            validUser = functions.studentLogin(username,password)
            print(validUser)
            userType = 'student'

        #login as a tutor
        if(userInput == 'tutor'.casefold()):
            username = input("Username: ")
            password = input("Password: ")
            validUser = functions.tutorLogin(username,password)
            userType = 'tutor'

    if(userInput == 'create account'.casefold()):
        userInput = input("Student or Tutor: ")
        print()

        if(userInput == "student".casefold()):
            functions.createAccount('student')
            validUser = True
            userType = 'student'

        elif(userInput == "tutor".casefold()):
            functions.createAccount('tutor')
            validUser = True
            userType = 'tutor'

    

    