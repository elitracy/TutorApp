import json

def compareClasses(studentName,studentClasses):

    #get student name
    #get their classes
    #compare against all tutors with same classes
    #return tutors that have those classes

    with open('studentData.json','r+') as file:
        studentData = json.load(file)
        file.close()

    with open('tutorData.json','r+') as file:
        tutorData = json.load(file)
        file.close()


    #find correct student data
    for i in studentData['users']:
        if(i['name'] == studentName):
            correctUser = i

    #compare class student needs to all tutors
    for i in tutorData['users']:
        for j in i['classes']:
            if(j == studentClasses):
                print(i['name'])
        
        
        

compareClasses('Eli','CSCE121')