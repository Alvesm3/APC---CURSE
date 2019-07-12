'''
Set up dictionaries 
*Dictionaries are powerful in that they are mutable, dynamic, and can be nested 
-> you can even map a list to a key which is what is done in this program
The dictionaries in this assignment emulate a database 
The key in a dictionary is synonymous with a primary key in a SQL table
The values in a dictioary is synonymous with the tuple in a SQL table
--Dictionary Defintions--
courses = {CRN : [Description]}
students = {UID : [Name, Major]}
instructor = {UID : [Name]}
Link courses and students
courses_students = {CRN : [populate list when a student signs up]}
Link courses and instructors
instructors_roster = {UID : [courses they teach]}
------------------------------------------------------------------------------------------
The dictionaries below would be modeled with classes and then instantiated with objects.
I have hardcoded them for now just to show functionality and to be able to test them.
------------------------------------------------------------------------------------------
'''
courses = {123456 : ["Math", 'Description', 25], 234567: ["Enlgish", 'Description', 25] }
students = {24 : ["Matt Alves", "BSCO"], 25 : ["Elon Musk", "Physics"]}
print(courses)

instructor = {32 : "Carpenter", 33: "Rawlins"}

courses_students = {123456 : [], 234567 : []}
instructors_roster = {32: [123456], 33: [234567]}
#--------------------------------------------------------------------------------------#
'''
STUDENT, INSTRUCTOR, ADMIN
In python, a dictioary is defined by a key:value pair
A key:value pair is called an item.
In CURSE, a key will be a unique idenfifer and the value
is acutally a [list] of values that stores information about
students, instructors, or courses.
#Printing all the courses
Print all the courses available with items() method
'''
#Printing all the courses
for keys, values in courses.items():
    print(keys, values)
#--------------------------------------------------------------------------------------#
'''
STUDENT
#Course Registration
This is where this algorthim shines. The magic of setdefault allows you to map a value to a specific key, i.e.
map a student to a specific course (CRN) even when the key hasn't been defined. In this case, the key (CRN) has been 
defined in courses_students. However, the courses_students dictioanry could dynamically change whenever a student signed
up for a course. This is because the course CRN is already defined in the courses dictioanry and we use that to index. The 
setdefault method does all the grunt work of adding the key and then adding the students to that specific CRN.
'''
#Course Registration
def register():
    #answer = int(input("What course would you like to sign up for? "))
    while True:
        crn = int(input("What course would you like to sign up for? "))
        while crn not in courses:
            if crn not in courses:
                print("Not a valid CRN, please try again")
                break
        if crn in courses:
            if students[25][0] in courses_students[crn]:
                print("You are already registered for this class")
                break
            else:
                courses_students.setdefault(crn, [])
                courses_students[crn].append(students[25][0])
                break

for i in range(2):
    register()
    
print(courses_students)
#--------------------------------------------------------------------------------------#
'''
STUDENT
#Check Student Schedule 
Iterate through the keys in course student list
If your name is a value in the courses_students values -> 
(we use students[25][0] so we can index to the position of the student -> [25]
and then we want the name which is the first element in the list -> [0])
Then iterate through the keys in courses -> this is because we want to print 
the course description as well! not just the CRN! and the course description
lives in courses and not courses_students
If the course CRN key in courses_students is equal to the course CRN key in courses
then we have a match, meaning you are in that respective course
thus print the CRN, and its description
'''
for keys in courses_students:
    print(keys, courses_students[keys])
 
for keys in courses:
    print(keys)
#Check Student Schedule 
for keys in courses_students:
    if students[25][0] in courses_students[keys]: #25 will be replaced with the students UID so students[uid][0], for now it is hardcoded -> UID will need to be fecthed when stuednt signs in
        for keys in courses:
            if keys == keys:
                print(keys, courses[keys])
#--------------------------------------------------------------------------------------#
'''
ADMIN
#Prints all the rosters
Prints out CRN and all the students that inhabit 
that course
'''
#Prints all the rosters
for x, y in courses_students.items():
    print(x, y)
#--------------------------------------------------------------------------------------#
'''
ADMIN & INSTRUCTOR
#Viewing instructors roster
Iterate through the keys in instructors_roster
If the CRN you entered is equal to a value found 
in the list of CRN's in instructors_roster
then print the students that are associated with that
CRN that you entered
'''
#Viewing instructors roster
crn = int(input("What course roster would you like to view"))
for keys in instructors_roster:
    if crn in instructors_roster[keys]:
        print(courses_students[crn])
#--------------------------------------------------------------------------------------#
'''
ADMIN
#Creating a new course
Take input
append input to courses dictionary
'''
#Creating a new course
print("Hello admin, please create a new class")
crn = int(input("What is the crn of the class"))
t, d, c, s = input("please enter a title, Description, capacity, and schedule for the class separated by commas").split(",")
#note: 
#crn will be saved as an int
#title, Description, capacity and schedule will be saved as strings
courses.setdefault(crn, []).append(t)
courses.setdefault(crn, []).append(d)
courses.setdefault(crn, []).append(c)
courses.setdefault(crn, []).append(s)

print(courses)
#--------------------------------------------------------------------------------------#
'''
ADMIN
#Deleting a course
Take input 
If the CRN is in courses
Then delete the course
'''
crn = int(input("What course would you like to remove? "))

if crn in courses:
    courses.pop(crn)
print(courses)
#--------------------------------------------------------------------------------------#
'''
ADMIN
#Force remove
Take input
If the CRN key exists in the courses_students 
If the student exists in the list of values 
that correspond to the entered CRN
Then remove them from that course
'''
#Force remove
print(courses_students.values())
print(courses_students)
crn = int(input("What course would you like to choose? "))
stu = input("what student would you like to delete? ")

if crn in courses_students:
    if stu in courses_students[crn]:
        courses_students[crn].remove(stu)

print(courses_students)
#--------------------------------------------------------------------------------------#
'''
ADMIN
#Force add
Take input
append input to courses_students
'''
#Force add
crn = int(input("What course would you like to choose? "))
stu = input("what student would you like to add? ")

courses_students.setdefault(crn, [])
courses_students[crn].append(stu)

print(courses_students)





