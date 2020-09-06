import functions

userInput = ''
validUser = False
userType = ''
currentUser = 'None'

while(userInput != 'quit' or userInput != 'q'):
    print("Logged in as: %s" % currentUser)

    #allow user to quit application
    if(userInput == 'q' or userInput == 'quit'):
        break

    if(validUser == False):
        #if user is not logged in 
        userInput = input("Login or Create Account: ")
        print()
    else:
        search = input("Search by [ Name | Class | Price ]: ").split()

        if(search[0] == 'q' or search[0] == 'quit'):
            break
        #search for users based on user type 
        if(userType == 'student'):
            #students search for tutors
            print()
            if(search[0] == 'name'.casefold()):
                functions.nameSearch(search[1],'student')
            elif(search[0] == 'class'.casefold()):    
                functions.classSearch(search[1],'student')
            elif(search[0] == 'price'.casefold()):
                functions.priceSearch(search[1],'student')

        elif(userType == 'tutor'):
            #tutors search for students
            print()
            if(search[0] == 'name'.casefold()):
                functions.nameSearch(search[1],'tutor')
            elif(search[0] == 'class'.casefold()):    
                functions.classSearch(search[1],'tutor')
            elif(search[0] == 'price'.casefold()):
                functions.priceSearch(search[1],'tutor')

    #user login
    if(userInput == 'login'.casefold()):
        userInput = input("Student or Tutor: ")
        print()

        #login as a student
        if(userInput == 'student'.casefold()):
            username = input("Username: ")
            password = input("Password: ")
            loginOutput = functions.studentLogin(username,password)
            validUser = loginOutput[0]
            currentUser = loginOutput[1]
            userType = 'student'

        #login as a tutor
        if(userInput == 'tutor'.casefold()):
            username = input("Username: ")
            password = input("Password: ")
            loginOutput = functions.tutorLogin(username,password)
            validUser = loginOutput[0]
            currentUser = loginOutput[1]
            userType = 'tutor'

    if(userInput == 'create account'.casefold()):
        userInput = input("Student or Tutor: ")
        print()

        if(userInput == "student".casefold()):
            currentUser = functions.createAccount('student')[1]
            validUser = True
            userType = 'student'

        elif(userInput == "tutor".casefold()):
            currentUser = functions.createAccount('tutor')[1]
            validUser = True
            userType = 'tutor'

    

    