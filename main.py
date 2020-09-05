import json

userInput = input("Student or Tutor: ")

tutorUsers = {}
tutorUsers['users'] = []


if(userInput == "student".casefold()):

    

    studentName = input("Name: ")
    studentPriceMax = input("Max Price/hour: ")
    studentClasses = input("Classes You Need Help In: ").split()

    userInfo = {
        'name' : studentName,
        'price' : studentPriceMax,
        'classes' : studentClasses
    }

    with open('studentData.json', 'r+') as file:
        data={}
        data = json.load(file)
        file.seek(0)
        data['users'].append(userInfo)
        json.dump(data,file,indent=4)
        file.close()


elif(userInput == "tutor".casefold()):
    tutorName = input("Name: ")
    tutorPrice = input("Price/hour: ")
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
        'classes' : tutorClasses
    }

    with open('tutorData.json', 'r+') as file:
        data={}
        data = json.load(file)
        file.seek(0)
        data['users'].append(userInfo)
        json.dump(data,file,indent=4)
        file.close()

else:
    print("invalid input")