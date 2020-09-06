import functions

userInput = ''
validUser = False
userType = ''
currentUser = 'None'

while(userInput != 'quit' or userInput != 'q'):
    print("\n[Logged in as: %s]" % currentUser)

    #allow user to quit application
    if(userInput == 'q' or userInput == 'quit'):
        break

    if(validUser == False):
        #if user is not logged in 
        userInput = input("Login or Create Account: ")
        print()
    else:
        userInput = input("Commands [Search | Logout | Delete Account | List]: ")

        if(userInput.lower() == "search"):

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

        elif(userInput.lower() == "logout"):
            currentUser = 'None'
            validUser = False

        elif(userInput.lower() == 'delete account'):
            functions.removeUser(currentUser,userType)
            currentUser = 'None'
            validUser = False

        elif(userInput.lower() == 'list'):
            functions.listUsers(userType)
   
   
    #user login
    if(userInput == 'login'.casefold()):
        userInput = input("Student or Tutor: ")
        print()

        try:
            #login as a student
            if(userInput.lower() == 'student'):
                userType = 'student'
                username = input("Username: ")
                password = input("Password: ")
                loginOutput = functions.studentLogin(username,password)
                validUser = loginOutput[0]
                currentUser = loginOutput[1]

            #login as a tutor
            if(userInput.lower() == 'tutor'):
                userType = 'tutor'
                username = input("Username: ")
                password = input("Password: ")
                loginOutput = functions.tutorLogin(username,password)
                validUser = loginOutput[0]
                currentUser = loginOutput[1]
                
        except Exception as e:
            print(end="")
        
        

    if(userInput == 'create account'.casefold()):
        userInput = input("Student or Tutor: ")
        print()

        if(userInput == "student".casefold()):
            currentUser = functions.createAccount('student')
            validUser = True
            userType = 'student'

        elif(userInput == "tutor".casefold()):
            currentUser = functions.createAccount('tutor')
            validUser = True
            userType = 'tutor'

    

    