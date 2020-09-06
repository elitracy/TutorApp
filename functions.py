import json
import hashlib

def classSearch(className,userType):

    personFound = False

    with open('studentData.json','r+') as file:
        studentData = json.load(file)
        file.close()

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()

    #student searches for tutor 
    if(userType == 'student'):
        print('Avalible Tutors: ')
        for i in tutorData['users']:
            for j in i['classes']:
                if(j == className):
                    print("%s : $%s/hr" % (i['name'], i['price']))
                    personFound = True
        
        if(not personFound):
            print("None :(")


    elif(userType == 'tutor'):
        print("Student Availible for Tutoring:")
        for i in studentData['users']:
            for j in i['classes']:
                if(j == className):
                    print(i['name'])
                    personFound = True

        if(not personFound):
            print("None :(")
    
    print()

def nameSearch(name,userType):

    with open('studentData.json','r+') as file:
        studentData = json.load(file)
        file.close()

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()

    correctUser = 'None'
     #tutor searching for student
    if(userType == 'tutor'):
        for i in studentData['users']:
            if(name in i['name'] ):
                correctUser = i
                print("%s : $%s/hr : %s" % (i['name'], i['price'],i['classes']))

            # else:
            #     print("User not Found")

    elif(userType == 'student'):
        for i in tutorData['users']:
            if(name in i['name']):
                correctUser = i
                print("%s : $%s/hr : %s" % (i['name'], i['price'],i['classes']))
            # else:
            #     print("User not Found")
    
def tutorLogin(username,password):

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()

    for i in tutorData['users']:
        if(i['username'] == username and i['password'] == hashlib.md5(password.encode()).hexdigest()):
            print('Login Successful\n')
            return True, username
    print('\nInvalid Credentials\n')
    return False

def studentLogin(username,password):
    
    with open('studentData.json','r+') as file:
        studentData = json.load(file)
        file.close()

    for i in studentData['users']:
        if(i['username'] == username and i['password'] == hashlib.md5(password.encode()).hexdigest()):
            print('Login Successful\n')
            return True, username

    print('\nInvalid Credentials\n')
    return False

def createAccount(userType):
    if(userType == "student"):
        
        username = input("Username: ")
        password = input("Password: ")
        studentName = input("Name: ")
        studentPriceMax = input("Max Price/hour: $")
        studentClasses = input("Classes You Need Help In: ").split()

        userInfo = {
            'name' : studentName,
            'price' : studentPriceMax,
            'classes' : studentClasses,
            'username' : username,
            'password' : hashlib.md5(password.encode()).hexdigest()
        }

        with open('studentData.json', 'r+') as file:
            data={}
            data = json.load(file)
            file.seek(0)
            data['users'].append(userInfo)
            json.dump(data,file,indent=4)
            file.close()

    if(userType == "tutor"):
        username = input("Username: ")
        password = input("Password: ")
        tutorName = input("Name: ")
        tutorPrice = input("Price/hour: $")
        tutorLocations = input("Locations: ").split()
        tutorMajor = input("Major: ")
        tutorGPA = input("GPA: ")
        tutorClasses = input("Classes: ").split()

        userInfo = {
            'name' : tutorName,
            'price' : tutorPrice,
            'locations' : tutorLocations,
            'major' : tutorMajor,
            'gpa' : tutorGPA,
            'classes' : tutorClasses,
            'username' : username,
            'password' : hashlib.md5(password.encode()).hexdigest()
        }

        with open('tutorData.json', 'r+') as file:
            data={}
            data = json.load(file)
            file.seek(0)
            data['users'].append(userInfo)
            json.dump(data,file,indent=4)
            file.close()

    return username

def priceSearch(maxPrice,userType):

    with open('studentData.json','r+') as file:
        studentData = json.load(file)
        file.close()

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()

    #student searches for tutor 
    if(userType == 'student'):

        for i in tutorData['users']:
            for j in i['price']:
                if(j <= maxPrice and j!='0'):
                    print("%s charges %s per hour." % (i['name'], i['price']) )
        return i['name'],i['price']

    elif(userType == 'tutor'):
        for i in studentData['users']:
            for j in i['price']:
                if(j <= maxPrice and j!='0'):
                    print("%s will pay up to %s per hour." % (i['name'], i['price']) )
        return i['name'],i['price']

def removeUser(username,userType):
    

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()

    if(userType == 'student'):
        with open('studentData.json','r+') as file:
            studentData = json.load(file)
            file.close()

        with open('studentData.json','w') as file:
            for i in studentData['users']:
                if(i['username'] == username):
                    studentData['users'].remove(i)
                    json.dump(studentData,file,indent=4)
                    print("User Removed")
            file.close()

    if(userType == 'tutor'):
        with open('tutorData.json','r+') as file:
            tutorData = json.load(file)
            file.close()

        with open('tutorData.json','w') as file:
            for i in tutorData['users']:
                if(i['username'] == username):
                    tutorData['users'].remove(i)
                    json.dump(tutorData,file,indent=4)
                    print("User Removed")
            file.close()

def listUsers(userType):
    with open('studentData.json','r+') as file:
        studentData = json.load(file)
        file.close()

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()

    if(userType == 'student'):
        print("\nTutors: ")
        for i in tutorData['users']:
            print("%s : $%s/hr : %s" % (i['name'], i['price'],i['classes']))
        print()

    if(userType == 'tutor'):
        print("\nStudents:")
        for i in studentData['users']:
            print("%s : $%s/hr : %s" % (i['name'], i['price'],i['classes']))
        print()
